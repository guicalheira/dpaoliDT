# Automatização de Buscar

## Visão Geral

Este script automatiza a pesquisa e interação com a interface do sistema Domínio Folha. Ele localiza elementos gráficos por imagem, insere um termo de pesquisa e identifica resultados usando OCR para clique automático.

## Dependências

* Python
* PyAutoGUI
* PyTesseract
* Pillow
* Time

## Comportamento Esperado

1. **Localização e Clique em Elementos:** O script busca elementos na tela por meio de imagens de referência e realiza cliques automáticos.
2. **Pesquisa de Termo:** O usuário insere um termo de busca, que é digitado automaticamente no campo de pesquisa.
3. **Reconhecimento de Texto via OCR:** O script captura a tela, analisa o texto com OCR e clica no resultado correspondente.
4. **Aguarda Elementos:** Espera até que a interface seja carregada antes de prosseguir.

## Funções Principais

### `<span>clicar_imagem(imagem, descricao)</span>`

* Localiza um elemento na tela por meio de uma imagem de referência e clica nele.
* Aguarda até `<span>timeout</span>` segundos para encontrar o elemento.
* Retorna `<span>True</span>` se a imagem foi encontrada e clicada, `<span>False</span>` caso contrário.

### `<span>encontrar_e_clicar_resultado(termo_pesquisa)</span>`

* Captura a tela e utiliza OCR para localizar o termo pesquisado.
* Se encontrar um termo correspondente, clica no centro do texto identificado.
* Retorna `<span>True</span>` se encontrou e clicou, `<span>False</span>` caso contrário.

### `<span>executar_automacao()</span>`

* Executa a sequência completa da automação:
  * Localiza e clica na logo do sistema.
  * Acessa a barra de pesquisa.
  * Digita o termo de busca e pressiona Enter.
  * Utiliza OCR para encontrar o resultado e clicar nele.

## Prevenção de Erros e Testes

* **Imagens de Referência:** As imagens usadas para reconhecimento devem ser bem definidas.
* **Resolução da Tela:** O script pode falhar se a resolução do monitor for diferente da usada para capturar as imagens de referência.
* **Tempo de Carregamento:** Pode ser necessário ajustar `<span>time.sleep()</span>` para sistemas mais lentos.
* **Execução em Segundo Plano:** O sistema Domínio Folha deve estar em primeiro plano para que o script funcione corretamente.
