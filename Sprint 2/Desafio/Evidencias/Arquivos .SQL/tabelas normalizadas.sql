-- --------------------------------------------------------
-- Servidor:                     C:\Users\santh\Desktop\Estágio - Compass\Sprint 2\SQL\Desafio final da Sprint 2\concessionaria.sqlite
-- Versão do servidor:           3.45.3
-- OS do Servidor:               
-- HeidiSQL Versão:              12.7.0.6850
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES  */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Copiando estrutura do banco de dados para concessionaria
DROP DATABASE IF EXISTS "concessionaria";
CREATE DATABASE IF NOT EXISTS "concessionaria";
;

-- Copiando dados para a tabela concessionaria.Carro: 10 rows
/*!40000 ALTER TABLE "Carro" DISABLE KEYS */;
INSERT INTO "Carro" ("idCarro", "kmCarro", "classiCarro", "marcaCarro", "modeloCarro", "anoCarro", "idCombustivel") VALUES
	(1, 1800, 'AAAKNS8JS76S39', 'Toyota', 'Corolla XEI', 2023, 3),
	(2, 10000, 'AKIUNS1JS76S39', 'Nissan', 'Versa', 2019, 2),
	(3, 121700, 'DKSHKNS8JS76S39', 'VW', 'Fusca 78', 1978, 1),
	(4, 55000, 'LLLUNS1JS76S39', 'Nissan', 'Versa', 2020, 2),
	(5, 28000, 'MSLUNS1JS76S39', 'Nissan', 'Frontier', 2022, 4),
	(6, 21800, 'SKIUNS8JS76S39', 'Nissan', 'Versa', 2019, 1),
	(7, 212800, 'SSIUNS8JS76S39', 'Fiat', 'Fiat 147', 1996, 1),
	(10, 211800, 'LKIUNS8JS76S39', 'Fiat', 'Fiat 147', 1996, 1),
	(98, 25412, 'AKJHKN98JY76539', 'Fiat', 'Fiat Uno', 2000, 1),
	(99, 20000, 'IKJHKN98JY76539', 'Fiat', 'Fiat Palio', 2010, 1);
/*!40000 ALTER TABLE "Carro" ENABLE KEYS */;

