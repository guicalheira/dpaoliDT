from playwright.sync_api import sync_playwright
import time
import pyautogui
import subprocess
from pywinauto import Application

def acessar_dominio():
    with sync_playwright() as p:
        # Abrir navegador
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Acessar site
        page.goto("https://www.dominioweb.com.br/")
        
        # Verificar carregamento da página
        if not page.locator(".bm-product-name").is_visible(timeout=10000):
            print("Erro ao carregar a página.")
            return
        
        # Clicar no botão de login
        page.locator(".SignOn-card-button-login").click()
        time.sleep(2)
        
        # Inserir email e senha
        page.fill("input[name='username']", "icaroglaucooliveira@gmail.com")
        page.press("input[name='username']", "Enter")
        time.sleep(1)
        
        page.fill("input[name='password']", "qU7,6HbH.wHn7-U")
        page.press("input[name='password']", "Enter")
        time.sleep(2)

        # Esperar e clicar no botão para abrir o sistema
        botao = None
        tempo_espera = 15  # Tempo máximo para encontrar o botão
        inicio = time.time()
        
        while time.time() - inicio < tempo_espera:
            try:
                botao = pyautogui.locateCenterOnScreen("imagens_Acesso/abrir_botao.png", confidence=0.8)
                if botao:
                    pyautogui.click(botao)
                    print("Botão clicado com sucesso!")
                    break
            except:
                pass  # Ignora qualquer erro caso o botão não seja encontrado

            time.sleep(1)
        
        # Verificação de dois fatores
        if page.locator("text=Continuar depois").is_visible(timeout=5000):
            page.locator("text=Continuar depois").click()
            print("Autenticação de dois fatores ignorada.")
        
        print("Login concluído!")

def interagir_sistema():
    print("Aguardando a janela do Domínio Web...")
    
    posicao = False
    while not posicao:
        imagem_janela = "imagens_Acesso/imagem_janela.png"  # Substitua pelo caminho correto da sua imagem
        try:
            posicao = pyautogui.locateCenterOnScreen(imagem_janela, confidence=0.8)
        except:
            print("Procurando janela...")
        time.sleep(2)
    
    # Simular cliques manuais na interface
    print("Interagindo manualmente com a interface...")
    pyautogui.click(posicao)  # Clique na janela para ativá-la
    time.sleep(2)
    
    # Verificar se algum dos três módulos desejados está visível e clicar
    modulos = {
        "Folha": "imagens_Acesso/folha.png",
        "Escrita Fiscal": "imagens_Acesso/escrita_fiscal.png",
        "Contabilidade": "imagens_Acesso/contabilidade.png"
    }
    
    for nome, imagem in modulos.items():
        posicao_modulo = pyautogui.locateCenterOnScreen(imagem, confidence=0.8)
        if posicao_modulo:
            print(f"Clicando no módulo {nome}...")
            pyautogui.doubleClick(posicao_modulo)
            time.sleep(5)
            break
    else:
        print("Nenhum módulo encontrado!")
    
    
    # Aguardar e inserir credenciais
    print("Aguardando conexão...")
    time.sleep(5)  # Ajuste conforme necessário
    print("Inserindo credenciais...")
    pyautogui.write("DPACIOLI")
    pyautogui.press("tab")
    pyautogui.write("dpacioli2025")
    pyautogui.press("enter")
    
    print("Acesso concluído!")
    
def aguardar_e_executar_lista_rubrica():
    print("Aguardando a abertura da tela desejada...")

    imagem_referencia = "imagens_Acesso/imagem_dominioFolha.png"  # Ajuste para o caminho correto da imagem de referência
    tempo_espera = 60  # Tempo máximo de espera em segundos
    inicio = time.time()

    while time.time() - inicio < tempo_espera:
        try:
            if pyautogui.locateCenterOnScreen(imagem_referencia, confidence=0.8):
                print("Tela encontrada! Executando script lista_rubrica.py...")
                subprocess.run(["python", "lista_rubrica.py"])
                return
        except:
            pass  # Continua tentando encontrar a imagem
        
        time.sleep(2)

    print("Tempo esgotado! A tela não foi encontrada.")
    

# Executar funções
acessar_dominio()
time.sleep(10)
interagir_sistema()
aguardar_e_executar_lista_rubrica()