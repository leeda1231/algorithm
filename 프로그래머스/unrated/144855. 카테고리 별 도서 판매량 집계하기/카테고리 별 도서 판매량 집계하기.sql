SELECT CATEGORY, SUM(SALES) AS TOTAL_SALES
FROM BOOK_SALES AS S LEFT JOIN BOOK AS B ON S.BOOK_ID = B.BOOK_ID
WHERE DATE_FORMAT(S.SALES_DATE,'%Y-%m') = '2022-01'
GROUP BY CATEGORY
ORDER BY CATEGORY
