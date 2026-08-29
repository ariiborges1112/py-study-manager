import json
from tarefa import Tarefa

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionarTarefa(self, tarefa):
        self.tarefas.append(tarefa)
        print(f"Tarefa '{tarefa.titulo}' adicionada com sucesso!")

    def listarTarefas(self):
        if not self.tarefas:
            print("A lista de tarefas está vazia")
            return
    
        print("\n==== LISTA DE TAREFAS ====")
        for i, tarefa in enumerate(self.tarefas, start=1):
            print(f"Tarefa {i}:\n{tarefa}\n")

    def listarTarefasNaoConcluidas(self):
        if not self.tarefas:
            print("A lista de tarefas está vazia")
            return

        temPendencias = False
        
        for i, tarefa in enumerate(self.tarefas, start=1):
            if not tarefa.concluida:
                temPendencias = True
                print(f"ID da Tarefa: [{i}]")
                print(f"{tarefa.titulo}")
                print(f"{tarefa.descricao}\n")

        if not temPendencias:
            print("Não há tarefas pendentes, parabéns!")
            return

    def concluirTarefaViaIndice(self, indice):
        if indice < 0 or indice >= len(self.tarefas):
            print("O valor do índice está incorreto")
            return

        tarefaConcluida = self.tarefas[indice]
        tarefaConcluida.concluir()

        return tarefaConcluida

    def removerTarefa(self, indice):
        if indice < 0 or indice >= len(self.tarefas):
            print("O valor do índice está incorreto")
            return
            
        tarefaRemovida = self.tarefas.pop(indice)

        return tarefaRemovida

    def salvarEmArquivo(self, caminhoArquivo="tarefas.json"):
        listaTraduzida = []
        for tarefa in self.tarefas:
            listaTraduzida.append(tarefa.paraDict())

        with open(caminhoArquivo, "w", encoding="utf-8") as arquivo:
            json.dump(listaTraduzida, arquivo, indent=4)

    def carregarEmArquivo(self, caminhoArquivo="tarefas.json"):
        try:
            with open(caminhoArquivo, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

                for tarefa in dados:
                    tarefaRecriada = Tarefa.deDict(tarefa)
                    self.tarefas.append(tarefaRecriada)
        except FileNotFoundError:
            pass