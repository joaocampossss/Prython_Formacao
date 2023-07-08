class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def imprimeSelf(self):
        print(f'Atributos da instância:\n{self.nome=}\n{self.sobrenome=}\n')
        print(f'Valor da instância no {self=}')
    
pedro = Pessoa("Pedro", "Almeida")
paulo = Pessoa("Paulo", "José")
    
pedro.imprimeSelf()
print(f'Valor do atributo {pedro=}\n')
paulo.imprimeSelf()
print(f'Valor do atributo {paulo=}')