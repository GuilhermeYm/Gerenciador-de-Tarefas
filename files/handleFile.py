import json
from pathlib import Path

NOME_ARQUIVO = "data.json"
CAMINHO_ARQUIVO = Path(__file__).resolve().parent / NOME_ARQUIVO


def alterar_arquivo(dados):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)


def ler_arquivo():
    try:
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
            dados = json.load(f)
            return dados
    except json.JSONDecodeError:
        return []


def arquivo_existe():
    if not CAMINHO_ARQUIVO.exists():
        print(
            f"O arquivo onde salvamos as tarefas não existia, então eu tive que criá-lo.\n{CAMINHO_ARQUIVO}"
        )
        try:
            # crio o arquivo
            CAMINHO_ARQUIVO.touch()

            # coloca no arquivo os dados iniciais -> são necessários para o aplicativo funcionar

            dados_iniciais = {
                "tarefas_atuais": [],
                "desfazer_pilha": [],
                "refazer_pilha": [],
            }
            alterar_arquivo(dados_iniciais)
        except Exception as e:
            print(f"Não foi possível criar o arquivo. Erro: {e}")


def desfazer_ultima_tarefa():
    try:
        dados = ler_arquivo()
        ultima_alteracao = dados["desfazer_pilha"].pop()

        # atualizar a redo stack
        dados["refazer_pilha"].clear()
        dados["refazer_pilha"] = dados["tarefas_atuais"].copy()

        # arrumar  agora as tarefas
        dados["tarefas_atuais"].clear()
        dados["tarefas_atuais"] = ultima_alteracao
        alterar_arquivo(dados)
        print("Desfiz a última alteração com sucesso!")
    except:
        ...


def adicionar_tarefa_no_arquivo(tarefa_content):
    try:
        tarefas = ler_arquivo()
        tarefas["desfazer_pilha"].append(tarefas["tarefas_atuais"].copy())
        tarefas["tarefas_atuais"].append(tarefa_content)
        alterar_arquivo(tarefas)
    except Exception as e:
        print(e)
