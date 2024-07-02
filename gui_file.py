import tkinter as tk
from tkinter import messagebox
import math
window = tk.Tk()


##gauss jordan
def determinant_gauss_jordan(matrix):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        messagebox.showinfo("error", "Input matrix must be a list of lists.")
        raise ValueError("Input matrix must be a list of lists.")
    
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        messagebox.showinfo("error", "Input matrix must be square.")
        raise ValueError("Input matrix must be square.")
    
    augmented_matrix = [row + [0] * n for row in matrix]
    
    det = 1
    for i in range(n):
        # Pivot (largest absolute value in the current column below the diagonal)
        pivot = i
        for j in range(i + 1, n):
            if abs(augmented_matrix[j][i]) > abs(augmented_matrix[pivot][i]):
                pivot = j
        
        # Check for zero pivot
        if abs(augmented_matrix[pivot][i]) < 1e-10:
            return 0
        
        # Swap rows if necessary
        if pivot != i:
            augmented_matrix[i], augmented_matrix[pivot] = augmented_matrix[pivot], augmented_matrix[i]
            det *= -1
        
        # Gauss-Jordan elimination
        det *= augmented_matrix[i][i]
        for j in range(i + 1, n):
            factor = augmented_matrix[j][i] / augmented_matrix[i][i]
            for k in range(n * 2):
                augmented_matrix[j][k] -= factor * augmented_matrix[i][k]
    
    return det

##laplace
def determinant(matrix):
    dimension = len(matrix)
    
    if dimension == 1:
        return matrix[0][0]
    if dimension == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    zero_counts_rows = [row.count(0) for row in matrix]
    zero_counts_cols = [sum(row[i] == 0 for row in matrix) for i in range(dimension)]
    
    if max(zero_counts_rows) >= max(zero_counts_cols):
        use_row = True
        index = zero_counts_rows.index(max(zero_counts_rows))
    else:
        use_row = False
        index = zero_counts_cols.index(max(zero_counts_cols))

    det = 0
    for i in range(dimension):
        if use_row:
            if matrix[index][i] == 0:
                continue
            sub_matrix = [row[:i] + row[i+1:] for row in (matrix[:index] + matrix[index+1:])]
            sign = (-1) ** (index + i)
            sub_det = determinant(sub_matrix)
            det += sign * matrix[index][i] * sub_det
        else:
            if matrix[i][index] == 0:
                continue
            sub_matrix = [row[:index] + row[index+1:] for row in (matrix[:i] + matrix[i+1:])]
            sign = (-1) ** (i + index)
            sub_det = determinant(sub_matrix)
            det += sign * matrix[i][index] * sub_det

    return det
##ommid rezaei
def delete_11(matrix):
    A=matrix
    A = A[1:]
    A = [row[1:] for row in A]
    return(A)

def delete_1n(matrix):
    A=matrix
    A = A[1:]
    A = [row[:-1] for row in A]
    return(A)

def delete_n1(matrix):
    A=matrix
    A = A[:-1]
    A = [row[1:] for row in A]
    return(A)

def delete_nn(matrix):
    A=matrix
    A = A[:-1]
    A = [row[:-1] for row in A]
    return(A)

def delete_11_nn(matrix):
    A=matrix
    A = A[:-1]
    A = A[1:]
    A = [row[:-1] for row in A]
    A = [row[1:] for row in A]
    return(A)

def det_omidfar(matrix):
  if len(matrix)==1:
      return matrix[0][0]
  if len(matrix)==2:
      return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
  
  
  m11 =det_omidfar(delete_11(matrix)) 
  m1n=det_omidfar(delete_1n(matrix))
  mn1=det_omidfar(delete_n1(matrix))
  mnn=det_omidfar(delete_nn(matrix))
  m11_nn=det_omidfar(delete_11_nn(matrix))
  if m11_nn==0:
      messagebox.showinfo("error", "determmina is NAN")
      raise ValueError("determmina is NAN")

  return ((m11*mnn - m1n*mn1)/m11_nn)

