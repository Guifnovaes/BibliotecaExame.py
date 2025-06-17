from datetime import datetime


livros = []
usuarios = {}
emprestimos = []
livros_set = set()


class Memoria:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir(self, valor):
        novo = Memoria(valor)
        if not self.inicio:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

    def listar(self):
        atual = self.inicio
        while atual:
            print(f"{atual.valor[0]} cadastrado: {atual.valor[1]}")
            atual = atual.proximo

class Armazenamento:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None
        
class ListaDevolucoesDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir(self, valor):
        novo = Armazenamento(valor)
        if not self.inicio:
            self.inicio = self.fim = novo
        else:
            self.fim.proximo = novo
            novo.anterior = self.fim
            self.fim = novo

    def listar(self):
        atual = self.inicio
        print("\nHistórico de Devoluções:")
        while atual:
            print(atual.valor)
            atual = atual.proximo


log_operacoes = ListaEncadeada()
historico_devolucoes = ListaDevolucoesDupla()


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"

class Emprestimo:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro
        self.data = datetime.now()

    def __str__(self):
        return f"{self.usuario.nome} pegou '{self.livro.titulo}' em {self.data.strftime('%d/%m/%Y')}"

def cadastrar_livro():
    titulo = input("Título do livro: ")
    autor = input("Autor: ")
    if titulo in livros_set:
        print("Livro já cadastrado!")
    else:
        livros.append(Livro(titulo, autor))
        livros_set.add(titulo)
        log_operacoes.inserir(("Livro", titulo))
        print("Livro cadastrado!")

def cadastrar_usuario():
    nome = input("Nome do usuário: ")
    cpf = input("CPF: ")
    if cpf in usuarios:
        print("Usuário já cadastrado!")
    else:
        usuarios[cpf] = Usuario(nome, cpf)
        log_operacoes.inserir(("Usuário", nome))
        print("Usuário cadastrado!")

def realizar_emprestimo():
    cpf = input("CPF do usuário: ")
    titulo = input("Título do livro: ")
    usuario = usuarios.get(cpf)
    livro = next((l for l in livros if l.titulo == titulo), None)
    if usuario and livro:
        emprestimos.append(Emprestimo(usuario, livro))
        log_operacoes.inserir(("Empréstimo", f"{usuario.nome} -> {titulo}"))
        print("Empréstimo registrado.")
    else:
        print("Usuário ou livro não encontrado.")

def listar_livros():
    print("\nLivros cadastrados:")
    for livro in livros:
        print(livro)

def listar_emprestimos():
    print("\nEmpréstimos registrados:")
    for e in emprestimos:
        print(e)

def ver_log_operacoes():
    print("\nLog de operações:")
    log_operacoes.listar()

def realizar_devolucao():
    cpf = input("CPF do usuário: ")
    titulo = input("Título do livro para devolução: ")
    emprestimo_encontrado = None
    for e in emprestimos:
        if e.usuario.cpf == cpf and e.livro.titulo == titulo:
            emprestimo_encontrado = e
            break

    if emprestimo_encontrado:
        emprestimos.remove(emprestimo_encontrado)
        devolucao = f"{emprestimo_encontrado.usuario.nome} devolveu '{emprestimo_encontrado.livro.titulo}' em {datetime.now().strftime('%d/%m/%Y')}"
        historico_devolucoes.inserir(devolucao)
        log_operacoes.inserir(("Devolução", f"{emprestimo_encontrado.usuario.nome} -> {titulo}"))
        print("Devolução registrada.")
    else:
        print("Empréstimo não encontrado.")

def ver_historico_devolucoes():
    historico_devolucoes.listar()

def menu():
    opcoes = {
        "1": cadastrar_livro,
        "2": cadastrar_usuario,
        "3": realizar_emprestimo,
        "4": listar_livros,
        "5": listar_emprestimos,
        "6": ver_log_operacoes,
        "7": realizar_devolucao,
        "8": ver_historico_devolucoes
    }
    while True:
        print("\n1. Cadastrar livro\n2. Cadastrar usuário\n3. Realizar empréstimo\n4. Listar livros\n5. Listar empréstimos\n6. Ver log de operações\n7. Realizar devolução\n8. Ver histórico de devoluções\n9. Sair")
        op = input("Escolha uma opção: ")
        if op == "9":
            break
        func = opcoes.get(op)
        func() if func else print("Opção inválida.")

if __name__ == "__main__":
    menu()

