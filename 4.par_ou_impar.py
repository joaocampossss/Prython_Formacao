"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input("Inserir um numero inteiro: ")

if numero.isdigit(): #Verifica se o numero é numerico
    numero_par_impar = int(numero) % 2 # faz o resto da divisão do numero inserido por 2 para verificar se é par
#   print(numero_par_impar)
    if numero_par_impar == 0:
        print(f"O Numero {numero} é par")
    else:
        print(f"O Numero {numero} é impar")
else:
    print("O numero que inserio não é numerico")