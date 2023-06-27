"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os # Executa comandos de sistema operativo

#                  01234567
palavra_secreta = "palomito" 
tentativas = 0
letras_acertadas = "" # Guarda as letras acertadas
cache = "" # Contem a palavra com os asteriscos

while cache != "palomito":
    tentativa_de_letra = input("Digite uma letra: ") # input da tentativa de letra e contagem de tentativas
    tentativas += 1
    
    if len(tentativa_de_letra) > 1: # se for inserido mais que 1 caractere ele avisa o utilizador e continua 
        print("Digite apenas uma letra")
        continue

    if tentativa_de_letra in palavra_secreta: # Se a letra estiver na palavra secreta ele adiciona a letra na variavel
        letras_acertadas += tentativa_de_letra

    cache = "" # è definida novamente a variavel para dar reset sempre que se corre o while
    for letra_secreta in palavra_secreta: 
        # para todas as letras da palavra secreta ele compara com a letra inserida/ Acertada e adiciona à cache que guarda a palavra porque as letras estão na variavel letras_acertadas
        if letra_secreta in letras_acertadas:
            cache += letra_secreta
        else:
            cache += "*"
    os.system("cls") # limpa a cmd
    print(f"Palavra Formada: {cache}")

# quando a regra de while for cumprida neste caso o cache seja igual à palavra ele sai e executa o bloco asgr.
print(f"Palavra Secreta era: {palavra_secreta} parabens!!\nVocê completou o jogo com {tentativas} tentativasa") 
#Outro metodo
"""
palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
"""