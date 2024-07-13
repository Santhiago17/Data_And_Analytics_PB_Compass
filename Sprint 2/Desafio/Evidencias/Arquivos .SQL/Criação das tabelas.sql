-- Executar cada comando para criação de tabela individualmente para verificar se cada tabela está nos conformes.


CREATE TABLE Cliente (
    idCliente INT PRIMARY KEY,
    cidadeCliente VARCHAR(100),
    estadoCliente VARCHAR(100),
    paisCliente VARCHAR(100)
);

CREATE TABLE Carro (
    idCarro INT PRIMARY KEY,
    kmCarro INT,
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(50),
    modeloCarro VARCHAR(50),
    anoCarro INT,
    idCombustivel INT
);

CREATE TABLE Combustivel (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(50)
);

CREATE TABLE Vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(100),
    sexoVendedor CHAR(1),
    estadoVendedor VARCHAR(100)
);

CREATE TABLE Locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    dataLocacao DATE,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(10, 2),
    dataEntrega DATE,
    horaEntrega TIME,
    idVendedor INT,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
);

