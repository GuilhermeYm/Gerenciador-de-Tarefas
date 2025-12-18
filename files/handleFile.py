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
        print("Arquivo de salvamento encontrado!")


def abrir_arquivo():
    try:
        with open(CAMINHO_ARQUIVO, "r") as f:
            tarefa_content = json.load(f)
            return tarefa_content
    except json.JSONDecodeError:
        print("Ainda não há nenhuma tarefa salva no arquivo.")
        return False
    except FileNotFoundError:
        print(
            "Arquivo não foi encontrado, vou tentar resolver o problema. Caso, ele persista, por favor, entre em contato com o suporte"
        )
        verificar_arquivo()
        print("Vamos tentar novamente!")
        abrir_arquivo()


def carregar_tarefas():
    tentar_abrir_arquivo = abrir_arquivo()
    if tentar_abrir_arquivo:
        return tentar_abrir_arquivo
    return []

def adicionar_tarefa_no_arquivo(tarefa_content):
    try: 
        tarefas = carregar_tarefas()
        tarefas.append(tarefa_content)
        with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(tarefas, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(e)