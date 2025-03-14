import cv2
import pytesseract
import numpy as np
import pandas as pd
import re

# Configurar o caminho do Tesseract caso necessário (Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocessar_imagem(imagem_path):
    """Carrega e pré-processa a imagem para OCR."""
    imagem = cv2.imread(imagem_path)
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_suavizada = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)
    _, imagem_bin = cv2.threshold(imagem_suavizada, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return imagem_bin

def extrair_texto(imagem):
    """Extrai todo o texto da imagem."""
    return pytesseract.image_to_string(imagem, lang='eng')

def extrair_tabela(imagem):
    """Extrai dados estruturados da tabela, como datas e horários."""
    dados_ocr = pytesseract.image_to_data(imagem, output_type=pytesseract.Output.DATAFRAME)
    dados_ocr = dados_ocr[dados_ocr.text.notna()]
    
    # Expressões regulares para identificar datas e horários
    padrao_horario = re.compile(r"\b\d{2}:\d{2}\b")
    padrao_data = re.compile(r"\b\d{2}\b")
    
    # Filtrar horários e datas
    horarios = [texto for texto in dados_ocr.text if padrao_horario.match(str(texto))]
    datas = [texto for texto in dados_ocr.text if padrao_data.match(str(texto)) and texto not in horarios]
    
    return pd.DataFrame({'Data': datas[:len(horarios)//4], 'Entrada1': horarios[0::4], 'Saída1': horarios[1::4],
                         'Entrada2': horarios[2::4], 'Saída2': horarios[3::4]})

# Caminho da imagem
imagem_path = "FOLHA_PONTO_02_-_2024_-_LUCAS_CASTRO_DOS_SANTOS.jpg"  # Substitua pelo caminho real

# Processamento da imagem
imagem_processada = preprocessar_imagem(imagem_path)

# Extração de texto bruto
texto_extraido = extrair_texto(imagem_processada)
print("Texto Extraído:")
print(texto_extraido)

# Extração de tabela estruturada
tabela_ponto = extrair_tabela(imagem_processada)
print("\nTabela Estruturada:")
print(tabela_ponto)