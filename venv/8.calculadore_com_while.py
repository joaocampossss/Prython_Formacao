while True:
    numero1 = input("Inserir um numero inteiro: ")
    numero2 = input("Inserir um segundo numero inteiro: ")
    operador = input("Inserir um operador para a conta(+-*/): ")

    numero1_float = 0
    numero2_float = 0
    numeros_validos = None

    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Ambos ou algum numero inserido não é válido")
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == "+":
        print(f"Calculo: {numero1_float + numero2_float}")
    elif operador == "-":
        print(f"Calculo: {numero1_float - numero2_float}")
    elif operador == "*":
        print(f"Calculo: {numero1_float * numero2_float}")
    elif operador == "/":
        print(f"Calculo: {numero1_float / numero2_float}")
    
    
    sair = input("Quer sair? [s]im: ").lower().startswith("s")

    if sair is True:
        break

