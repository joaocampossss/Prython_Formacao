def pig_it(text):
    res = []
    
    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)
            
    return ' '.join(res)

# def pig_it(text):
#     string=[]
#     pontuacao = ['?', '!', '.', ',', ';', ':', '-', '"', "'"]
#     for palavra in text.split():
#         if not str(palavra).startswith(tuple(pontuacao)):
#             for letra in palavra[0]:
#                 primeira_letra = letra
#             i = str(palavra).replace(palavra[0], '',1)
#             string.append(i + primeira_letra + 'ay')
#         else:
#             string.append(palavra)
        
#     print (' '.join(string))



pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Nunc est bibenbdum')     # elloHay orldway !

