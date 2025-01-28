import math  


letter_to_index = {chr(i + ord('A')): i for i in range(26)}
index_to_letter = {i: chr(i + ord('A')) for i in range(26)}


def encryptAffine(plaintext, alpha, beta, m):
    plaintext = "".join(plaintext.split())

    ciphertext = []
    if plaintext.isalpha() and len(plaintext) >= 1:
        for i in plaintext:
            idx = letter_to_index[i.upper()]
            x = (alpha * idx + beta) % m
            ciphertext.append(index_to_letter[x])
        return "".join(ciphertext)
    else:
        return "An Error has occurred, please double check input used is valid."


def decryptAffine(ciphertext, alpha, beta, m):
    ciphertext = "".join(ciphertext.split())  

    plaintext = []
    if ciphertext.isalpha() and len(ciphertext) >= 1:
        for a_inv in range(m):
            if (a_inv * alpha) % m == 1:
                break

        for i in ciphertext:
            idx = letter_to_index[i.upper()]
            x = (a_inv * (idx - beta)) % m  
            plaintext.append(index_to_letter[x])
        return "".join(plaintext)  
    else:
        return "An Error has occurred, please double check input used is valid."

def main():
    m = 26  

 
    user_input = input("Would you like to perform encryption or decryption?\nPlease Enter 'e' or 'd': ").lower()
    isValid = True

    if user_input not in ['e', 'd']:
        print("Invalid input, please enter 'e' for encryption or 'd' for decryption.")
        isValid = False
    else:
      
        try:
            alpha = int(input(f"Enter an alpha value between 1 and {m - 1}: "))
            beta = int(input(f"Enter a beta value between 0 and {m - 1}: "))

            if not (1 <= alpha <= m - 1) or not (0 <= beta <= m - 1):
                print("Alpha and Beta values are out of valid range.")
                isValid = False
            elif math.gcd(alpha, m) != 1:
                print(f"The GCD of alpha and {m} must be 1.")
                isValid = False
        except ValueError:
            print("Invalid numeric input, please enter valid integers.")
            isValid = False

    if isValid:
        if user_input == 'e':  
            user_input_plaintext = input("\nPlease enter the plaintext to encrypt: \n").strip()
            ciphertext = encryptAffine(user_input_plaintext, alpha, beta, m)
            print("\nPlaintext (Original): " + user_input_plaintext)
            print("Ciphertext (Encrypted): " + ciphertext)

        elif user_input == 'd':  
            user_input_ciphertext = input("\nPlease enter the ciphertext to decrypt: \n").strip()
            plaintext = decryptAffine(user_input_ciphertext, alpha, beta, m)
            print("\nCiphertext (Original): " + user_input_ciphertext)
            print("Plaintext (Decrypted): " + plaintext)

if __name__ == "__main__":
    main()
