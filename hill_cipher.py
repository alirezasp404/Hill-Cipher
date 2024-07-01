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
    for i in range(text_len//key_len):
        vector = [ord(text[i*key_len+j]) - first_character for j in range(key_len)]
        for p in range(key_len):
         result=0
         for k in range(key_len):
            result+=vector[k] * key[p][k]  
         encrypted_text += chr((result%num_of_characters)+first_character)
    return encrypted_text

# def decrypt(cipher_text, key):
#     decrypted_text = ""
#     n = len(key)
#     det = round((key[0][0]*key[1][1]) - (key[0][1]*key[1][0]))
#     det_inv = 0
#     for i in range(26):
#         if (det * i) % 26 == 1:
#             det_inv = i
#             break
#     key_inv = [[(key[1][1]*det_inv) % 26, (-key[0][1]*det_inv) % 26], [(-key[1][0]*det_inv) % 26, (key[0][0]*det_inv) % 26]]
#     for i in range(0, len(cipher_text), n):
#         vector = [ord(cipher_text[i+j]) - 65 for j in range(n)]
#         result = [(vector[j] * key_inv[j][0] + vector[(j+1)%n] * key_inv[(j+1)%n][0]) % 26 for j in range(n)]
#         decrypted_text += ''.join([chr(result[j] + 65) for j in range(n)])
#     return decrypted_text

key_text = input("Enter the text to generate the key: ")
key = generate_key(key_text)
if key is not None :
    text = input("Enter the text to encrypt: ").upper().replace(" ", "")
    encrypted_text = encrypt(text, key)
    print("Encrypted text: ", encrypted_text)
    # decrypted_text = decrypt(encrypted_text, key)
    # print("Decrypted text: ", decrypted_text)