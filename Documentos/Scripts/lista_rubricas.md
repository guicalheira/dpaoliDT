# Captura de Rubricas no Domínio Folha

## Comportamento Esperado

1. **Localiza e clica** nos botões necessários para acessar a lista de rubricas.
2. **Aguarda a tela carregar** antes de prosseguir para evitar erros.
3. **Maximiza a janela** do sistema, caso não esteja maximizada.
4. **Captura screenshots** da lista de rubricas enquanto realiza a rolagem até o final.
5. **Salva os prints** em uma pasta específica chamada `rubrica`.
6. **Verifica automaticamente o fim da lista** para evitar capturas repetidas.

---

## Funções Principais

### `encontrar_e_clicar(imagem, confidence=0.7, timeout=10)`

* Procura a imagem na tela e clica nela.
* Retorna `True` se a imagem for encontrada e clicada, ou `False` se o tempo limite expirar.

### `maximizar_janela()`

* Conecta-se à janela do Domínio Folha.
* Maximiza a janela se ela não estiver maximizada.

### `capturar_lista_rubricas(img_canto_superior, img_canto_inferior, pasta_output="rubrica")`

* Localiza os limites da lista de rubricas.
* Captura screenshots da lista enquanto rola até o final.
* Salva as imagens na pasta `rubrica`.
* Para a captura ao detectar que a rolagem não está mais mudando a imagem.

### `aguardar_aparecer_e_executar(imagem_referencia)`

* Aguarda até que um elemento específico apareça na tela antes de prosseguir.
* Se a imagem não for encontrada dentro de 60 segundos, exibe um erro.

### `executar_automacao()`

* Controla a execução da automação.
* Executa todas as etapas na ordem correta:
  1. Clica para abrir a lista de rubricas.
  2. Aguarda carregamento.
  3. Clica para listar as rubricas.
  4. Aguarda e inicia a busca.
  5. Captura e salva as rubricas.

---

## Prevenção de Erros e Testes

* **Confirmação Visual** : As imagens usadas devem estar bem definidas para que a detecção funcione corretamente.
* **Ajuste de `confidence`** : Se a imagem não estiver sendo localizada, ajuste o parâmetro `confidence`.
* **Verificação de Tempo** : Os `timeout` evitam loops infinitos caso um elemento não seja encontrado.
* **Erros na Conexão da Janela** : Se o sistema Domínio Folha não estiver aberto, a automação falhará ao tentar conectar-se a ele.
* **Pasta de Saída** : O diretório de saída das imagens deve existir ou ser criado corretamente.

---
