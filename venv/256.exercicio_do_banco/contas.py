import abc


class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor): ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'Depositado {valor}')

    def detalhes(self, msg=''):
        print(f'O seu Saldo é {self.saldo:.2f} {msg}')
        print('--')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if (self.saldo - valor) < 0:
            self.detalhes(f'Não é possivel sacar {valor} Saldo insuficiente')
        else:
            self.saldo -= valor
            self.detalhes(f'{valor} sacado com sucesso')

    def depositar(self, valor):
        return super().depositar(valor)

    def verificar_saldo(self):
        return self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo - valor) < -self.limite:
            self.detalhes(
                f'Não é possivel sacar {valor} Saldo insuficiente\
 | Limite = {-self.limite}'
            )

        elif (self.saldo - valor) < self.limite:
            self.saldo -= valor
            self.detalhes(f'{valor} sacado com sucesso')
            self.detalhes(
                f'Atenção está a usar {self.limite + self.saldo}\
 do limite extra'
            )

        else:
            self.saldo -= valor
            self.detalhes(f'{valor} sacado com sucesso')

    def depositar(self, valor):
        return super().depositar(valor)

    def verificar_saldo(self):
        return self.detalhes()

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
            f'{self.limite!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    # conta1 = ContaPoupanca(1, 'teste', 500)
    # conta1.depositar(100)
    # conta1.sacar(700)
    # print('@@@@@@@@@@@@@@@@@')
    conta2 = ContaCorrente(1, 'teste', 500, 100)
    conta2.depositar(100)
    conta2.sacar(650)
    conta2.verificar_saldo()
