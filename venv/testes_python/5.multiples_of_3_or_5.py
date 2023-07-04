def solution(number):
    valor = 0
    for n in range(number):
        if (n % 3) == 0:
            valor += n
            continue
        elif (n % 5) == 0:
            valor += n
            continue
    return valor

# def solution(number):
#     return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
  

        --

print(solution(6))