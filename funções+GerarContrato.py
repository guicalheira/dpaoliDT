import json
import os

def solicitar_dados_cliente():
    """Solicita manualmente os dados de um cliente caso não sejam encontrados."""
    return {
        "NOME_CLIENTE": input("Informe o nome do cliente: "),
        "CNPJ": input("Informe o CNPJ: "),
        "ENDERECO": input("Informe o endereço: "),
        "TELEFONE": input("Informe o telefone: ")
    }

def encontrar_pasta_cliente(base_dir: str, nome_cliente: str) -> str:
    """Retorna o caminho da pasta do cliente dentro do diretório base do escritório."""
    caminho_cliente = os.path.join(base_dir, nome_cliente)
    if os.path.exists(caminho_cliente) and os.path.isdir(caminho_cliente):
        return caminho_cliente
    raise FileNotFoundError(f"Pasta do cliente '{nome_cliente}' não encontrada em '{base_dir}'")

def achar_colaborador(pasta_cliente: str, nome_colaborador: str) -> str:
    """Retorna o caminho da pasta de um colaborador específico dentro da pasta do cliente."""
    colaboradores_dir = os.path.join(pasta_cliente, "colaboradores", nome_colaborador)
    if os.path.exists(colaboradores_dir) and os.path.isdir(colaboradores_dir):
        return colaboradores_dir
    raise FileNotFoundError(f"Colaborador '{nome_colaborador}' não encontrado para o cliente '{pasta_cliente}'")

def ler_dados_cliente(pasta_cliente: str) -> dict:
    """Lê o arquivo DADOS.TXT dentro da pasta do cliente."""
    caminho_arquivo = os.path.join(pasta_cliente, "DADOS.TXT")
    if not os.path.exists(caminho_arquivo):
        return solicitar_dados_cliente()
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def gerar_contrato(cliente, colaborador, template_path="contrato_template.txt", output_path="contrato_gerado.txt"):
    """Gera um contrato preenchendo os dados do cliente e do colaborador no template e salva o resultado."""
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template {template_path} não encontrado.")
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    
    dados_completos = {**cliente, **colaborador}
    for chave, valor in dados_completos.items():
        template = template.replace(f"{{{{{chave}}}}}", valor)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(template)
    print(f"Contrato salvo em {output_path}")

def main():
    base_dir = "clientes"
    nome_cliente = input("Digite o nome do cliente: ")
    try:
        pasta_cliente = encontrar_pasta_cliente(base_dir, nome_cliente)
        cliente = ler_dados_cliente(pasta_cliente)
        nome_colaborador = input("Digite o nome do colaborador: ")
        colaborador_dir = achar_colaborador(pasta_cliente, nome_colaborador)
        print(f"Cliente: {cliente}")
        print(f"Colaborador encontrado em: {colaborador_dir}")
    except FileNotFoundError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
