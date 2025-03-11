import cv2
import pytesseract
import re
import numpy as np
from PIL import Image

# Defina o caminho do executável do Tesseract (somente para Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def extrair_dados_folha_ponto(caminho_imagem):
    """
    Extrai informações relevantes da folha de ponto a partir da imagem,
    incluindo nome, CPF, horários e validação dos dados.
    """
    # Carregar a imagem em escala de cinza
    imagem = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
    
    # Aplicar filtro de binarização para remover ruídos
    _, imagem = cv2.threshold(imagem, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Extrair texto usando o Tesseract OCR
    texto = pytesseract.image_to_string(imagem, lang="por")
    
    dados = {
        "nome": None,
        "cpf": None,
        "horarios": [],
        "faltas": 0
    }
    
    # Procurar por nome (suposição: primeira linha ou começo do documento)
    linhas = texto.split('\n')
    if linhas:
        dados["nome"] = linhas[0].strip()
    
    # Procurar CPF
    match_cpf = re.search(r"\d{3}\.\d{3}\.\d{3}-\d{2}", texto)
    if match_cpf:
        dados["cpf"] = match_cpf.group()
    
    # Procurar horários (formato HH:MM ou HH:MM:SS)
    horarios = re.findall(r"\b\d{2}:\d{2}(?::\d{2})?\b", texto)
    dados["horarios"].extend(horarios)
    
    # Contar possíveis faltas (supondo que cada dia tenha entrada e saída)
    dias_trabalhados = len(set(horarios)) // 2  # Considerando entrada e saída
    dias_totais = 30  # Supondo um mês
    dados["faltas"] = max(0, dias_totais - dias_trabalhados)
    
    # Validação dos critérios
    criterios = {
        "nome_presente": bool(dados["nome"]),
        "cpf_presente": bool(dados["cpf"]),
        "horarios_minimos": len(dados["horarios"]) > 10,  # Supondo ao menos 5 dias registrados
        "faltas_excessivas": dados["faltas"] < 10  # Máximo de 10 faltas aceitáveis
    }
    
    folha_valida = all(criterios.values())
    
    return dados, folha_valida, criterios

# Caminho da imagem da folha de ponto
caminho_imagem = "folha_ponto.jpg"

# Extração e validação
dados_extraidos, valido, detalhes_validacao = extrair_dados_folha_ponto(caminho_imagem)

# Exibir os dados extraídos e validação
print("Dados extraídos:", dados_extraidos)
print("Folha de ponto válida?", "Sim" if valido else "Não")
print("Detalhes da validação:", detalhes_validacao)
