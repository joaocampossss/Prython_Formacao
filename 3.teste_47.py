#Teste de conhecimento com manipulação de stings

nome = input("Inserir o seu nome: ")
idade = input("Inserir sua idade: ")

#if bool(nome) != False and bool(idade) != False:
if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if " " in nome:
        print("Seu nome contem espaços")
    else:
        print("Seu nome não contem espaços")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra de seu nome é {nome[0]}")
    print(f"A ultima letra de seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios")