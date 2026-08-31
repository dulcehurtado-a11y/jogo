import tkinter as tk
import random

numero_secreto = 0
tentativas = 0
limite = 20

janela = tk.Tk()

janela.title("Jogo de Adivinhação")
janela.geometry("450x500")

titulo = tk.Label(
janela,
text="JOGO DE ADIVINHAÇÃO",
font=("Arial",20)
)

titulo.pack(pady=20)
