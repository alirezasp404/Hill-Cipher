import tkinter as tk
from tkinter import messagebox
import hill_cipher  

window = tk.Tk()
answer_lable=None

def encrypt_decrypt():
    key = key_entry.get()
    text = text_entry.get("1.0", "end-1c")
    mode = mode_var.get()
    global answer_lable
    if mode == "Encryption":
        if key=="" or text=="":
            messagebox.showinfo("error", "enter text and key")
        else:
            for widget in window.winfo_children():
                if isinstance(widget, tk.Label) and(widget != key_label and widget != text_label and widget !=a and widget !=b and widget !=c and widget !=d):
                    widget.destroy()
            tk.Label(window, text="", fg="white",pady=1).pack()
            tk.Label(window, text="decryption text:",  fg="black", font="Times 15  bold",padx=20,pady=1).pack()
            tk.Label(window, text=hill_cipher.encrypt(text,key),  fg="black", font="Times 15  bold",padx=195,pady=1).pack()
    else:
        if key=="" or text=="":
            messagebox.showinfo("error", "enter text and key")
        else:
            for widget in window.winfo_children():
                if isinstance(widget, tk.Label) and(widget != key_label and widget != text_label and widget !=a and widget !=b and widget !=c and widget !=d):
                    widget.destroy()
            tk.Label(window, text="", fg="white",pady=1).pack()
            tk.Label(window, text="encryption text:",  fg="black", font="Times 15  bold",padx=195,pady=5).pack()
            tk.Label(window, text=hill_cipher.decrypt(text,key),  fg="black", font="Times 15  bold",padx=195,pady=5).pack()




##GUI
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