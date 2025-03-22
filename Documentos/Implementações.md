            Roadmap de Implementações
========================================================
## Base
Instalador:
    - Instalação do executor de modelo
    - Configurador dos scripts
    - Personalizações:
        Registro de rúbricas personalizadas na instalação 


## Construções de segundo nível
Instruir a IA para rotinas com lançamentos como serviços de manuntenção em ações na janela de periódicos:
    Folha mensal, 13º integral e adiantado

Criar subrotina integrada de Monitoramento e leitura de integração com o eSocial pelo Painel de pendências do eSocial nos scripts:
    Esses eventos podem ser demorados, mas são programados em persistir o procedimento
    
Criar sistema de análise de logs pré-atividades para determinação de incoerências


## Objetivos pra Sábado 22 de março:

Criar interface de determinações:

        - Para cada atividade conhecida listada ao modelo, fazer pergunta de confirmação da clareza da atividade incluindo localizações para arquivos modelo para as atividades
        e salvar na pasta da instação do software
        

Dar uma interface acompanhamento:
    - wrapper de IO para execução de funções e dar na side inter de acompanhamento

        
        Esquematizar Objeto: CONTEXTO (instância de execução)
            Status de sucesso
            Pipeline de execução com campos de retorno
        
        Instruções para utilização do contexto
        
        . Criar loop de interação com chamada de funções
        - Testar isso na tarefa: gerar contrato de admissão para empresa tal, funcionário tal
                
                Passos e parâmetros esperados da inferência da inteligência (específico de caso de contrato de admissão):
                    - Identificar dados:
                        (específico de caso de contrato de admissão)
                        - Cargo
                        - Salário
                        - Regime
                        
                    - Identificar Empresa X e Funcionário Y
                    
                    - Determinar arquivos que existem para essas entidades:
                        (específico de caso de contrato de admissão)
                        - Básicos da empresa (DADOS.txt)
                        - Básicos do funcionário:
                            - Identificação
                            - Exame admissional
                            - Comprovante de Endereço
                            
                    anexar a pipeline:
                        [ler_pasta_clientes, ler_pasta_comuns_determinadas_na_instalacao]
                        
                    > Retornar saída para o sistema externo
                    
                    < Receber nova entrada, com objeto de contexto contendo resultado das funções na pipeline
                    
                    - Determinar arquivos na lista que podem conter os dados necessários para solicitação
                    
                    anexar a pipeline
                        [consultar_dados_em_arquivos(entidade_relacionada, [arquivos], [dados])...]
                    
                    - Determinar os dados faltantes para solicitação
                    
                    - Solicitar ao usuário dados ou localização dos mesmos referindo para quais entidades da solicitação se cabível
                    
                    - Inferir se usuário apontou localização ou forneceu os dados
                    
                    || Se sim (apontou localização):
                        - Montar caminho para arquivos
                        anexar a pipeline:
                            [consultar_dados_em_arquivos(entidade_relacionada, [arquivos], [dados])]
                            
                        > Retornar saída para o sistema externo
                        
                        < Receber nova entrada, com objeto de contexto contendo resultado das funções na pipeline
                        
                    || Se não (forneceu diretamente os dados)
                    
                    anexar a pipeline
                        ler_template_lista_templates
                        
