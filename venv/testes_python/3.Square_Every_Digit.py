square_digit = 9119

def square_digits(num):
    # Your code heresquare
    number = ""
    for n in str(num):
        square = int(n) ** 2
        number += str(square)
    return int(number)



print(square_digits(square_digit))

# Alternativa
# def square_digits(num):
#     return int(''.join(str(int(d)**2) for d in str(num)))