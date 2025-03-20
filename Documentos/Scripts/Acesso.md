Acesso:

(Para todas as etapas de acesso inicial, vai ter por via de regra, a determinação de um botão com a classe "SignOn-card-button-login" para click em continuar)

- abre navegador
- Inserir o endereço do dominio (https://www.dominioweb.com.br/)
- Determinar que a janela e dominio foi aberta com sucesso (Pesquisar pelo elemento de classe "bm-product-name")
- Script determinará por a existência do botão com seguinte class, SignOn-card-button-login, um botão de continuar
- Abrir inspetor de elementos fazer, seleciona a aba console, e no corpo da mesma escreve o comando para clickar no botão (forma de comandar click de botões sujeito a desenvolvimento) document.querySelector("#enterButton").click() e dar enter (comando de clique)
- Na janela seguite, o Script determina a existência de botão com o texto "continuar" e clica
- Indentificar um input de email name="username", inserir email guardado em arquivos definido na instalação do programa
  clickar no botão com o atributo type="submit"
- identificar campo com atributo name="password" inserir senha guardado em arquivos definido na instalação do programa
  clickar no botão com o atributo type="submit"
- condição caso exista verificação de duas etapas clicar no botão com o conteúdo "continuar depois"
- Deixar como requisito do software geral de agente a instalação do sistema Dominio

continuação com Caso1: Indentificar Janela de alerta (window.alert) com botão de "abrir" ()determinar pelo reconhecimento do texto)

- Script precisa esperar o inicio do programa até o momento em que indentifica o seguinte texto "seu computador está conectando ao Domínio Web" e a janela "App controller" aparece no sistema
- Script precisará indentificar a janela "lista de programas" e determinar a area de click pelo modulo e escolher uma das 3 primeiras opções Folha, Escrita Fiscal ou Contabilidade
- Para acesso script precisa clicar duas vezes no icone ou clicar e apertar enter
- Script precisa identifcar o surgimento de terceira janela com nome "Conectando..."
  (leitura da tela)

(testar cliques na tela para funcionamento e após isso integrar)

- Primeiro dado usuário script precisará buscar dado predeterminado na instalação nome de usuário para o agente

- Segundo dado senha script precisará buscar dado predeterminado na instalação senha para o agente

- clicar em ok

(testar cliques na janela sem nome do sistema Domínio que automaticamente aparece ao fundo da janela "lista de programas" para funcionamento e após isso integrar)

- identificar dominio e icone (tirar um print) clicar para ativar a janela

- finalizado

Extra(Pesquisar se existe uma abordagem melhor para abrir a janela)
