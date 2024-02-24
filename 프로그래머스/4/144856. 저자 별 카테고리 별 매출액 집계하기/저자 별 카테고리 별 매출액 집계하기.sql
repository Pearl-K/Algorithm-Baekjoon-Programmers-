
SELECT a.author_id as AUTHOR_ID, a.author_name as AUTHOR_NAME, b.category, sum(s.sales*b.price) as TOTAL_SALES
FROM BOOK b, AUTHOR a, BOOK_SALES s
WHERE s.sales_date like '2022-01%' and b.book_id = s.book_id and b.author_id = a.author_id
GROUP BY a.author_id, b.category
ORDER BY a.author_id asc, b.category desc