-- Copiando dados para a tabela concessionaria.Cliente: 10 rows
/*!40000 ALTER TABLE "Cliente" DISABLE KEYS */;
INSERT INTO "Cliente" ("idCliente", "cidadeCliente", "estadoCliente", "paisCliente") VALUES
	(2, 'São Paulo', 'São Paulo', 'Brasil'),
	(3, 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil'),
	(4, 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil'),
	(6, 'Belo Horizonte', 'Minas Gerais', 'Brasil'),
	(10, 'Rio Branco', 'Acre', 'Brasil'),
	(20, 'Macapá', 'Amapá', 'Brasil'),
	(22, 'Porto Alegre', 'Rio Grande do Sul', 'Brasil'),
	(23, 'Eusébio', 'Ceará', 'Brasil'),
	(5, 'Manaus', 'Amazonas', 'Brasil'),
	(26, 'Campo Grande', 'Mato Grosso do Sul', 'Brasil');
/*!40000 ALTER TABLE "Cliente" ENABLE KEYS */;

-- Copiando dados para a tabela concessionaria.Combustivel: -1 rows
/*!40000 ALTER TABLE "Combustivel" DISABLE KEYS */;
INSERT INTO "Combustivel" ("idCombustivel", "tipoCombustivel") VALUES
	(1, 'Gasolina'),
	(2, 'Etanol'),
	(3, 'Flex'),
	(4, 'Diesel');
/*!40000 ALTER TABLE "Combustivel" ENABLE KEYS */;

-- Copiando dados para a tabela concessionaria.Locacao: -1 rows
/*!40000 ALTER TABLE "Locacao" DISABLE KEYS */;
INSERT INTO "Locacao" ("idLocacao", "idCliente", "idCarro", "dataLocacao", "horaLocacao", "qtdDiaria", "vlrDiaria", "dataEntrega", "horaEntrega", "idVendedor") VALUES
	(1, 2, 98, '20150110', '10:00', 2, 100, '20150112', '10:00', 5),
	(2, 2, 98, '20150210', '12:00', 2, 100, '20150212', '12:00', 5),
	(3, 3, 99, '20150213', '12:00', 2, 150, '20150215', '12:00', 6),
	(4, 4, 99, '20150215', '13:00', 5, 150, '20150220', '13:00', 6),
	(5, 4, 99, '20150302', '14:00', 5, 150, '20150307', '14:00', 7),
	(6, 6, 3, '20160302', '14:00', 10, 250, '20160312', '14:00', 8),
	(7, 6, 3, '20160802', '14:00', 10, 250, '20160812', '14:00', 8),
	(8, 4, 3, '20170102', '18:00', 10, 250, '20170112', '18:00', 6),
	(9, 4, 3, '20180102', '18:00', 10, 280, '20180112', '18:00', 6),
	(10, 10, 10, '20180302', '18:00', 10, 50, '20180312', '18:00', 16),
	(11, 20, 7, '20180401', '11:00', 10, 50, '20180411', '11:00', 16),
	(12, 20, 6, '20200401', '11:00', 10, 150, '20200411', '11:00', 16),
	(13, 22, 2, '20220501', '8:00', 20, 150, '20220521', '18:00', 30),
	(14, 22, 2, '20220601', '8:00', 20, 150, '20220621', '18:00', 30),
	(15, 22, 2, '20220701', '8:00', 20, 150, '20220721', '18:00', 30),
	(16, 22, 2, '20220801', '8:00', 20, 150, '20220721', '18:00', 30),
	(17, 23, 4, '20220901', '8:00', 20, 150, '20220921', '18:00', 31),
	(18, 23, 4, '20221001', '8:00', 20, 150, '20221021', '18:00', 31),
	(19, 23, 4, '20221101', '8:00', 20, 150, '20221121', '18:00', 31),
	(20, 5, 1, '20230102', '18:00', 10, 880, '20230112', '18:00', 16),
	(21, 5, 1, '20230115', '18:00', 10, 880, '20230125', '18:00', 16),
	(22, 26, 5, '20230125', '8:00', 5, 600, '20230130', '18:00', 32),
	(23, 26, 5, '20230131', '8:00', 5, 600, '20230205', '18:00', 32),
	(24, 26, 5, '20230206', '8:00', 5, 600, '20230211', '18:00', 32),
	(25, 26, 5, '20230212', '8:00', 5, 600, '20230217', '18:00', 32),
	(26, 26, 5, '20230218', '8:00', 1, 600, '20230219', '18:00', 32);
/*!40000 ALTER TABLE "Locacao" ENABLE KEYS */;

-- Copiando dados para a tabela concessionaria.Vendedor: -1 rows
/*!40000 ALTER TABLE "Vendedor" DISABLE KEYS */;
INSERT INTO "Vendedor" ("idVendedor", "nomeVendedor", "sexoVendedor", "estadoVendedor") VALUES
	(5, 'Vendedor cinco', '0', 'São Paulo'),
	(6, 'Vendedora seis', '1', 'São Paulo'),
	(7, 'Vendedora sete', '1', 'Rio de Janeiro'),
	(8, 'Vendedora oito', '1', 'Minas Gerais'),
	(16, 'Vendedor dezesseis', '0', 'Amazonas'),
	(30, 'Vendedor trinta', '0', 'Rio Grande do Sul'),
	(31, 'Vendedor trinta e um', '0', 'Ceará'),
	(32, 'Vendedora trinta e dois', '1', 'Mato Grosso do Sul');
/*!40000 ALTER TABLE "Vendedor" ENABLE KEYS */;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
