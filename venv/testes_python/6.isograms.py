def is_isogram(string):
    string = string.lower()
    for letter in string:
        counting = string.count(letter)
        print(letter, counting)
        if counting > 1:
            return False
    return True

print(is_isogram('Dermatoglyphics'))
print(is_isogram('moose'))
print(is_isogram('aba'))
print(is_isogram(''))

def is_isogram(string):
    return len(string) == len(set(string.lower())) 