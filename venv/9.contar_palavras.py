frase = "O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.".lower()

i = 0
tamanho_frase = len(frase)

quantidade = 0 # Variaveis para guardar histórico
letra_com_mais_contagem = ""

while i < tamanho_frase:
    
    letra = frase[i]  # A cada loop é testada uma letra com o i 
    i += 1 # Adicionado mais 1 para o proximo loop

    if letra == " ": # Salta o espaço
        continue
    
    letra_quantidade_atual = frase.count(letra) # Faz a contagem da letra na frase
    
    if quantidade < letra_quantidade_atual: # Se a quantidade atual for maior que a que está guardada em cache este if corre e atualiza os valores
        quantidade = letra_quantidade_atual
        letra_com_mais_contagem = letra

print(f"A letra mais presente na frase é {letra_com_mais_contagem}, que aparece {quantidade} vezes")
