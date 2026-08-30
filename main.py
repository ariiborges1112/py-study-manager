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

if __name__ == "__main__":
    gerenciador = GerenciadorTarefas()
    gerenciador.carregarEmArquivo()

    while True:
        limparTela()
        exibirMenu()

        try:
            opcaoDoUsuario = int(input("Digite a opção desejada: "))
        except ValueError:
            print("\nERRO!!! Não é permitido letras ou caracteres especiais!!!")
            print("Por favor, digite um número de 1 a 6")
            continue

        match opcaoDoUsuario:
            case 1:
                print("\nDigite alguns dados sobre a tarefa que deseja adicionar")

                titulo = input("\nDigite o titulo da tarefa: ")
                descricao = input("Digite a descrição da tarefa: ")

                tarefa = Tarefa(titulo, descricao)
                gerenciador.adicionarTarefa(tarefa)
                input("\nPressione Enter para continuar...")

            case 2:
                if gerenciador.estaVazio():
                    print("\nA lista de tarefas está vazia!")
                    input("\nPressione Enter para continuar...")
                    continue

                print("\nListando todas as tarefas...")
                gerenciador.listarTarefas()
                input("Pressione Enter para continuar...")
                
            case 3:
                if not gerenciador.temTarefasPendentes():
                    print("\nNão há tarefas pendentes para concluir")
                    input("\nPressione Enter para continuar...")
                    continue

                gerenciador.listarTarefasNaoConcluidas()

                try:
                    indice = int(input("Qual tarefa deseja marcar como CONCLUÍDA? [de acordo com seu ID]: "))
                except ValueError:
                    print("\nERRO!!! Não é permitido letras ou caracteres especiais!!!")
                    print("Por favor, digite apenas o número da tarefa")
                    input("\nPressione Enter para continuar...")                    
                    continue

                tarefaRetornada = gerenciador.concluirTarefaViaIndice(indice - 1)

                if tarefaRetornada:
                    print(f"\nA tarefa {tarefaRetornada.titulo} foi marcada como concluída em {tarefaRetornada.dataConclusao}")

                input("\nPressione Enter para continuar...")

            case 4:
                if not gerenciador.temTarefasConcluidas():
                    print("\nNão há tarefas concluídas para desmarcar")
                    input("\nPressione Enter para continuar...")
                    continue

                gerenciador.listarTarefasConcluidas()

                try:
                    indice = int(input("Qual tarefa deseja DESMARCAR (tornar pendente)? [de acordo com seu ID]: "))
                except ValueError:
                    print("\nERRO!!! Não é permitido letras ou caracteres especiais!!!")
                    print("Por favor, digite apenas o número da tarefa")
                    input("\nPressione Enter para continuar...")                    
                    continue

                tarefaRetornada = gerenciador.desmarcarTarefaViaIndice(indice - 1)

                if tarefaRetornada:
                    print(f"\nA tarefa {tarefaRetornada.titulo} voltou a ficar pendente!")

                input("\nPressione Enter para continuar...")                

            case 5:
                if gerenciador.estaVazio():
                    print("\nA lista de tarefas está completamente vazia!")
                    print("Não há o que excluir!")
                    input("\nPressione Enter para continuar...")
                    continue

                gerenciador.listarTarefas()

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
                        print("\nERRO!!! Não é permitido letras ou caracteres especiais!!!")
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
                        print("\nNão há tarefas concluídas para remover")

                else:
                    print("\nERRO!!! Opção inválida!")

                input("\nPressione Enter para continuar...")

            case 6:
                print("\nSalvando e saindo do programa...\n")
                gerenciador.salvarEmArquivo()
                time.sleep(2)
                break

            case _:
                print("ERRO! Só é permitido números inteiros entre 1 a 6")
                print("Digite novamente!")