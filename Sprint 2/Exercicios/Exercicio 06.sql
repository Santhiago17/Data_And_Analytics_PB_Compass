SELECT
	autor.codautor,
	autor.nome,
	COUNT(livro.autor) AS quantidade_publicacoes
FROM
	livro
	JOIN autor ON livro.autor = autor.codautor
GROUP BY
	autor.codautor,
	autor.nome
ORDER BY
	quantidade_publicacoes DESC
LIMIT
	1