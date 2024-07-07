SELECT
	tbvendedor.cdvdd,
	tbvendedor.nmvdd
FROM
	tbvendas
JOIN 
	tbvendedor 
ON 
	tbvendas.cdvdd = tbvendedor.cdvdd
WHERE
	tbvendas.status = 'Concluído'
GROUP BY
	tbvendedor.cdvdd, tbvendedor.nmvdd
ORDER BY
	COUNT(tbvendas.cdvdd) DESC
LIMIT
	1

