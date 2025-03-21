import time
import pyautogui
from pywinauto import Application
import pytesseract
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import cv2
from PIL import ImageGrab, ImageFilter, ImageOps, ImageEnhance
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def encontrar_e_clicar(imagem,confidence=0.7, timeout=10):
    """Localiza um botão pela imagem e clica nele."""
    inicio = time.time()
    while time.time() - inicio < timeout:
        posicao = pyautogui.locateCenterOnScreen(imagem, confidence=confidence)
        if posicao:
            
            pyautogui.click(posicao)
            print("clicado com sucesso!")
            return True
        time.sleep(1)
    print("não encontrado!")
    return False

def maximizar_janela():
    """Tenta maximizar a janela do sistema se não estiver maximizada."""
    app = Application().connect(title_re=".*Domínio Folha.*")
    janela = app.window(title_re=".*Domínio Folha.*")
    if not janela.is_maximized():
        janela.maximize()
        print("Janela maximizada.")
    else:
        print("Janela já está maximizada.")



def capturar_lista_rubricas(img_canto_superior="imagens_Lista_Rubrica/canto_coluna_codigo.png", 
                             img_canto_inferior="imagens_Lista_Rubrica/canto_coluna_setinha_rolagem.png", 
                             output_excel="rubricas.xlsx"):
    """Captura a lista de rubricas na tela e extrai os dados usando OCR."""
    time.sleep(2)

    # Localizar os cantos da área de captura
    canto_superior = pyautogui.locateCenterOnScreen(img_canto_superior, confidence=0.8)
    canto_inferior = pyautogui.locateCenterOnScreen(img_canto_inferior, confidence=0.8)

    if not canto_superior or not canto_inferior:
        print("Erro: Não foi possível localizar um dos cantos.")
        return None
    
    # Definir coordenadas do retângulo de captura
    x1, y1 = canto_superior
    x2, y2 = canto_inferior
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    y1 += 10

    # Capturar a área retangular definida pelos cantos
    captura = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    
    # PRÉ-PROCESSAMENTO PARA MELHORAR OCR
    captura = captura.convert("L")  # Converter para escala de cinza
    captura = ImageEnhance.Contrast(captura).enhance(2)  # Aumentar contraste
    captura = ImageEnhance.Sharpness(captura).enhance(2)  # Aumentar nitidez
    captura = ImageOps.invert(captura)  # Inverter cores (ajuda no OCR)
    
    # Salvar imagem para depuração
    captura.save("imagem_processada.png")
    
    # Extração de texto
    texto = pytesseract.image_to_string(captura, lang='por', config='--oem 1')
    print("Texto extraído:")
    print(texto)
    
    # Processamento dos dados extraídos
    linhas = texto.split("\n")
    dados_processados = []

    for linha in linhas:
        partes = linha.strip().split(" ", 1)  # Separar pelo primeiro espaço
        if len(partes) == 2:
            codigo, descricao = partes
        else:
            codigo, descricao = partes[0], ""

        if codigo.isdigit():  # Validar código
            dados_processados.append([codigo, descricao])

    # Criar DataFrame e salvar em Excel
    df = pd.DataFrame(dados_processados, columns=["Código", "Descrição"])
    df.to_excel(output_excel, index=False)
    
    print(f"Lista de rubricas capturada e salva em {output_excel}")
    return df


def aguardar_aparecer_e_executar(imagem_referencia ):
    print("Aguardando a abertura da tela desejada...")

    imagem_referencia   # Ajuste para o caminho correto da imagem de referência
    tempo_espera = 60  # Tempo máximo de espera em segundos
    inicio = time.time()

    while time.time() - inicio < tempo_espera:
        try:
            if pyautogui.locateCenterOnScreen(imagem_referencia, confidence=0.8):
                
                return 
        except:
            pass  
        
        time.sleep(2)

    print("Tempo esgotado! A tela não foi encontrada.")

def executar_automacao():
    """Executa a automação passo a passo."""
    #encontrar_e_clicar("imagens_Lista_Rubrica/rubrica_icone.png")
    #aguardar_aparecer_e_executar("imagens_Lista_Rubrica/icone_listar_rubricas.png")
    #encontrar_e_clicar("imagens_Lista_Rubrica/icone_listar_rubricas.png",0.6)
       
    #maximizar_janela()
    aguardar_aparecer_e_executar("imagens_Lista_Rubrica/image.png")
    encontrar_e_clicar("imagens_Lista_Rubrica/icone_buscar.png")
    time.sleep(2)
       
    
    lista_rubricas = capturar_lista_rubricas()
    return lista_rubricas

if __name__ == "__main__":
    executar_automacao()
