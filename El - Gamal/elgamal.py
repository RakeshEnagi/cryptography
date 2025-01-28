import random
from sympy import isprime


def generate_prime(bits=512):
    prime = random.getrandbits(bits)
    while not isprime(prime):
        prime = random.getrandbits(bits)
    return prime


def generate_keypair(bits=512):
    p = generate_prime(bits) 
    g = random.randint(2, p-1)  
    x = random.randint(2, p-2)  
    h = pow(g, x, p)  
    return (p, g, h), (p, g, x)


def encrypt(public_key, plaintext):
    p, g, h = public_key
    ciphertext = []
    for char in plaintext:
        m = ord(char)  
        y = random.randint(2, p-2)  
        c1 = pow(g, y, p)  
        c2 = (m * pow(h, y, p)) 
        ciphertext.append((c1, c2))
    return ciphertext



def decrypt(private_key, ciphertext):
    p, g, x = private_key
    plaintext = ""
    for c1, c2 in ciphertext:
        m = (c2 * pow(c1, p - 1 - x, p)) % p  
        plaintext += chr(m)
    return plaintext


if __name__ == "__main__":
    print("Generating ElGamal keys...")
    public_key, private_key = generate_keypair(bits=512)

    print("Public Key:", public_key)
    print("Private Key:", private_key)

    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("\nEnter your choice (1/2/3): ")

        if choice == '1':
         
            message = input("\nEnter a message to encrypt: ")
            encrypted_message = encrypt(public_key, message)
            print("\nEncrypted Message:", encrypted_message)
        elif choice == '2':
      
            encrypted_message_input = input("\nEnter the encrypted message (format: (c1, c2) (c1, c2) ...): ")
            
       
            encrypted_message_input = encrypted_message_input.strip()
            encrypted_message_input = encrypted_message_input.replace(") (", ") (") 
            encrypted_message_input = encrypted_message_input.strip('()')
            encrypted_message = []
            
            for pair in encrypted_message_input.split(") ("):
                pair = pair.strip("()")
                c1, c2 = map(int, pair.split(","))
                encrypted_message.append((c1, c2))
            
            decrypted_message = decrypt(private_key, encrypted_message)
            print("\nDecrypted Message:", decrypted_message)
        elif choice == '3':
            print("\nExiting the program...")
            break
        else:
            print("\nInvalid choice, please try again.")
