import random

cpf = ""

for i in range(9):
    cpf += str(random.randint(0, 9))

print(cpf)

cache1 = 0
indice1 = 10



for digito in cpf:
    cache1 += indice1 * int(digito)
    indice1 -= 1

resultado_1_digito = (cache1 * 10) % 11
resultado_1_digito = resultado_1_digito if resultado_1_digito <= 9 else 0

primeiros_9_digitos_formatado_mais_resultado1 = cpf + str(resultado_1_digito)

cache2 = 0
indice2 = 11

for digito in primeiros_9_digitos_formatado_mais_resultado1:
    cache2 += indice2 * int(digito)
    indice2 -= 1

resultado_2_digito = (cache2 * 10) % 11
resultado_2_digito = resultado_2_digito if resultado_2_digito <= 9 else 0

cpf_gerado_pelo_calculo = cpf + str(resultado_1_digito) + str(resultado_2_digito)

print(cpf_gerado_pelo_calculo)