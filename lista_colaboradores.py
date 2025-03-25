import time
import pyautogui
import os
from pywinauto import Application
from PIL import ImageGrab

def encontrar_e_clicar(imagem, confidence=0.7, timeout=10):
    """Localiza um botão pela imagem e clica nele."""
    inicio = time.time()
    while time.time() - inicio < timeout:
        posicao = pyautogui.locateCenterOnScreen(imagem, confidence=confidence)
        if posicao:
            pyautogui.click(posicao)
            print("Clicado com sucesso!")
            return True
        time.sleep(1)
    print("Não encontrado!")
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

def capturar_lista_listagem(img_canto_superior, img_canto_inferior, pasta_output="colaboradores"):
    """Captura prints da lista de listagem e salva em uma pasta, rolando até o final."""
    time.sleep(2)
    os.makedirs(pasta_output, exist_ok=True)
    
    # Localizar os cantos da área de captura
    canto_superior = pyautogui.locateCenterOnScreen(img_canto_superior, confidence=0.8)
    canto_inferior = pyautogui.locateCenterOnScreen(img_canto_inferior, confidence=0.8)
    
    if not canto_superior or not canto_inferior:
        print("Erro: Não foi possível localizar um dos cantos.")
        return None
    
    x1, y1 = canto_superior
    x2, y2 = canto_inferior
    x1, x2 = min(x1, x2), max(x1, x2) + 50  # Expandindo para direita para capturar a barra de rolagem
    y1, y2 = min(y1, y2), max(y1, y2)
    y1 += 10
    
    ultima_imagem = None
    contador = 0
    while True:
        captura = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        
        if ultima_imagem and captura.tobytes() == ultima_imagem.tobytes():
            print("Fim da lista detectado pela repetição da imagem!")
            break
        
        imagem_path = os.path.join(pasta_output, f"colaboradores_{contador}.png")
        captura.save(imagem_path)
        print(f"Captura salva: {imagem_path}")
        
        ultima_imagem = captura
        contador += 1
        pyautogui.press("pagedown")
        time.sleep(2)

def aguardar_aparecer_e_executar(imagem_referencia):
    print("Aguardando a abertura da tela desejada...")
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
    encontrar_e_clicar("imagens_Lista_Colaboradores/botao_empregados.png")
    aguardar_aparecer_e_executar("imagens_Lista_Colaboradores/listagem.png")
    encontrar_e_clicar("imagens_Lista_Colaboradores/listagem.png", 0.8)
    
    #maximizar_janela()
    aguardar_aparecer_e_executar("imagens_Lista_Colaboradores/image.png")
    encontrar_e_clicar("imagens_Lista_Colaboradores/botao_buscar.png", 0.8)
    time.sleep(2)
    
    capturar_lista_listagem("imagens_Lista_Colaboradores/canto_coluna_codigo.png", 
                             "imagens_Lista_Colaboradores/canto_coluna_setinha_rolagem.png")
    
if __name__ == "__main__":
    executar_automacao()