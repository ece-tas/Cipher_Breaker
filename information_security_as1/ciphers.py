import argparse
import math

len_alph = 26
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dict_alph = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 
    'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 
    'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 
    'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

# python ciphers.py caesar plaintext_ceasar.txt e -s 20
def encrypt_caesar(plaintext, shift):
    cipher = alph[-shift:] + alph[:-shift]
    encrypted_text = ""
    
    for letter in plaintext:
        if (letter.isalpha()):
            index = alph.find(letter.upper())
            if (index != -1):
                if letter.islower():
                    encrypted_text += cipher[index].lower()
                else:
                    encrypted_text += cipher[index]
        else:
            encrypted_text += letter    # if it is not a letter, don't change

    return encrypted_text   


# python ciphers.py caesar ciphertext_ceaser.txt d -s 20
def decrypt_caesar(ciphertext, shift):
    shift = len_alph - shift
    return encrypt_caesar(ciphertext, shift)

#ENCRYPTION
#RSLEZYKDVS
# python ciphers.py affine coded.txt e -a 3 -b 5
def encrypt_affine(plaintext, a, b):
    encrypted_text = ""

    if(are_relatively_prime(a, len_alph)):
        for letter in plaintext:
            if (letter.isalpha()):
                index = alph.find(letter.upper())
                hash = (a * index + b) % len_alph
                if (index != -1):
                    if letter.islower():
                       encrypted_text += alph[hash].lower()
                    else:
                        encrypted_text += alph[hash]
            else:
                encrypted_text += letter        # if it is not a letter, don't change
    return encrypted_text

# python ciphers.py affine ciphertext_affine.txt d -a 3 -b 5    
def decrypt_affine(plaintext, a, b):
    decrypted_text = ""
    
    a_inv = mod_inverse(a, len_alph)  # Find the modular inverse of 'a'
    if a_inv is None:
        raise ValueError(f"{a} has no modular inverse mod {len_alph}, decryption not possible.")
    
    for letter in plaintext:
        if letter.isalpha():  
            index = alph.find(letter.upper())
            if index != -1:
                # Decrypt using the formula: a_inv * (index - b) % len_alph
                hash = (a_inv * (index - b)) % len_alph
                if letter.islower():
                    decrypted_text += alph[hash].lower()
                else:
                    decrypted_text += alph[hash]
        else:
            decrypted_text += letter    # if it is not a letter, don't change
    
    return decrypted_text


# python ciphers.py mono plaintext_mono.txt e -k QWERTYUIOPASDFGHJKLZXCVBNM
def encrypt_mono(plaintext, key):
    encrypted_text = ""
    key = key.upper()
    
    for letter in plaintext:
        if letter.isalpha():
            index = alph.find(letter.upper())
            if index != -1:
                if letter.islower():
                    encrypted_text += key[index].lower()
                else:
                    encrypted_text += key[index]
        else:            
            encrypted_text += letter

    return encrypted_text            

# python ciphers.py mono ciphertext_mono.txt d -k QWERTYUIOPASDFGHJKLZXCVBNM
def decrypt_mono(plaintext, key):
    decrypted_text = ""
    key = key.upper()
    for letter in plaintext:
        if letter.isalpha():
            index = key.find(letter.upper())                
            if index != -1:
                if letter.islower():
                    decrypted_text += alph[index].lower()
                else:
                    decrypted_text += alph[index]    
        else:            
            decrypted_text += letter

    return decrypted_text  


def are_relatively_prime(a, m):
    return math.gcd(a, m) == 1

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None  # No modular inverse exists if gcd(a, m) != 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="ciphers", description="encyript ciphers")

    parser.add_argument("cipher", help="Choose cipher: caesar, affine, mono")
    parser.add_argument("file", help="Input file containing the text")
    parser.add_argument("mode", help="e for encryption, d for decryption")

    parser.add_argument("-s", "--SHIFT", required=False, help="Shift value for Caesar cipher", type=int)
    parser.add_argument("-a", "--A_value", required=False, help="a value for Affine cipher", type=int)
    parser.add_argument("-b", "--B_value", required=False, help="b value for Affine cipher", type=int)
    parser.add_argument("-k", "--KEY", required=False, help="Key for Mono-alphabetic cipher")

    args = parser.parse_args()

    with open(args.file, "r") as f:
        text = f.read()


    if args.cipher == "caesar":
        if args.mode == "e":
            print(encrypt_caesar(text, args.SHIFT))
        elif args.mode == "d":
            print(decrypt_caesar(text, args.SHIFT))
        
    elif args.cipher == "affine":
        if args.mode == "e":
            print(encrypt_affine(text, args.A_value, args.B_value))
        elif args.mode == "d":
            print(decrypt_affine(text, args.A_value, args.B_value))

    elif args.cipher == "mono":
            if args.mode == "e":
                print(encrypt_mono(text, args.KEY))
            elif args.mode == "d":
                print(decrypt_mono(text, args.KEY))
        

