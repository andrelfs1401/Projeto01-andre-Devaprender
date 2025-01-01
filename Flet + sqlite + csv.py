import flet as ft
from datetime import datetime
import sqlite3
import os
import csv

def main(page: ft.Page):
    page.title = "Calculadora de Quantidade"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 10
    page.spacing = 10
    
    # Conectar ao banco de dados SQLite (ou criar se não existir)
    conn = sqlite3.connect('/storage/emulated/0/Download/calculos.db')
    cursor = conn.cursor()
    
    # Criar tabela se não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS calculos (
                        inicio INTEGER,
                        fim INTEGER,
                        rodada INTEGER,
                        quantidade INTEGER,
                        data TEXT)''')
    conn.commit()

    # Carregar dados da tabela
    calculos = cursor.execute('SELECT * FROM calculos').fetchall()

    # Obtém a data de hoje no formato DD/MM/YY
    data_hoje = datetime.today().strftime('%d/%m/%y')

    # Campos de entrada
    input_inicio = ft.TextField(label="Início", width=200)
    input_fim = ft.TextField(label="Fim", width=200)
    input_rodada = ft.TextField(label="Rodada", width=200)
    input_data = ft.TextField(label="Data (DD/MM/YY)", value=data_hoje, width=200)

    # Campo para exibir o resultado
    result_text = ft.Text(value="Quantidade será exibida aqui", size=18)

    def calcular_quantidade(e):
        try:
            inicio = int(input_inicio.value)
            fim = int(input_fim.value)
            rodada = int(input_rodada.value)
            Quantidade = (rodada * 100) - inicio + fim
            result_text.value = f"Quantidade: {Quantidade}"
        except ValueError:
            result_text.value = "Por favor, insira números válidos no formato correto."

        page.update()

    def inserir_na_lista(e):
        try:
            inicio = int(input_inicio.value)
            fim = int(input_fim.value)
            rodada = int(input_rodada.value)
            data_str = input_data.value

            # Converte a string da data para um objeto datetime no formato DD/MM/YY
            data = datetime.strptime(data_str, '%d/%m/%y').date().strftime('%Y-%m-%d')

            Quantidade = (rodada * 100) - inicio + fim

            # Inserir dados no banco de dados
            cursor.execute('INSERT INTO calculos (inicio, fim, rodada, quantidade, data) VALUES (?, ?, ?, ?, ?)',
                           (inicio, fim, rodada, Quantidade, data))
            conn.commit()

            result_text.value = "Informações inseridas na lista e salvas com sucesso."
        except ValueError:
            result_text.value = "Erro ao inserir na lista. Por favor, verifique os valores."

        page.update()

    def exportar_csv(e):
        try:
            # Consultar dados do banco de dados
            dados = cursor.execute('SELECT quantidade, data FROM calculos').fetchall()
            
            # Nome do arquivo CSV
            nome_arquivo_csv = os.path.join("/storage/emulated/0/Download", "calculos_exportados.csv")
            
            # Salvar dados no arquivo CSV
            with open(nome_arquivo_csv, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Quantidade', 'Data'])
                writer.writerows(dados)

            result_text.value = "Arquivo CSV exportado com sucesso."
        except Exception as ex:
            result_text.value = f"Erro ao exportar o arquivo CSV: {ex}"

        page.update()

    # Botão para calcular
    calcular_button = ft.ElevatedButton(
        text="Calcular",
        on_click=calcular_quantidade
    )

    # Botão para inserir na lista
    inserir_button = ft.ElevatedButton(
        text="Inserir na Lista",
        on_click=inserir_na_lista
    )

    # Botão para exportar o arquivo CSV
    exportar_csv_button = ft.ElevatedButton(
        text="Exportar CSV",
        on_click=exportar_csv
    )

    # Adicionando os componentes à página
    page.add(
        ft.Column(
            [
                input_inicio,
                input_fim,
                input_rodada,
                input_data,
                calcular_button,
                inserir_button,
                exportar_csv_button,
                result_text
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    # Ajusta os componentes com base no tamanho da tela
    def ajustar_tela(e):
        largura_tela = page.window_width

        if largura_tela < 500:  # Tamanho típico de um smartphone
            largura_input = 150
            tamanho_texto = 16
        else:
            largura_input = 200
            tamanho_texto = 18

        # Atualiza os componentes com os novos tamanhos
        input_inicio.width = largura_input
        input_fim.width = largura_input
        input_rodada.width = largura_input
        input_data.width = largura_input
        result_text.size = tamanho_texto

        page.update()

    # Ajusta a tela inicialmente e ao redimensionar
    ajustar_tela(None)
    page.on_resize = ajustar_tela

ft.app(target=main)
