"""1)	Замените две равные буквы следующей буквой алфавита (две буквы преобразуются в одну):
"aa" => "b", "bb" => "c", .. "zz" => "a".
Одинаковые буквы не обязательно должны быть смежными.
Повторяйте эту операцию до тех пор, пока не останется никаких возможных замен.
Вернуть строку.
Пример:
let str = "zzzab"
    str = "azab"
    str = "bzb"
    str = "cz"
return "cz"
Заметки
Порядок букв в результате не имеет значения.
Буквы "zz"трансформируются в "a".
Будут только строчные буквы."""



def zamena(str):
    new = "abcdefghijklmnopqrstuvwxyza"
    for i in str:
        if str.count(i)>1:
            str = str.replace(i,"",2)+new[new.index(i)+1]
            return zamena(str)
    return str
str=input()
print((zamena(str)))