##hill cipher
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
        messagebox.showinfo("error", "Key must contain only alphabetic characters (A-Z or a-z)")
        raise ValueError("Key must contain only alphabetic characters (A-Z or a-z)")
    dim = round(math.sqrt(len(text)))
    if(dim!=math.sqrt(len(text))):
        messagebox.showinfo("error", "The length of the Key should be the square of a number")
        raise ValueError("The length of the Key should be the square of a number")
    key = [[0 for i in range(dim)] for j in range(dim)]
    text = text.replace(" ", "").upper()
    for i in range(dim*dim):
        key[i//dim][i%dim] = (ord(text[i]) - first_character)% num_of_characters

    det = round(determinant(key))
    if (is_key_valid(det)==False):
        messagebox.showinfo("error", "Key must be invertible")
        raise ValueError("Key must be invertible")
    return key

def encrypt(text, key_text):
    text,key=initialize(text,key_text)
    if not text.isalpha():
        messagebox.showinfo("error","Input must contain only alphabetic characters (A-Z or a-z)")
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
        messagebox.showinfo("error", "The key matrix is not invertible modulo 26")
        raise ValueError("The key matrix is not invertible modulo 26")
    
    cofactor_matrix = matrix_cofactor(key)
    adj_matrix = transpose(cofactor_matrix)
    
    inv_key = [[(det_inv * adj_matrix[i][j]) % num_of_characters for j in range(len(key))] for i in range(len(key))]
    
    return inv_key

def validate_decryption_input(text):
    for char in text:
        if not char.isalpha() and char != '@':
            messagebox.showinfo("error",f"Invalid character '{char}' found. Only alphabetic characters and '@' are allowed.")
            raise ValueError(f"Invalid character '{char}' found. Only alphabetic characters and '@' are allowed.")
        
def decrypt(text,key_text):
    text,key=initialize(text,key_text)
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

def initialize(text,key_text):
    text=text.upper().replace(" ", "")
    key = generate_key(key_text)
    return text,key



##gui
def encrypt_decrypt():
    key = key_entry.get()
    text = text_entry.get("1.0", "end-1c")
    mode = mode_var.get()
    if mode == "Encryption":
        if key=="" or text=="":
            messagebox.showinfo("error", "enter text and key")
        else:
            for widget in window.winfo_children():
                if isinstance(widget, tk.Label) and(widget != key_label and widget != text_label and widget !=a and widget !=b and widget !=c and widget !=d):
                    widget.destroy()
            tk.Label(window, text="", fg="white",pady=1).pack()
            tk.Label(window, text="decryption text:",  fg="black", font="Times 15  bold",padx=20,pady=1).pack()
            tk.Label(window, text=encrypt(text,key),  fg="black", font="Times 15  bold",padx=195,pady=1).pack()
    else:
        if key=="" or text=="":
            messagebox.showinfo("error", "enter text and key")
        else:
            for widget in window.winfo_children():
                if isinstance(widget, tk.Label) and(widget != key_label and widget != text_label and widget !=a and widget !=b and widget !=c and widget !=d):
                    widget.destroy()
            tk.Label(window, text="", fg="white",pady=1).pack()
            tk.Label(window, text="encryption text:",  fg="black", font="Times 15  bold",padx=195,pady=5).pack()
            tk.Label(window, text=decrypt(text,key),  fg="black", font="Times 15  bold",padx=195,pady=5).pack()




window.title("Encryption/Decryption Tool")
window.geometry('600x650')
window.resizable(0, 0)
window.title(' ENCRIPTTION APP')
a=tk.Label(window, text=" ", fg="white",pady=1)
a.pack()
key_label = tk.Label(window, text="key:", background="black", fg="white", font="Times 15  bold",padx=200,pady=5)
key_label.pack()
b=tk.Label(window, text=" ", fg="white")
b.pack()

key_entry = tk.Entry(window,width=55,border=2,highlightcolor="blue",font="Times")
key_entry.pack()
c=tk.Label(window, text="", fg="white",pady=1)
c.pack()
text_label = tk.Label(window, text="Text:", background="black", fg="white", font="Times 15  bold",padx=195,pady=5)
text_label.pack()
d=tk.Label(window, text=" ", fg="white",pady=1)
d.pack()

text_entry = tk.Text(window, height=5, width=55,font="Times")
text_entry.pack()

mode_var = tk.StringVar(value="Encryption")
mode_radio_encryption = tk.Radiobutton(window, text="Encryption", variable=mode_var, value="Encryption",pady=10,font="Times")
mode_radio_encryption.pack()
mode_radio_decryption = tk.Radiobutton(window, text="Decryption", variable=mode_var, value="Decryption",pady=2,font="Times")
mode_radio_decryption.pack()

submit_button =tk.Button(window, text="Submit",bg="yellow",fg="black",command=encrypt_decrypt,font="Times 12  bold",padx=195)
submit_button.pack()

window.mainloop()