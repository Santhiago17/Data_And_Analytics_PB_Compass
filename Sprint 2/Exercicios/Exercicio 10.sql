SELECT
    tbvendedor.nmvdd AS vendedor,
    SUM(tbvendas.qtd * tbvendas.vrunt) AS valor_total_vendas,
    ROUND(SUM(tbvendas.qtd * tbvendas.vrunt) * tbvendedor.perccomissao / 100, 2) AS comissao
FROM
    tbvendas
JOIN
    tbvendedor ON tbvendas.cdvdd = tbvendedor.cdvdd
WHERE
    tbvendas.status = 'Concluído'
GROUP BY
    tbvendedor.nmvdd, tbvendedor.perccomissao
ORDER BY
    comissao DESC;
