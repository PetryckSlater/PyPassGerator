import tkinter as tk
from tkinter import ttk
import string
import secrets
import csv
from datetime import datetime

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("No characters selected for password generation")

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate():
    try:
        length = int(length_entry.get())
        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        result_label.config(text=password)
        save_password(password)
    except ValueError:
        result_label.config(text="Por favor, insira um número válido.")

def copy_to_clipboard():
    password = result_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(password)

def save_password(password):
    name = name_entry.get()
    with open('generated_passwords.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([password, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), name])

# Criando a janela principal
root = tk.Tk()
root.title("Gerador de Senhas")

# Comprimento da senha
ttk.Label(root, text="Comprimento da senha:").grid(column=0, row=0, padx=10, pady=10)
length_entry = ttk.Entry(root)
length_entry.grid(column=1, row=0, padx=10, pady=10)
length_entry.insert(0, "12")

# Nome da senha
ttk.Label(root, text="Nome da senha:").grid(column=0, row=1, padx=10, pady=10)
name_entry = ttk.Entry(root)
name_entry.grid(column=1, row=1, padx=10, pady=10)

# Opções de caracteres
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

ttk.Checkbutton(root, text="Incluir letras maiúsculas", variable=upper_var).grid(column=0, row=2, padx=10, pady=5)
ttk.Checkbutton(root, text="Incluir letras minúsculas", variable=lower_var).grid(column=1, row=2, padx=10, pady=5)
ttk.Checkbutton(root, text="Incluir dígitos", variable=digits_var).grid(column=0, row=3, padx=10, pady=5)
ttk.Checkbutton(root, text="Incluir caracteres especiais", variable=special_var).grid(column=1, row=3, padx=10, pady=5)

# Botão para gerar a senha
generate_button = ttk.Button(root, text="Gerar Senha", command=generate)
generate_button.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Rótulo para exibir a senha gerada
result_label = ttk.Label(root, text="", font=("TkDefaultFont", 12))
result_label.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

# Botão para copiar a senha
copy_button = ttk.Button(root, text="Copiar Senha", command=copy_to_clipboard)
copy_button.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

# Executando a aplicação
root.mainloop()
