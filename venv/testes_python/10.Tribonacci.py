def tribonacci(signature, n):
    if n < 3:
        signature = signature[:n]
    for n in range(n-3):
        last_tree = signature[-3:]
        next_number = sum(last_tree)
        signature.append(next_number)
    print(signature)


tribonacci([1, 1, 1], 0)