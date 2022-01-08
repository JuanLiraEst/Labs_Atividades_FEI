from tkinter import * 
from tkinter import scrolledtext

arquivo = open("chat.txt", "r", encoding="utf-8")
textao = arquivo.readlines()

janela = Tk()
janela.title("Filttro de Palavras")
janela.geometry("500x500")

txt = scrolledtext.ScrolledText(janela, width=50, height=50)
txt.place(relx=0.5, rely=0.5, anchor=CENTER)

for i in range(0,100):
    txt.insert(END, i)

janela.mainloop()