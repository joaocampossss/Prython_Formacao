"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

cpf = "746.824.890-70"

cache1 = 0
indice1 = 10

lista_para_primeiro_digito = cpf.split("-") # Dividir a string em dois valores de uma lista

primeiros_9_digitos_cru, *_ = lista_para_primeiro_digito # Desempacotar valores para variavel

primeiros_9_digitos_formatado = primeiros_9_digitos_cru.replace(".", "") # Retirar os pontos da string

""" vertifica se o numero inserido é sequencial
import re
import sys

# cpf_enviado_usuario = '746.824.890-70' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')
entrada = input('CPF [746.824.890-70]: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit() """

# Outro metodo
# cpf = cpf.replace(".", "").replace("-", "")
# print(cpf)

"""
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
"""
for digito in primeiros_9_digitos_formatado:
    valor_multiplicado = indice1 * int(digito)
    cache1 = cache1 + valor_multiplicado
    #Maneira Alternativa
    # cache += i * int(digito)
    indice1 -= 1

# Multiplicar o resultado anterior por 10
# Obter o resto da divisão da conta anterior por 11
resultado_1_digito = (cache1 * 10) % 11
""" Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta """
resultado_1_digito = resultado_1_digito if resultado_1_digito <= 9 else 0

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
primeiros_9_digitos_formatado_mais_resultado1 = primeiros_9_digitos_formatado + str(resultado_1_digito)

cache2 = 0
indice2 = 11

for digito in primeiros_9_digitos_formatado_mais_resultado1:
    cache2 += indice2 * int(digito)
    indice2 -= 1

resultado_2_digito = (cache2 * 10) % 11
resultado_2_digito = resultado_2_digito if resultado_2_digito <= 9 else 0

cpf_gerado_pelo_calculo = cpf[:12] + str(resultado_1_digito) + str(resultado_2_digito)

if cpf_gerado_pelo_calculo == cpf:
    print(f"O CPF {cpf} é válido")
else:
    print(f"O CPF {cpf} não é válido")

