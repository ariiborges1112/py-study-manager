class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False

    def estaConcluida(self):
        if self.concluida:
            print(f"A tarefa {self.titulo} já está concluída")
        else:
            print(f"A tarefa {self.titulo} não está concluída")

    def concluir(self):
        self.concluida = True

    def __str__(self):
        status = "+" if self.concluida else " "
        return f"[{status}] {self.titulo}: {self.descricao}"

    def paraDict(self):
        return {
            "titulo": self.titulo,
            "descricao": self.descricao,
            "concluida": self.concluida
        }

    @classmethod
    def deDict(cls, dados):
        novaTarefa = cls(dados["titulo"], dados["descricao"])
        novaTarefa.concluida = dados["concluida"]
        return novaTarefa