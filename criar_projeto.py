# InvesJota-Hub-Financeiro
import os

def criar_estrutura_invesjota():
    """Cria a estrutura de pastas e arquivos para o projeto InvesJota."""
    
    # 1. Definição da Estrutura
    estrutura_base = {
        "HubFinanceiro": {
            "InvesJota": {
                "assets": {
                    "css": [
                        "invesjota_base.css"  # Estilo Vintage
                    ],
                    "js": [
                        "logica_calculadoras.js"
                    ]
                },
                "html": [
                    "catalogo_calculadoras.html",
                    "juros_compostos.html",
                    "noticias.html",
                    "home.html"
                ],
            },
            "CalculaTudoFacil": {
                "assets": {
                    "css": [
                        "calculatudo_base.css"  # Estilo Clean
                    ]
                },
                "html": [
                    "juros_simples_mvp.html"
                ]
            },
            "Imagens": [] # Pasta vazia para logos
        }
    }

    def criar_recursivo(base_path, estrutura):
        for nome, conteudo in estrutura.items():
            caminho_completo = os.path.join(base_path, nome)
            
            if isinstance(conteudo, dict):
                # Se for um dicionário, cria a pasta e chama recursivamente
                print(f"Criando diretório: {caminho_completo}")
                os.makedirs(caminho_completo, exist_ok=True)
                criar_recursivo(caminho_completo, conteudo)
            
            elif isinstance(conteudo, list):
                # Se for uma lista (arquivos), cria os arquivos
                if nome == "html":
                    # Trata arquivos HTML na raiz da pasta
                    caminho_arquivos = base_path 
                else:
                    # Trata arquivos CSS/JS em subpastas
                    caminho_arquivos = os.path.join(base_path, nome)
                    os.makedirs(caminho_arquivos, exist_ok=True)

                for arquivo in conteudo:
                    caminho_arquivo = os.path.join(caminho_arquivos, arquivo)
                    print(f"Criando arquivo: {caminho_arquivo}")
                    # Cria um arquivo vazio. Use 'w' para sobrescrever se já existir.
                    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                        # Adiciona um comentário simples para identificar o arquivo
                        if arquivo.endswith('.html'):
                            f.write(f"\n")
                        elif arquivo.endswith('.css'):
                            f.write(f"/* Arquivo de estilo para {nome} */\n")
                        elif arquivo.endswith('.js'):
                            f.write(f"// Arquivo de lógica para {nome} \n")

    # Inicia a criação na pasta atual
    if "HubFinanceiro" in estrutura_base:
        criar_recursivo(os.getcwd(), estrutura_base)
    
    print("\n✅ Estrutura do projeto 'HubFinanceiro' criada com sucesso!")


if __name__ == "__main__":
    criar_estrutura_invesjota()