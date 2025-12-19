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


def refazer_ultimas_tarefas():
    try:
        dados = ler_arquivo()
        dados["desfazer_pilha"].append(dados["tarefas_atuais"].copy())
        dados["tarefas_atuais"].clear()
        dados["tarefas_atuais"] = dados["refazer_pilha"].copy()
        dados["refazer_pilha"].clear()
        alterar_arquivo(dados)
        return "Sucesso ao refazer a última alteração!"
    except Exception as e:
        return f"Não foi possível adicionar a tarefa. Erro: {e}"


def desfazer_ultima_tarefa():
    try:
        dados = ler_arquivo()
        # limpa a pilha de refazer
        dados["refazer_pilha"].clear()
        # atualiza a pilha de refazer com o estado atual das tarefas
        dados["refazer_pilha"] = dados["tarefas_atuais"].copy()

        # pegar a última adição que fizeram na lista de tarefas
        dados["tarefas_atuais"].clear()
        dados["tarefas_atuais"] = dados["desfazer_pilha"].pop()

        alterar_arquivo(dados)
        print("Desfiz a última alteração com sucesso!")
    except Exception as e:
        return f"Não foi possível adicionar a tarefa. Erro: {e}"


def adicionar_tarefa_no_arquivo(tarefa_content):
    try:
        dados = ler_arquivo()

        # limpa a pilha de refazer
        dados["refazer_pilha"].clear()

        dados["desfazer_pilha"].append(dados["tarefas_atuais"].copy())
        dados["tarefas_atuais"].append(tarefa_content)

        # atualiza o arquivo com os dados atualizados
        alterar_arquivo(dados)

        return "Tarefa foi adicionada com sucesso!"
    except Exception as e:
        return f"Não foi possível adicionar a tarefa. Erro: {e}"
