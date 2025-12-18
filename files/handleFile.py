import json
from pathlib import Path

NOME_ARQUIVO = "data.json"
CAMINHO_ARQUIVO = Path(__file__).resolve().parent / NOME_ARQUIVO


def verificar_arquivo():
    if not CAMINHO_ARQUIVO.exists():
        print(
            f"O arquivo onde salvamos as tarefas não existia, então eu tive que criá-lo.\n{CAMINHO_ARQUIVO}"
        )
        CAMINHO_ARQUIVO.touch()
    else:
        print("Arquivo de salvamente encontrado!")


def carregar_tarefas():
    try:
        with open(CAMINHO_ARQUIVO, "r") as f:
            file_content = json.load(f)
            print(file_content)
    except FileNotFoundError:
        print(
            "Arquivo não foi encontrado, vou tentar resolver o problema. Caso, ele persista, por favor, entre em contato com o suporte"
        )
        verificar_arquivo()
        print("Vamos tentar novamente!")
        carregar_tarefas()
