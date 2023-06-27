# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def multiplicador(*args):
    total = 1
    for numeros in args:
        total *= numeros
    print(total)
    return total

def par_impar(x):
    resto = x % 2
    if resto == 0:
        print(f"O Numero {x} é Par")
    else:
        print(f"{x} é Impar")

numero_multiplicado = multiplicador(1, 2, 3, 4, 5)
par_impar(numero_multiplicado)


