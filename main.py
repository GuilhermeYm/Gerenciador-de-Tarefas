from os import name, system
from time import sleep

from files.handleFile import verificar_arquivo
from files.handleTasks import Task

tarefas_usuarios = Task()


def cmd_limpar():
    print("Limpando em três segundos...")
    sleep(3)
    system("clear" if name == "posix" else "cls")


def cmd_sair():
    print("Saindo do aplicativo em três segundos....")
    sleep(3)
    exit()


def cmd_ajuda(): ...


commandsTask = {
    "listar": tarefas_usuarios.listar,
    "desfazer": tarefas_usuarios.desfazer,
    "refazer": tarefas_usuarios.refazer,
    "excluir": tarefas_usuarios.excluir,
}
commandsSystem = {"limpar": cmd_limpar, "sair": cmd_sair, "ajuda": cmd_ajuda}

# o Pipe no Python e no contexto de dicionário significa juntar
commands_zipped = commandsTask | commandsSystem

def ver_comandos():
    for command in commands_zipped:
        print(f"- {command}")
        
def saudacao():
    verificar_arquivo()
    print('Iniciando a aplicação....')
    cmd_limpar()
    print(f"{'#' * 50}")
    print("Olá! Seja bem vindo a um simples gerenciador de tarefas pelo terminal!")
    print()
    sleep(2)
    print(
        "A seguir te mostrarei os comandos que nós temos e que serão muito importante para você!"
    )
    print(f"{'#' * 50}")
    sleep(1)

saudacao()

while True:
    ver_comandos()
    print(f"{'#' * 50}")
    user_answer = input(
        "Digite um comando ou apenas a tarefa que você deseja adicionar > "
    )
    
    if user_answer in commands_zipped.keys():
        commands_zipped[user_answer]()
    else:
        tarefas_usuarios.adicionar_tarefa(user_answer)
