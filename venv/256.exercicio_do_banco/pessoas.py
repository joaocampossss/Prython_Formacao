import contas


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        self._idade = valor

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None


if __name__ == '__main__':
    # pessoa1 = Pessoa('João', 10)
    # print(pessoa1.nome, pessoa1.idade)
    # pessoa1.idade = 22
    # print(pessoa1.nome, pessoa1.idade)

    cliente1 = Cliente('João', 21)
    conta1 = contas.ContaCorrente(1, 'teste', 500, 100)
    # conta1.depositar(100)
    # conta1.sacar(650)
    # conta1.verificar_saldo()
    print(cliente1)
    print(conta1)
