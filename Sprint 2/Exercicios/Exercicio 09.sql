SELECT
    tbvendas.cdpro,
    tbvendas.nmpro
FROM
    tbvendas
JOIN
    tbestoqueproduto ON tbvendas.cdpro = tbestoqueproduto.cdpro
WHERE
    tbvendas.status = 'Concluído'
    AND tbvendas.dtven BETWEEN '2014-02-03' AND '2018-02-02'
GROUP BY
    tbvendas.cdpro, tbvendas.nmpro
ORDER BY
    COUNT(tbvendas.cdpro) DESC
LIMIT 1;

