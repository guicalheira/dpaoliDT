import cv2  # Biblioteca OpenCV para processamento de imagens
import pytesseract  # Biblioteca para OCR (Reconhecimento Óptico de Caracteres)
import re  # Biblioteca para trabalhar com expressões regulares
import numpy as np  # Biblioteca NumPy para manipulação de arrays
import os  # Biblioteca para operações com sistema de arquivos
from skimage.metrics import structural_similarity as ssim  # Para comparar similaridade de imagens

# Configuração do caminho do executável do Tesseract OCR (necessário no Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def extrair_dados_folha_ponto(caminho_imagem):
    """
    Função para extrair informações textuais da folha de ponto.
    Isso inclui:
    - Nome do colaborador
    - CPF
    - Horários registrados
    """
    # Carregar a imagem em escala de cinza para facilitar o processamento
    imagem = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)

    # Aplicar um threshold adaptativo para melhorar o contraste e facilitar a extração de texto
    _, imagem_bin = cv2.threshold(imagem, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Aplicar OCR para extrair texto da imagem processada
    texto = pytesseract.image_to_string(imagem_bin, lang="por")

    # Criar um dicionário para armazenar os dados extraídos
    dados = {
        "nome": None,  # Nome do colaborador
        "cpf": None,  # CPF do colaborador
        "horarios": [],  # Lista para armazenar os horários registrados
    }

    # Dividir o texto extraído em linhas para análise
    linhas = texto.split("\n")
    if linhas:
        dados["nome"] = linhas[0].strip()  # Assumimos que o nome está na primeira linha

    # Procurar um CPF no texto usando uma expressão regular
    match_cpf = re.search(r"\d{3}\.\d{3}\.\d{3}-\d{2}", texto)
    if match_cpf:
        dados["cpf"] = match_cpf.group()  # Se encontrado, armazenar o CPF

    # Encontrar todos os horários no formato HH:MM ou HH:MM:SS no texto
    horarios = re.findall(r"\b\d{2}:\d{2}(?::\d{2})?\b", texto)
    dados["horarios"].extend(horarios)  # Adicionar horários encontrados ao dicionário

    return dados  # Retorna o dicionário com as informações extraídas


def extrair_assinaturas(caminho_imagem):
    """
    Função para identificar e extrair as áreas da imagem que contêm assinaturas.
    """
    # Carregar a imagem em cores
    imagem = cv2.imread(caminho_imagem)
    # Converter a imagem para escala de cinza para facilitar a análise
    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicar um threshold para inverter as cores e destacar áreas escuras (assinaturas)
    _, imagem_bin = cv2.threshold(imagem_gray, 150, 255, cv2.THRESH_BINARY_INV)

    # Encontrar contornos na imagem binária (objetos de interesse, como assinaturas)
    contornos, _ = cv2.findContours(imagem_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    assinaturas = []  # Lista para armazenar as assinaturas extraídas

    # Iterar pelos contornos encontrados para filtrar as regiões que podem ser assinaturas
    for cnt in contornos:
        x, y, w, h = cv2.boundingRect(cnt)  # Obter coordenadas do retângulo delimitador
        if 50 < w < 300 and 20 < h < 100:  # Filtrar regiões baseando-se em tamanhos típicos de assinaturas
            assinatura = imagem_gray[y:y+h, x:x+w]  # Recortar a assinatura da imagem original
            assinaturas.append(assinatura)  # Adicionar a assinatura à lista

    return assinaturas  # Retorna a lista de imagens contendo assinaturas


def comparar_assinatura(assinatura1, assinatura2):
    """
    Compara duas assinaturas usando o Índice de Similaridade Estrutural (SSIM),
    que mede a semelhança entre duas imagens.
    """
    # Redimensionar as assinaturas para um tamanho padrão para permitir comparação justa
    assinatura1 = cv2.resize(assinatura1, (300, 100))
    assinatura2 = cv2.resize(assinatura2, (300, 100))

    # Calcular a similaridade estrutural entre as duas assinaturas
    score, _ = ssim(assinatura1, assinatura2, full=True)
    return score  # Retorna a similaridade como um valor entre 0 e 1 (1 = idêntico)


def verificar_assinaturas(caminho_folha, caminho_assinaturas_colaboradores):
    """
    Verifica se alguma das assinaturas presentes na folha de ponto
    corresponde às assinaturas cadastradas dos colaboradores.
    """
    # Extrair as assinaturas da folha de ponto
    assinaturas_folha = extrair_assinaturas(caminho_folha)
    
    # Percorrer os arquivos da pasta que contém as assinaturas registradas dos colaboradores
    for arquivo in os.listdir(caminho_assinaturas_colaboradores):
        if arquivo.endswith((".png", ".jpg", ".jpeg")):  # Garantir que seja uma imagem
            caminho_assinatura_colaborador = os.path.join(caminho_assinaturas_colaboradores, arquivo)
            assinatura_colaborador = cv2.imread(caminho_assinatura_colaborador, cv2.IMREAD_GRAYSCALE)

            # Comparar cada assinatura da folha com a assinatura do colaborador
            for assinatura_folha in assinaturas_folha:
                similaridade = comparar_assinatura(assinatura_folha, assinatura_colaborador)

                # Se a similaridade for maior que 70%, consideramos como uma assinatura válida
                if similaridade > 0.7:
                    return True, similaridade  # Assinatura válida encontrada

    return False, 0  # Nenhuma assinatura válida encontrada

# Caminho da folha de ponto e da pasta com assinaturas cadastradas
caminho_folha = "FOLHA_PONTO_02_-_2024_-_LUCAS_CASTRO_DOS_SANTOS.jpg"
caminho_pasta_colaboradores = "empresa/colaboradores/assinaturas/"

# Extrair informações textuais da folha de ponto
dados_folha = extrair_dados_folha_ponto(caminho_folha)
print("Dados extraídos:", dados_folha)

# Verificar se as assinaturas correspondem às cadastradas
assinatura_valida, confianca = verificar_assinaturas(caminho_folha, caminho_pasta_colaboradores)
print(f"Assinatura válida? {'Sim' if assinatura_valida else 'Não'} (Confiança: {confianca:.2f})")
