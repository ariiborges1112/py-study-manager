from datetime import datetime

class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False
        self.dataConclusao = None

    def marcarComoConcluido(self):
        self.concluida = True
        self.dataConclusao = datetime.now().strftime("%d/%m/%Y às %H:%M")

    def marcarComoPendente(self):
        self.concluida = False
        self.dataConclusao = None

    def __str__(self):
        status = "+" if self.concluida else " "
        infoData = f" | Concluída em: {self.dataConclusao}" if self.concluida else ""
        return (
            f"[{status}] {self.titulo}{infoData}\n"
            f"    Descrição: {self.descricao}"
        )

    def paraDict(self):
        return {
            "titulo": self.titulo,
            "descricao": self.descricao,
            "concluida": self.concluida,
            "dataConclusao": self.dataConclusao
        }

    @classmethod
    def deDict(cls, dados):
        novaTarefa = cls(dados["titulo"], dados["descricao"])
        novaTarefa.concluida = dados["concluida"]
        novaTarefa.dataConclusao = dados.get("dataConclusao", None)
        return novaTarefa