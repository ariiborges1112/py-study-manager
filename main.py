import os
from tarefa import Tarefa
from gerenciadorTarefas import GerenciadorTarefas

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibirMenu():
    print("\n==== GERENCIADOR DE TAREFAS ====\n")
    print("1. Adicionar nova tarefa")
    print("2. Listar todas as tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Excluir tarefa")
    print("5. Salvar e sair")

def simOuNao(mensagem: str) -> str:
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in ["sim", "nao"]:
            return resposta
        print("\nERRO! Resposta inválida! Digite apenas 'sim' ou 'nao'!!!")

if __name__ == "__main__":
    gerenciador = GerenciadorTarefas()
    gerenciador.carregarEmArquivo()

    while True:
        limparTela()
        exibirMenu()

        try:
            opcaoDoUsuario = int(input("Digite a opção desejada: "))
        except ValueError:
            print("\nERRO, não é permido letras ou caracteres especiais!!!")
            print("Por favor, digite um número de 1 a 5")
            continue

        match opcaoDoUsuario:
            case 1:
                print("\nDigite alguns dados sobre a tarefa que deseja adicionar")

                titulo = input("\nDigite o titulo da tarefa: ")
                descricao = input("\nDigite a descrição da tarefa: ")

                tarefa = Tarefa(titulo, descricao)
                gerenciador.adicionarTarefa(tarefa)

            case 2:
                print("Listando todas as tarefas...\n")
                gerenciador.listarTarefas()

            case 3:
                opc = simOuNao("\nDeseja conferir a lista de tarefas pendentes? [sim/nao]: ")
                if opc == "sim":
                    print()
                    gerenciador.listarTarefasNaoConcluidas()

                try:
                    indice = int(input("Qual tarefa deseja marcar como concluída? (de acordo com seu índice)\n"))
                except ValueError:
                    print("\nERRO, não é permido letras ou caracteres especiais!!!")
                    print("Por favor, digite apenas o número da tarefa")
                    continue

                tarefaRetornada = gerenciador.concluirTarefaViaIndice(indice - 1)
                if tarefaRetornada:
                    print(f"Tarefa {tarefaRetornada.titulo} marcada como concluída")

            case 4:
                opc = simOuNao("\nDeseja conferir a lista de tarefas pendentes? [sim/nao]: ")
                if opc == "sim":
                    gerenciador.listarTarefasNaoConcluidas()

                try:
                    indice = int(input("Qual tarefa deseja excluir? (de acordo com seu índice)\n"))
                except ValueError:
                    print("\nERRO, não é permido letras ou caracteres especiais!!!")
                    print("Por favor, digite apenas o número da tarefa")
                    continue

                tarefaRetornada = gerenciador.removerTarefa(indice - 1)

                if tarefaRetornada:
                    print(f"Tarefa {tarefaRetornada.titulo} foi removida com sucesso!")

            case 5:
                print("Salvando e saindo do programa...")
                gerenciador.salvarEmArquivo()
                break

            case _:
                print("ERRO! Só é permitidos números inteiros entre 1 a 5")
                print("Digite novamente!")