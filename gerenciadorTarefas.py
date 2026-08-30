import json
from tarefa import Tarefa

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionarTarefa(self, tarefa):
        self.tarefas.append(tarefa)
        print(f"\nA Tarefa '{tarefa.titulo}' adicionada com sucesso!")

    def listarTarefas(self):
        print("\n==== LISTA DE TAREFAS ====")
        for i, tarefa in enumerate(self.tarefas, start=1):
            print(f"Tarefa {i}:\n{tarefa}\n")

    def listarTarefasConcluidas(self):
        print("\n==== TAREFAS CONCLUÍDAS ====")
        for i, tarefa in enumerate(self.tarefas, start=1):
            if tarefa.concluida:
                print(f"ID da Tarefa: [{i}]")
                print(f"{tarefa.titulo}")
                print(f"{tarefa.descricao}\n")

    def listarTarefasNaoConcluidas(self):
        print("\n==== TAREFAS NÃO CONCLUÍDAS ====")
        for i, tarefa in enumerate(self.tarefas, start=1):
            if not tarefa.concluida:
                print(f"ID da Tarefa: [{i}]")
                print(f"{tarefa.titulo}")
                print(f"{tarefa.descricao}\n")

    def concluirTarefaViaIndice(self, indice):
        if indice < 0 or indice >= len(self.tarefas):
            print("\nO valor do índice está INCORRETO!")
            return

        tarefa = self.tarefas[indice]
        tarefa.marcarComoConcluido()

        return tarefa

    def desmarcarTarefaViaIndice(self, indice):
        if indice < 0 or indice >= len(self.tarefas):
            print("\nO valor do índice está INCORRETO!")
            return
    
        tarefa = self.tarefas[indice]
        tarefa.marcarComoPendente()

        return tarefa
    
    def removerTarefa(self, indice):
        if indice < 0 or indice >= len(self.tarefas):
            print("\nO valor do índice está INCORRETO!")
            return
            
        tarefaRemovida = self.tarefas.pop(indice)

        return tarefaRemovida

    def removerTarefasConcluidas(self):
        tarefasPendentes = []

        for tarefa in self.tarefas:
            if not tarefa.concluida:
                tarefasPendentes.append(tarefa)

        totalRemovidas = len(self.tarefas) - len(tarefasPendentes)
        self.tarefas = tarefasPendentes

        return totalRemovidas

    def temTarefasPendentes(self) -> bool:
        return any(not tarefa.concluida for tarefa in self.tarefas)

    def temTarefasConcluidas(self) -> bool:
        return any(tarefa.concluida for tarefa in self.tarefas)

    def estaVazio(self) -> bool:
        return len(self.tarefas) == 0

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