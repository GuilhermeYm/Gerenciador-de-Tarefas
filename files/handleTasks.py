from os import name, system
from time import sleep

from files.handleFile import (
    ler_arquivo,
    adicionar_tarefa_no_arquivo,
    desfazer_ultima_tarefa,
    arquivo_existe,
    refazer_ultimas_tarefas,
)


class Task:
    # Método para definir os atributos
    def __init__(self):
        # Atributos de instância

        self.tasks = None
        # Funções

        # Carregar ao iniciar o objeto
        self.carregar_tarefas_na_classe()

    def carregar_tarefas_na_classe(self):
        # Primeiro precisamos verificar a existênica do arquivo, e o seu conteúdo para depois ler.
        arquivo_existe()

        # Obter os dados do arquivo
        dados = ler_arquivo()
        self.tasks = dados["tarefas_atuais"] if len(dados["tarefas_atuais"]) > 0 else []

    # Método de Instância
    def adicionar_tarefa(self, tarefa_content):
        self.tasks.append(tarefa_content)
        atualizando_arquivoco_com_a_nova_tarefa = adicionar_tarefa_no_arquivo(
            tarefa_content
        )

        print(atualizando_arquivoco_com_a_nova_tarefa)

        sleep(1)
        self.listar()

    @staticmethod
    def verificar_tamanho_lista_tarefa(lista):
        if len(lista) == 0:
            return "Lista vazia."
        else:
            return len(lista)

    def listar(self):
        # Carregar novamente para garantir que os dados estão atualizados
        self.carregar_tarefas_na_classe()

        if len(self.tasks) == 0:
            print(
                "Você ainda não criou nenhuma tarefa. Se quiser adicionar uma, basta voltar e digitá-la"
            )
        else:
            system("clear" if name == "posix" else "cls")
            print("Lista de tarefas: ")

            # essa função vai criar tuplas com cada elemento da lista, e o índice dela
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

        input("Basta digitar qualquer tecla para sair")

    def desfazer(self):
        desfazer_alteracao = desfazer_ultima_tarefa()
        print(desfazer_alteracao)

    def refazer(self):
        refazer_alteracao = refazer_ultimas_tarefas()
        print(refazer_alteracao)

    def excluir(self): ...
