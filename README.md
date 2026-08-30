# 📝 Py Study Manager - Gerenciador de Tarefas

Aplicação de linha de comando (CLI) desenvolvida em Python para gerenciamento e organização de tarefas de estudo e rotina diária, com suporte à persistência de dados em formato JSON.

---

## 🚀 Funcionalidades

- **Adicionar Tarefas:** Cadastro de novas tarefas com título e descrição.
- **Listar Tarefas:** Exibição completa de todas as tarefas cadastradas.
- **Filtragem por Status:** Visualização dedicada para tarefas pendentes ou concluídas.
- **Controle de Estado:** Permite marcar tarefas como concluídas ou revertê-las para pendentes.
- **Exclusão Flexível:** Remoção de uma tarefa específica por ID ou limpeza em massa de todas as concluídas.
- **Persistência de Dados:** Salvamento automático das alterações em um arquivo local `tarefas.json`.
- **Interface Limpa:** Tratamento contra erros de digitação (exceções) e limpeza automática de tela a cada navegação.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **JSON** (para persistência de dados)
- **OS & Time** (para manipulação de terminal e controle de fluxo)

---

## 📁 Estrutura do Projeto

```text
py-study-manager/
│
├── main.py                # Interface de linha de comando e fluxo principal
├── gerenciadorTarefas.py  # Controller (regras de negócio e manipulação da lista)
├── tarefa.py              # Classe modelo (atributos e conversão de/para dicionário)
├── .gitignore             # Arquivo de exclusão do Git (ignora dados sensíveis e cache)
└── README.md              # Documentação do projeto