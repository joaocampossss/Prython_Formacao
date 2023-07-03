#O pretendido é *j*o*a*o* *c*a*m*p*o*s

nome = "joao campos"

tamanho_nome = len(nome)

numero = 0

while numero < tamanho_nome:
    print(f"*{nome[numero]}", end="")
    numero += 1

#Outra maneira de resolver
indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice] # é retirada letra a letra e depois adicionada na linha de baixo numa nova variavel que no fim é imprimida
    novo_nome += f'*{letra}'
    indice += 1
print()
print(novo_nome)