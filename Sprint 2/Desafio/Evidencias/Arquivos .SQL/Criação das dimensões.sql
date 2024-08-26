CREATE VIEW DimCliente AS
SELECT 
    idCliente,
    cidadeCliente,
    estadoCliente,
    paisCliente
FROM Cliente;


CREATE VIEW DimCarro AS
SELECT 
    Carro.idCarro,
    kmCarro,
    classiCarro,
    marcaCarro,
    modeloCarro,
    anoCarro,
    Combustivel.tipoCombustivel
FROM Carro
JOIN Combustivel ON Carro.idCombustivel = Combustivel.idCombustivel;



CREATE VIEW DimCombustivel AS
SELECT 
    idCombustivel,
    tipoCombustivel
FROM Combustivel;


CREATE VIEW DimVendedor AS
SELECT 
    idVendedor,
    nomeVendedor,
    sexoVendedor,
    estadoVendedor
FROM Vendedor;



CREATE VIEW FatoLocacao AS
SELECT 
    Locacao.idLocacao,
    Locacao.idCliente,
    Locacao.idCarro,
    Locacao.idVendedor,
    Locacao.dataLocacao,
    Locacao.horaLocacao,
    Locacao.qtdDiaria,
    Locacao.vlrDiaria,
    Locacao.dataEntrega,
    Locacao.horaEntrega
FROM Locacao;

