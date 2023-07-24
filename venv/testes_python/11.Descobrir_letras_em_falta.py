def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))


# def find_missing_letter(chars):
#     letra = ''
#     for n in chars:
#         if not letra:
#             if 'A' <= n <= 'Z':
#                 letra = chr((ord(n) - ord('A') + 1) % 26 + ord('A'))
#             elif 'a' <= n <= 'z':
#                 letra = chr((ord(n) - ord('a') + 1) % 26 + ord('a'))
#         elif n == letra:
#             if 'A' <= n <= 'Z':
#                 letra = chr((ord(n) - ord('A') + 1) % 26 + ord('A'))
#             elif 'a' <= n <= 'z':
#                 letra = chr((ord(n) - ord('a') + 1) % 26 + ord('a'))
#         else:
#             return letra
            



# find_missing_letter(['a','b','c','d','f'])
# find_missing_letter(['O','Q','R','S'])