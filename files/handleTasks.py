from os import name, system

from handleFile import carregar_tarefas

class Task:
    # Método para definir os atributos
    def __init__(self):
        self.tasks = []
        self.carregar_tarefas_na_classe()

    def carregar_tarefas_na_classe(self):
        tarefas_carregadas = carregar_tarefas()
        #self.tasks = tarefas_carregadas
    # Método de Instância
    def add_task(self, tarefa_content):
        self.tasks.append(tarefa_content)

    def listar(self):
        if len(self.tasks) == 0:
            print(
                "Você ainda não criou nenhuma tarefa. Se quiser adicionar uma, basta voltar e digitá-la"
            )
        else:
            system("cls" if name == "nt" else "clear")
            print("Lista de tarefas: ")
            # essa função vai criar tuplas com cada elemento da lista, e o índice dela
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

        input("Basta digitar qualquer tecla para sair")

    def desfazer(self): ...
    def refazer(self): ...
    def excluir(self): ...
