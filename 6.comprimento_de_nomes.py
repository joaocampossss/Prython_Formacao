"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Escreva o seu primeiro Nome: ")

numero_de_letras_no_nome = len(nome) # Verifica com a função len() quantos caracteres tem o nome inserido

if numero_de_letras_no_nome <= 4:
    print("Seu nome é curto")
elif numero_de_letras_no_nome >= 5 and numero_de_letras_no_nome <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")