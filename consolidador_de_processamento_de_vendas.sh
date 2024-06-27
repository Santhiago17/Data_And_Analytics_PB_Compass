#!/bin/bash

# Diretório atual
script_dir=$(dirname "$0")
cd "$script_dir"

# Diretório onde o relatório é armazenado
backup_dir="vendas/backup"

# Arquivo final de relatório
relatorio_final="vendas/backup/relatorio_final.txt"

# Arquivo de relatório acumulado
relatorio_acumulado="vendas/backup/relatorio.txt"

# Verifique se o diretório de backup existe
if [ ! -d "$backup_dir" ]; then
    echo "Erro: O diretório $backup_dir não foi encontrado."
    exit 1
fi

# Verifique se o relatório acumulado existe
if [ ! -f "$relatorio_acumulado" ]; then
    echo "Erro: O arquivo $relatorio_acumulado não foi encontrado."
    exit 1
fi

# Inicializar o arquivo final de relatório
echo "Consolidando relatórios em $relatorio_final..."
echo "Relatório Consolidado" > $relatorio_final
echo "====================" >> $relatorio_final

# Adicionar o conteúdo do relatório acumulado ao relatório final
cat "$relatorio_acumulado" >> $relatorio_final

echo "Processo de consolidação concluído. Verificar o arquivo $relatorio_final."

