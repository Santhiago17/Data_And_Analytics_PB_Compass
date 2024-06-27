#!/bin/bash

# Diretório atual
script_dir=$(dirname "$0")
cd "$script_dir"

# Verifica se o arquivo de vendas existe
if [ ! -f dados_de_vendas.csv ]; then
    echo "Erro: O arquivo dados_de_vendas.csv não foi encontrado."
    exit 1
fi

# Passo 1: Criar o diretório 'vendas'
echo "Criando o diretório vendas..."
mkdir -p vendas

# Passo 2: Copiar o arquivo 'dados_de_vendas.csv' para o diretório 'vendas'
echo "Copiando o arquivo dados_de_vendas.csv para o diretório vendas..."
cp dados_de_vendas.csv vendas/

# Passo 3: Criar o subdiretório 'backup' dentro de 'vendas'
echo "Criando o subdiretório backup dentro de vendas..."
mkdir -p vendas/backup

# Passo 4: Obter a data atual no formato yyyymmdd
data=$(date +%Y%m%d)

# Passo 5: Fazer uma cópia do arquivo 'dados_de_vendas.csv' no subdiretório 'backup' com a data no nome
echo "Copiando o arquivo dados_de_vendas.csv para vendas/backup/dados-${data}.csv..."
cp vendas/dados_de_vendas.csv vendas/backup/dados-${data}.csv

# Passo 6: Renomear o arquivo 'dados-yyyymmdd.csv' para 'backup-dados-yyyymmdd.csv'
echo "Renomeando o arquivo para backup-dados-${data}.csv..."
mv vendas/backup/dados-${data}.csv vendas/backup/backup-dados-${data}.csv

# Passo 7: Obter informações para o relatório
echo "Obtendo informações para o relatório..."
data_sistema=$(date +"%Y/%m/%d %H:%M")
data_primeiro_registro=$(awk -F ',' 'NR==2 {print $5}' vendas/backup/backup-dados-${data}.csv)
data_ultimo_registro=$(awk -F ',' 'END {print $5}' vendas/backup/backup-dados-${data}.csv)
total_itens_diferentes=$(awk -F ',' 'NR>1 {print $2}' vendas/backup/backup-dados-${data}.csv | sort | uniq | wc -l)

# Passo 8: Criar o arquivo relatorio.txt com as informações no subdiretório 'backup'
echo "Criando o arquivo relatorio.txt..."
relatorio="vendas/backup/relatorio.txt"
{
    echo "-----------------------------"
    echo "Data do Sistema: ${data_sistema}"
    echo "Data do Primeiro Registro: ${data_primeiro_registro}"
    echo "Data do Último Registro: ${data_ultimo_registro}"
    echo "Total de Itens Diferentes Vendidos: ${total_itens_diferentes}"
    echo "Primeiras linhas do arquivo backup-dados-${data}.csv:"
    head -n 10 vendas/backup/backup-dados-${data}.csv
} >> ${relatorio}

# Passo 9: Compactar o arquivo 'backup-dados-yyyymmdd.csv' para 'backup-dados-yyyymmdd.zip'
echo "Compactando o arquivo backup-dados-${data}.csv para backup-dados-${data}.zip..."
zip vendas/backup/backup-dados-${data}.zip vendas/backup/backup-dados-${data}.csv

# Passo 10: Remover o arquivo 'backup-dados-yyyymmdd.csv' do diretório 'backup'
echo "Removendo o arquivo backup-dados-${data}.csv do diretório backup..."
rm -f vendas/backup/backup-dados-${data}.csv

# Passo 11: Remover o arquivo 'dados_de_vendas.csv' do diretório 'vendas'
echo "Removendo o arquivo dados_de_vendas.csv do diretório vendas..."
rm -f vendas/dados_de_vendas.csv

echo "Processo concluído. Verifique o diretório vendas/backup para os arquivos criados."

