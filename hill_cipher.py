from laplace_expansion import determinant
import math
first_character=64
num_of_characters=27
def is_key_valid(det):
    if det == 0:
        return False
    if math.gcd(det, num_of_characters) != 1:
        return False
    return True

def generate_key(text):
    if not text.isalpha():
        raise ValueError("Key must contain only alphabetic characters (A-Z or a-z)")
    dim = round(math.sqrt(len(text)))
    if(dim!=math.sqrt(len(text))):
        raise ValueError("The length of the Key should be the square of a number")
    key = [[0 for i in range(dim)] for j in range(dim)]
    text = text.replace(" ", "").upper()
    for i in range(dim*dim):
        key[i//dim][i%dim] = (ord(text[i]) - first_character)% num_of_characters

    det = round(determinant(key))
    if (is_key_valid(det)==False):
        raise ValueError("Key must be invertible")
    return key

def encrypt(text, key):
    if not text.isalpha():
        raise ValueError("Input must contain only alphabetic characters (A-Z or a-z)")
    encrypted_text = ""
    key_len = len(key)
    text_len=len(text)
    if(text_len%key_len!=0):
        for h in range(text_len%key_len):
            text+='@'
    for i in range(len(text)//key_len):
        vector = [ord(text[i*key_len+j]) - first_character for j in range(key_len)]
        for p in range(key_len):
         result=0
         for k in range(key_len):
            result+=vector[k] * key[p][k]  
         encrypted_text += chr((result%num_of_characters)+first_character)
    return encrypted_text


def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def matrix_cofactor(matrix):
    return [
        [
            ((-1) ** (i + j)) * determinant([row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])])
            for j in range(len(matrix))
        ]
        for i in range(len(matrix))
    ]

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]

def generate_invert_key(key):
    det = round(determinant(key)) % num_of_characters
    det_inv = mod_inverse(det, num_of_characters)
    
    if det_inv is None:
        raise ValueError("The key matrix is not invertible modulo 26")
    
    cofactor_matrix = matrix_cofactor(key)
    adj_matrix = transpose(cofactor_matrix)
    
    inv_key = [[(det_inv * adj_matrix[i][j]) % num_of_characters for j in range(len(key))] for i in range(len(key))]
    
    return inv_key

def validate_decryption_input(text):
    for char in text:
        if not char.isalpha() and char != '@':
            raise ValueError(f"Invalid character '{char}' found. Only alphabetic characters and '@' are allowed.")
        
def decrypt(text,key):
    invert_key= generate_invert_key(key)
    validate_decryption_input(text)
    decrypted_text = ""
    key_len = len(invert_key)
    text_len=len(text)
    if(text_len%key_len!=0):
        raise ValueError("Input length for decryption must be a multiple of 2 ")
    for i in range(text_len//key_len):
        vector = [ord(text[i*key_len+j]) - first_character for j in range(key_len)]
        for p in range(key_len):
         result=0
         for k in range(key_len):
            result+=vector[k] * invert_key[p][k]  
         decrypted_text += chr((result%num_of_characters)+first_character)
    decrypted_text=decrypted_text.replace("@", "")

    return decrypted_text
    
key_text = input("Enter the text to generate the key: ")
key = generate_key(key_text)
if key is not None :
    text = input("Enter the text to encrypt: ").upper().replace(" ", "")
    encrypted_text = encrypt(text, key)
    print("Encrypted text: ", encrypted_text)
    text = input("Enter the text to decrypt: ").upper().replace(" ", "")
    decrypted_text = decrypt(text, key)
    print("Decrypted text: ", decrypted_text)
