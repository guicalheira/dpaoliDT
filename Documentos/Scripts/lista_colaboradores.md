# Lista Colaboradores

## Comportamento Esperado

1. **Localização e Clique em Elementos:** O script busca elementos na tela por meio de imagens de referência e realiza cliques automáticos.
2. **Maximização da Janela:** Garante que a janela do sistema esteja maximizada para evitar erros de captura de tela.
3. **Captura de Listagem:** Realiza capturas de tela rolando a página até o final da lista.
4. **Aguarda Elementos:** Espera até que a interface seja carregada antes de prosseguir.

## Funções Principais

### `<span>encontrar_e_clicar(imagem, confidence=0.7, timeout=10)</span>`

* Localiza um elemento na tela e clica nele.
* Tenta localizar a imagem por um tempo definido pelo `<span>timeout</span>`.
* Retorna `<span>True</span>` se a imagem foi encontrada e clicada, `<span>False</span>` caso contrário.

### `<span>maximizar_janela()</span>`

* Conecta-se à janela do sistema Domínio Folha e a maximiza se necessário.

### `<span>capturar_lista_listagem(img_canto_superior, img_canto_inferior, pasta_output="colaboradores")</span>`

* Captura imagens da listagem e salva na pasta `<span>colaboradores</span>`.
* Rola a tela automaticamente até o fim da lista, comparando imagens consecutivas.

### `<span>aguardar_aparecer_e_executar(imagem_referencia)</span>`

* Aguarda até que um elemento de referência apareça na tela antes de prosseguir.

### `<span>executar_automacao()</span>`

* Executa a sequência completa da automação, incluindo:
  * Localizar e clicar nos botões.
  * Aguardar telas carregarem.
  * Capturar a listagem completa.

## Prevenção de Erros e Testes

* **Imagens de Referência:** As imagens usadas para reconhecimento devem ser claras e bem definidas.
* **Resolução da Tela:** O script pode falhar se a resolução do monitor for diferente da usada para capturar as imagens de referência.
* **Tempo de Carregamento:** Pode ser necessário ajustar `<span>time.sleep()</span>` para sistemas mais lentos.
* **Execução em Segundo Plano:** O sistema Domínio Folha deve estar em primeiro plano para que o script funcione corretamente.
