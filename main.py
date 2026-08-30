import os
import time
from tarefa import Tarefa
from gerenciadorTarefas import GerenciadorTarefas

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibirMenu():
    print("\n==== GERENCIADOR DE TAREFAS ====\n")
    print("1. Adicionar nova tarefa")
    print("2. Listar todas as tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Marcar tarefa como Pendente")
    print("5. Excluir tarefa")
    print("6. Salvar e sair")

def simOuNao(mensagem: str) -> str:
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in ["sim", "nao", "s", "n"]:
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
            print("\nERRO!!! Não é permido letras ou caracteres especiais!!!")
            print("Por favor, digite um número de 1 a 6")
            continue

        match opcaoDoUsuario:
            case 1:
                print("\nDigite alguns dados sobre a tarefa que deseja adicionar")

                titulo = input("\nDigite o titulo da tarefa: ")
                descricao = input("\nDigite a descrição da tarefa: ")

                tarefa = Tarefa(titulo, descricao)
                gerenciador.adicionarTarefa(tarefa)
                input("\nPressione Enter para continuar...")

            case 2:
                print("\nListando todas as tarefas...")
                gerenciador.listarTarefas()
                input("Pressione Enter para continuar...")
                
            case 3:
                opc = simOuNao("\nDeseja conferir a lista de tarefas pendentes? [sim/nao]: ")
                if opc in ["sim", "s"]:
                    gerenciador.listarTarefasNaoConcluidas()
                else:
                    print()

                try:
                    indice = int(input("Qual tarefa deseja marcar como CONCLUÍDA? [de acordo com seu ID]: "))
                except ValueError:
                    print("\nERRO!!! Não é permido letras ou caracteres especiais!!!")
                    print("Por favor, digite apenas o número da tarefa")
                    input("\nPressione Enter para continuar...")                    
                    continue

                tarefaRetornada = gerenciador.concluirTarefaViaIndice(indice - 1)

                if tarefaRetornada:
                    print(f"\nA tarefa {tarefaRetornada.titulo} foi marcada como concluída")

                input("\nPressione Enter para continuar...")

            case 4:
                opc = simOuNao("\nDeseja conferir a lista de tarefas concluídas? [sim/nao]: ")
                if opc in ["sim", "s"]:
                    gerenciador.listarTarefasConcluidas()
                else:
                    print()

                try:
                    indice = int(input("Qual tarefa deseja DESMARCAR (tornar pendente)? [de acordo com seu ID]: "))
                except ValueError:
                    print("\nERRO!!! Não é permido letras ou caracteres especiais!!!")
                    print("Por favor, digite apenas o número da tarefa")
                    input("\nPressione Enter para continuar...")                    
                    continue

                tarefaRetornada = gerenciador.desmarcarTarefaViaIndice(indice - 1)

                if tarefaRetornada:
                    print(f"\nA tarefa {tarefaRetornada.titulo} voltou a ficar pendente!")

                input("\nPressione Enter para continuar...")                

            case 5:
                opc = simOuNao("\nDeseja conferir a lista completa de tarefas? [sim/nao]: ")
                if opc in ["sim", "s"]:
                    gerenciador.listarTarefas()
                else:
                    print()

                print("O que deseja excluir?")
                print("1. Apenas  uma tarefa específica (por ID)")
                print("2. Todas as tarefas já CONCLUÍDAS")

                try:
                    escolhaExclusao = int(input("Escolha a opção desejada [1 ou 2]: "))
                except ValueError:
                    print("\nERRO!!! Digite apenas 1 ou 2!")
                    input("\nPressione Enter para continuar...")
                    continue

                if escolhaExclusao == 1:
                    try:
                        indice = int(input("\nQual tarefa deseja excluir? [de acordo com seu índice]: "))
                    except ValueError:
                        print("\nERRO!!! Não é permido letras ou caracteres especiais!!!")
                        print("Por favor, digite apenas o número da tarefa")
                        input("\nPressione Enter para continuar...")
                        continue

                    tarefaRetornada = gerenciador.removerTarefa(indice - 1)

                    if tarefaRetornada:
                        print(f"\nA Tarefa {tarefaRetornada.titulo} foi removida com sucesso!")

                elif escolhaExclusao == 2:
                    removidas = gerenciador.removerTarefasConcluidas()

                    if removidas > 0:
                        print(f"\nSucesso! {removidas} tarefa(s) concluída(s) removida(s)")
                    else:
                        print(f"\nNão há tarefas concluídas para remover")

                else:
                    print("\nERRO!!! Opção inválida!")

                input("\nPressione Enter para continuar...")

            case 6:
                print("\nSalvando e saindo do programa...")
                gerenciador.salvarEmArquivo()
                time.sleep(2)
                break

            case _:
                print("ERRO! Só é permitido números inteiros entre 1 a 6")
                print("Digite novamente!")