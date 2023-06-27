# Exercício - sistema de perguntas e respostas
import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

def perguntas_respostas(numero_pergunta):
    perguntas_acertadas = 0
    print(f"{perguntas[numero_pergunta]['Pergunta']}\nOpções:")
    for i, opcoes in enumerate(perguntas[numero_pergunta]["Opções"]):
        print(f"{i}) {opcoes}")
    
    resposta_indice = input("Escolha uma Opção: ")

    try:
        resposta_indice = int(resposta_indice)
        if perguntas[numero_pergunta]["Opções"][resposta_indice] == perguntas[numero_pergunta]["Resposta"]:
            print("\nAcertou :)\n")
            perguntas_acertadas += 1
        else:
            print("\nErrou :(\n")
    except IndexError:
        print("O Indice Inserido NÃO EXISTE")
    except ValueError:
        print("Por Favor Insira um Indice Válido")

    return perguntas_acertadas

os.system("cls")
pergunta_1 = perguntas_respostas(0)
pergunta_2 = perguntas_respostas(1)
pergunta_3 = perguntas_respostas(2)
respostas_certas = pergunta_1 + pergunta_2 + pergunta_3
print(f"Acertou {respostas_certas} Respostas de 3 Perguntas")