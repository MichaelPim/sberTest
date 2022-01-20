SELECT
    p.name AS product_name
    ,EXTRACT(YEAR FROM s.date)::INT AS year
    ,EXTRACT(MONTH from s.date)::INT AS month
    ,EXTRACT(DAY from s.date)::INT AS day
    ,SUM((p.price*sd.count)) AS total
FROM sales_details sd
    INNER JOIN sales s on sd.sale_id = s.id
    INNER JOIN products p ON sd.product_id = p.id
GROUP BY
  Product_name
  ,ROLLUP(year,month,day)
ORDER BY
  product_name
  ,year
  ,month
  ,day	
