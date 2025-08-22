import win32print
import win32ui
from PIL import Image, ImageWin
import os

def imprimir_imagem(nome_imagem, path, printer_name=None):
    if printer_name is None:
        printer_name = win32print.GetDefaultPrinter()
    img_path = './etiquetas/'+path+'/'+nome_imagem+'.png'

    if not os.path.exists(img_path):
        print(f"Arquivo não encontrado: {img_path}")
        return

    try:
        img = Image.open(img_path)
        img.verify()  # Verifica se a imagem não está corrompida
        img = Image.open(img_path)  # Reabra para uso após verify()
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
        return
    
    img_width, img_height = img.size

    # Configurações
    num_linhas = 4
    num_colunas = 3

    # Espaçamento entre etiquetas em mm e pixels
    espaco_horizontal_mm = 0  # espaço entre colunas
    espaco_vertical_mm = 20   # espaço entre linhas
    margem_superior_mm = 0 # NOVA LINHA: Margem para mover tudo para baixo
    dpi = 203  # ajuste se necessário

    espaco_horizontal_px = int((espaco_horizontal_mm / 25.4) * dpi)
    espaco_vertical_px = int((espaco_vertical_mm / 25.4) * dpi)
    margem_superior_px = int((margem_superior_mm / 25.4) * dpi)

    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC(printer_name)
    hDC.StartDoc("Etiqueta")
    hDC.StartPage()

    for linha in range(num_linhas):
        y = margem_superior_px + linha * (img_height + espaco_vertical_px)
        for coluna in range(num_colunas):
            x = coluna * (img_width + espaco_horizontal_px)
            dib = ImageWin.Dib(img)
            dib.draw(hDC.GetHandleOutput(), (x, y, x + img_width, y + img_height))

    hDC.EndPage()
    hDC.EndDoc()
    hDC.DeleteDC()

def imprimir_2cols(nome_imagem, path, printer_name=None):
    if printer_name is None:
        printer_name = win32print.GetDefaultPrinter()
    img_path = './etiquetas/'+path+'/'+nome_imagem+'.png'

    if not os.path.exists(img_path):
        print(f"Arquivo não encontrado: {img_path}")
        return

    try:
        img = Image.open(img_path)
        img.verify()  # Verifica se a imagem não está corrompida
        img = Image.open(img_path)  # Reabra para uso após verify()
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
        return
    
    img_width, img_height = img.size

    # Configurações
    num_linhas = 4
    num_colunas = 2

    # Espaçamento entre etiquetas em mm e pixels
    espaco_horizontal_mm = 0  # espaço entre colunas
    espaco_vertical_mm = 6   # espaço entre linhas
    margem_superior_mm = 0.5 # NOVA LINHA: Margem para mover tudo para baixo
    dpi = 203  # ajuste se necessário

    espaco_horizontal_px = int((espaco_horizontal_mm / 25.4) * dpi)
    espaco_vertical_px = int((espaco_vertical_mm / 25.4) * dpi)
    margem_superior_px = int((margem_superior_mm / 25.4) * dpi)

    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC(printer_name)
    hDC.StartDoc("Etiqueta")
    hDC.StartPage()

    for linha in range(num_linhas):
        y = margem_superior_px + linha * (img_height + espaco_vertical_px)
        for coluna in range(num_colunas):
            x = coluna * (img_width + espaco_horizontal_px)
            dib = ImageWin.Dib(img)
            dib.draw(hDC.GetHandleOutput(), (x, y, x + img_width, y + img_height))

    hDC.EndPage()
    hDC.EndDoc()
    hDC.DeleteDC()