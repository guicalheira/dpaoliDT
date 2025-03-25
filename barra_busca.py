import pyautogui
import time
import pytesseract
from PIL import ImageGrab

# Caminhos das imagens
logo_path = "barra_busca/dominioIcone.png"
search_bar_path = "barra_busca/barra_busca.png"

# Tempo limite para encontrar os elementos
timeout = 120  

# Caminho do Tesseract OCR (ajuste conforme necessário)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Solicita ao usuário o termo de pesquisa
termo_pesquisa = input("Digite o termo a ser pesquisado: ")

# Função para localizar e clicar em um elemento na tela
def clicar_imagem(imagem, descricao):
    start_time = time.time()
    while time.time() - start_time < timeout:
        posicao = pyautogui.locateCenterOnScreen(imagem, confidence=0.8)
        if posicao:
            pyautogui.click(posicao)
            print(f"{descricao} encontrado e clicado!")
            return True
        time.sleep(1)
    print(f"Tempo limite atingido! {descricao} não encontrado.")
    return False

# Função para encontrar e clicar no resultado da busca
def encontrar_e_clicar_resultado(termo_pesquisa):
    start_time = time.time()
    while time.time() - start_time < timeout:
        screenshot = ImageGrab.grab()  # Captura a tela
        text_data = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)

        for i, word in enumerate(text_data["text"]):
            if termo_pesquisa.lower() in word.lower():  # Verifica se o termo está no texto
                x, y, w, h = text_data["left"][i], text_data["top"][i], text_data["width"][i], text_data["height"][i]
                center_x, center_y = x + w // 2, y + h // 2
                pyautogui.click(center_x, center_y)
                print(f"Resultado '{word}' encontrado e clicado!")
                return True

        time.sleep(1)  # Aguarda antes da próxima verificação

    print("Tempo limite atingido! Nenhum resultado correspondente encontrado.")
    return False

# Executa os passos
if clicar_imagem(logo_path, "Logo DOMÍNIO"):
    if clicar_imagem(search_bar_path, "Barra de pesquisa"):
        time.sleep(1)  # Pequeno delay para garantir que o cursor esteja ativo
        pyautogui.write(termo_pesquisa)
        pyautogui.press("enter")
        print("Pesquisa realizada com sucesso!")
        
        # Tenta encontrar e clicar no resultado
        encontrar_e_clicar_resultado(termo_pesquisa)
