def rot13(message):
    lista = []
    for palavra in message:
        string = ""
        for letra in palavra:
            if 'A' <= letra <= 'Z':
                ciphra = chr((ord(letra) - ord('A') + 13) % 26 + ord('A'))
            elif 'a' <= letra <= 'z':
                ciphra = chr((ord(letra) - ord('a') + 13) % 26 + ord('a'))
            else:
                ciphra = letra
            string += ciphra
        lista.append(string)
    print(''.join(lista))
rot13('1     3     abzzq  &!  2')