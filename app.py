import pandas as pd
import math
from imprimir import imprimir_imagem, imprimir_2cols
from gerarImagem import gerar_imagem_3col, gerar_imagem_2col
import time
from datetime import datetime
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def imprimir_excel():

    if 'excel' not in request.files:
        return "Nenhum arquivo Excel enviado", 400

    arquivo = request.files['excel']
    
    if not arquivo.filename.endswith('.xlsx'):
        return "Arquivo enviado não é um arquivo Excel válido", 400

    df = pd.read_excel(arquivo)
    date = datetime.now()
    day = f"{date.day:02d}"
    month = f"{date.month:02d}"
    year = f"{date.year:04d}"
    path3col = f"{year}/3 col/{day}-{month}/"

    for index, row in df.iterrows():
        nome = row['Nome']
        rawPrice = str(row['Valor']).replace(',', '.')
        preco = float(rawPrice)
        quantidade = math.ceil(int(row['Quantidade']) / 3)  # arredonda para cima

        os.makedirs(f"./etiquetas/{path3col}", exist_ok=True)  # cria o diretório se não existir

        name_img = gerar_imagem_3col(nome, preco, path3col)
        time.sleep(2)
        for i in range(quantidade):
            imprimir_imagem(name_img, path3col)
        time.sleep(5)
    
    return "Impressão concluída com sucesso!", 200

@app.route('/big', methods=['POST'])
def imprimir_big():

    if 'excel' not in request.files:
        return "Nenhum arquivo Excel enviado", 400

    arquivo = request.files['excel']
    
    if not arquivo.filename.endswith('.xlsx'):
        return "Arquivo enviado não é um arquivo Excel válido", 400

    df = pd.read_excel(arquivo)
    date = datetime.now()
    day = f"{date.day:02d}"
    month = f"{date.month:02d}"
    year = f"{date.year:04d}"
    path2col = f"{year}/2 col/{day}-{month}/"

    for index, row in df.iterrows():
        nome = row['Nome']
        rawPrice = str(row['Valor']).replace(',', '.')
        preco = float(rawPrice)
        quantidade = math.ceil(int(row['Quantidade']) / 2)  # arredonda para cima

        os.makedirs(f"./etiquetas/{path2col}", exist_ok=True)  # cria o diretório se não existir

        name_img = gerar_imagem_2col(nome, preco, path2col)
        time.sleep(2)
        for i in range(quantidade):
            imprimir_2cols(name_img, path2col)
        time.sleep(5)
    
    return "Impressão concluída com sucesso!", 200

if __name__ == "__main__":
    app.run(debug=True)
