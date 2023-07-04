quote = "how can mirrors be real if our eyes aren't real"  # .capitalize()


def to_jaden_case(string):
    lista = str(string).split(" ")
    lista_capitalizada = [ camel.capitalize() for camel in lista ]
    return " ".join(lista_capitalizada)


print(to_jaden_case(quote))

