from random import sample
from itertools import product as col


def generator(key, char, length):
    char_len = key.count(char)
    key_piece = key[:length - char_len]
    list_keys = [key_piece + "".join(i) for i in list(col([chr(i) for i in range(65, 65+26)], repeat=char_len))]
    return list_keys


def vigenere(x, key, encrypt):
    lst_final = []
    code = list(x)
    j = 0

    for i, char in enumerate(code):
        if char.isalpha():
            code[i] = key[(i + j) % len(key)]
            if encrypt:
                lst_final.append((ord(x[i]) + ord(code[i]) - 65 * 2) % 26)  # Encrypt
            else:
                lst_final.append((ord(x[i]) - ord(code[i])) % 26)  # Decrypt
        else:
            lst_final.append(ord(char))  
            j -= 1
            

    for i, char in enumerate(code):
        if char.isalpha():
            lst_final[i] = chr(lst_final[i] + 65)
        else:
            lst_final[i] = chr(lst_final[i])

    return ''.join(lst_final)


print("Welcome to the Vigenère cipher")

if input('Encrypt or Decrypt: ').lower() == 'e':
    x = input('Enter the text: ').upper()
    key = input('Enter the key: ').upper()
    encrypt = True
    print(vigenere(x, key, encrypt))
    
    
else:
    x = input('Enter the text: ').upper()
    encrypt = False
    if input('Do you have the key (y/n)? ') == "y":
        key = input('Enter the key: ').upper()
        print(vigenere(x, key, encrypt))
        
        
    else:
        abc = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        question = input('Enter a part of the key or length (answer by 1 or 2 or nothing): ')
        if question == '1':
            key = input('*Use \'?\' for the missing letter in the key (e.g., C?? or CL? for ex to CLE): ').upper()
            list_of_keys = generator(key, '?', len(key))
            for k in list_of_keys:
                print(f'For key {k} ==> {vigenere(x, k, encrypt)}')
        elif question == '2':
            length = int(input('Enter the length: '))
            while True:
                key_gen = ''.join(sample(abc, length))
                print(f"For generated key {key_gen} = {vigenere(x, key_gen, encrypt)}")
                if input('Continue (y/n)? ') == "n":
                    break
        else:
            print("Sorry, this script cannot find your encrypted text without sufficient input.")
