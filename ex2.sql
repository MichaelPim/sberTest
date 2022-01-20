drop table if exists documents;

create table if not exists documents (
	id integer,
	data text
);

select * from documents;

drop table if exists documents_changelog;

create table if not exists documents_changelog (
	id integer,
	document_id integer,
	old_data text,
	new_data text
);

select * from documents_changelog;


drop function if exists insert_copy();
drop trigger if exists insert1 on documents_changelog;
drop function if exists update_copy();
drop trigger if exists update1 on documents_changelog;
drop function if exists delete_copy();
drop trigger if exists delete1 on documents_changelog;


insert into documents
values (1, 'hello'), (2, 'world');


update documents set data='hi'
where data='hello';


delete from documents
where data='hi';



create function insert_copy()
returns trigger
as
$$
begin
	insert into documents_changelog (document_id, new_data)
	select new.id, new.data
	from documents;
	return documents_changelog.document_id, documents_changelog.new_data;
end;
$$language plpgsql;


create trigger insert1
after insert
on documents
for each row
execute procedure insert_copy();


create function update_copy()
returns trigger
as
$$
begin
insert into documents_changelog(documents.id, documents.old_data, documents.new_data)
values (documents.id, documents.data);
end;
$$language plpgsql;


create trigger update1
after update
on documents_changelog
for each row
execute procedure update_copy();



create function delete_copy()
returns trigger
as
$$
begin
insert into documents_changelog(document_id, old_data)
values (documents.id, documents.data);
end;
$$language plpgsql;



create trigger delete1
after delete
on documents_changelog
for each row
execute procedure delete_copy();

INSERT INTO documents_changelog(document_id, old_data, new_data) VALUES (-1, NULL, NULL);
