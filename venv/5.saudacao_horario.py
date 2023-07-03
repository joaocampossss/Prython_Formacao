"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input("Inserir o Horário(INT): ")

if horario.isdigit():
    horario_int = int(horario)
    bom_dia = horario_int >= 0 and horario_int <= 11
    boa_tarde = horario_int >= 12 and horario_int <= 17
    boa_noite = horario_int >= 18 and horario_int <= 23
    if bom_dia:
        print("Bom dia")
    if boa_tarde:
        print("Boa Tarde")
    if boa_noite:
        print("Boa Noite")
    if horario_int >= 24:
        print("Essa hora não existe")
else:
    print("O Numero não é inteiro")

