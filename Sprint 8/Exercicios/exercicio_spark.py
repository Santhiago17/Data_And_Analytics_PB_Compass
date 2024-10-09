from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import rand,when
from pyspark.sql.functions import floor

# Etapa 1
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()
    

# Lendo o arquivo
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)


# Altera nome da coluna
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")


df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(rand() < 0.33, "Fundamental")
    .when((rand() >= 0.33) & (rand() < 0.66),"Medio")
    .otherwise("Superior")
)


paises = [
    "Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", "Equador", 
    "Guiana", "Paraguai", "Peru", "Suriname", "Uruguai", "Venezuela", "Guiana Francesa"
]

# Gerando um valor aleatório para selecionar os paises
df_nomes = df_nomes.withColumn("random_val", floor(rand() * 13))

df_nomes = df_nomes.withColumn(
    "Pais",
    when(df_nomes["random_val"] == 0, paises[0])
    .when(df_nomes["random_val"] == 1, paises[1])
    .when(df_nomes["random_val"] == 2, paises[2])
    .when(df_nomes["random_val"] == 3, paises[3])
    .when(df_nomes["random_val"] == 4, paises[4])
    .when(df_nomes["random_val"] == 5, paises[5])
    .when(df_nomes["random_val"] == 6, paises[6])
    .when(df_nomes["random_val"] == 7, paises[7])
    .when(df_nomes["random_val"] == 8, paises[8])
    .when(df_nomes["random_val"] == 9, paises[9])
    .when(df_nomes["random_val"] == 10, paises[10])
    .when(df_nomes["random_val"] == 11, paises[11])
    .otherwise(paises[12])
)
df_nomes = df_nomes.drop("random_val")


df_nomes = df_nomes.withColumn("AnoNascimento", floor(rand() * (2010 - 1945 + 1)) + 1945)

df_select = df_nomes.filter(df_nomes["AnoNascimento"] >= 2000)

df_select.select("Nomes").show(10)


# -----------------------Etapa 7 ------------------

df_nomes.createOrReplaceTempView("Pessoas")

df_select_sql = spark.sql("SELECT Nomes FROM Pessoas WHERE AnoNascimento >= 2000")

df_select_sql.show(10)

# -------------------------Etapa 8 --------------------

# Filtrando as pessoas que nasceram entre 1980 e 1994 
df_millennials = df_nomes.filter((df_nomes["AnoNascimento"] >= 1980) & (df_nomes["AnoNascimento"] <= 1994))

# Contando o número de pessoas 
count_millennials = df_millennials.count()

print(f"Número de pessoas da Geração Millennial: {count_millennials}")


# ---------------------------Etapa 9 -------------------

df_nomes.createOrReplaceTempView("Pessoas")

# Executando a consulta SQL para contar o número de pessoas (1980 a 1994)
df_millennials_sql = spark.sql("SELECT COUNT(*) as count_millennials FROM Pessoas WHERE AnoNascimento >= 1980 AND AnoNascimento <= 1994")

df_millennials_sql.show()

# ------------------------ Etapa 10 ----------------------

df_nomes.createOrReplaceTempView("Pessoas")

df_geracoes_pais = spark.sql(
    """
    SELECT 
        Pais, 
        CASE 
            WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
            WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
            WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
            WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
            ELSE 'Outras'
        END AS Geracao,
        COUNT(*) AS Quantidade
    FROM Pessoas
    WHERE AnoNascimento BETWEEN 1944 AND 2015
    GROUP BY Pais, Geracao
    ORDER BY Pais ASC, Geracao ASC, Quantidade ASC
"""
)

df_geracoes_pais.show(truncate=False)
