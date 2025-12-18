from os import name, system

from files.handleFile import carregar_tarefas, adicionar_tarefa_no_arquivo


class Task:
    # Método para definir os atributos
    def __init__(self):
        self.tasks = []
        self.carregar_tarefas_na_classe()
        self.undo_stack = []
        self.redo_stack = []
        
    def carregar_tarefas_na_classe(self):
        tarefas_carregadas = carregar_tarefas()
        self.tasks = tarefas_carregadas

    # Método de Instância
    def adicionar_tarefa(self, tarefa_content):
        self.tasks.append(tarefa_content)
        adicionar_tarefa_no_arquivo(self.tasks)
        
    @staticmethod
    def verificar_tamanho_lista_tarefa(lista):
        if len(lista) == 0:
            return "Lista vazia."
        else:
            return len(lista)

    def listar(self):
        self.carregar_tarefas_na_classe()
        if len(self.tasks) == 0:
            print(
                "Você ainda não criou nenhuma tarefa. Se quiser adicionar uma, basta voltar e digitá-la"
            )
        else:
            system("cls" if name == "nt" else "clear")
            print("Lista de tarefas: ")
            verificar_tamanho_lista_tarefa = self.verificar_tamanho_lista_tarefa(self.tasks)
            if isinstance(verificar_tamanho_lista_tarefa, str):
                return verificar_tamanho_lista_tarefa
            # essa função vai criar tuplas com cada elemento da lista, e o índice dela
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

        input("Basta digitar qualquer tecla para sair")

    def desfazer(self): ...
    def refazer(self): ...
    def excluir(self): ...
