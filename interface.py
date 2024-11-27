import tkinter as tk
import pandas as pd
from tkinter import messagebox
from tkinter import ttk
from CRUD import Create, Update, Delete


def mostrarErroNulo():
    messagebox.showerror("Erro", "Dados vazios ou produto não existe.")


#Salvar dados da janela de cadastro:
def salvarInfo(janela, entradaValor, entradaNome, entradaCategoria):
    nome = entradaNome.get()
    categoria = entradaCategoria.get()
    valor = entradaValor.get()
    if nome and categoria and valor:
        Create(nome, categoria, valor)
        janela.destroy()
        return
    else:
        messagebox.showwarning("Erro", "Preencha todos os dados.")


#Janela secundária para criar produto novo:
def janelaCadastro():
    janelaCadastro = tk.Toplevel()
    janelaCadastro.title("Cadastrar Produto")
    janelaCadastro.geometry("800x600")
    #Area de nome do produto
    tk.Label(janelaCadastro, text="Digite o nome do produto:", font=("Times New Roman", 20)).pack(pady=10)
    entradaNome = tk.Entry(janelaCadastro)
    entradaNome.pack(pady=10)

    tk.Label(janelaCadastro, text="Digite a categoria do produto:", font=("Times New Roman", 20)).pack(pady=10)
    entradaCtg = tk.Entry(janelaCadastro)
    entradaCtg.pack(pady=10)

    tk.Label(janelaCadastro, text="Digite o valor do produto:", font=("Times New Roman", 20)).pack(pady=10)
    entradaValor = tk.Entry(janelaCadastro)
    entradaValor.pack(pady=10)

    #lambda para criar uma função "anonima" que faz com que eu possa passar os parametros do salvarinfo sem ele executar a funcao imediatamente
    tk.Button(janelaCadastro, text = "Cadastrar", command= lambda: salvarInfo(janelaCadastro, entradaValor, entradaNome, entradaCtg)).pack(pady=10)

#Janela de Retrieve (unica que nao vai precisar de nada do codigo CRUD):
def janelaRetrieve():
    df = pd.read_csv("cardapio.csv")
    janelaRetrieve = tk.Toplevel()
    janelaRetrieve.title("Cardápio")
    janelaRetrieve.geometry("800x600")

    tree = ttk.Treeview(janelaRetrieve)
    tree["columns"] =  list(df.columns)
    
    for coluna in df.columns:
        tree.heading(coluna, text=coluna)
        tree.column(coluna, anchor = "center")

    df_linhas = df.to_numpy().tolist()
    for linha in df_linhas:
        tree.insert("", "end", values=linha)

    tree.pack(fill="both", expand=True)

#Janela de atualizar um item já existente:
def janelaUpdate():
    janelaUpdate = tk.Toplevel()
    janelaUpdate.title("Atualizar Produto")
    janelaUpdate.geometry("800x600")
    #Area de nome do produto
    tk.Label(janelaUpdate, text="Digite o nome do produto:", font=("Times New Roman", 20)).pack(pady=10)
    entradaNome = tk.Entry(janelaUpdate)
    entradaNome.pack(pady=10)
    tk.Label(janelaUpdate, text="Digite o novo valor:", font=("Times New Roman", 20)).pack(pady=10)
    entradaValor = tk.Entry(janelaUpdate)
    entradaValor.pack(pady=10)
    tk.Button(janelaUpdate, text = "Atualizar Valor", command= lambda: Update(entradaNome.get(), 1, int(entradaValor.get()))).pack(padx=10,pady=10)
    tk.Button(janelaUpdate, text = "Atualizar Categoria", command= lambda: Update(entradaNome.get(), 2, int(entradaValor.get()))).pack(padx=10,pady=10)

#Janela de Deletar um item:
def janelaDelete():
    janelaDelete = tk.Toplevel()
    janelaDelete.title("Deletar Produto")
    janelaDelete.geometry("800x600")
    #Area de nome do produto
    tk.Label(janelaDelete, text="Digite o nome do produto:", font=("Times New Roman", 20)).pack(pady=10)
    entradaNome = tk.Entry(janelaDelete)
    entradaNome.pack(pady=10)
    tk.Button(janelaDelete, text = "Deletar", command= lambda: Delete(entradaNome.get())).pack(pady=10)
    

#principal do app

principal = tk.Tk()
principal.title("Panificadora Boa Esperança")
principal.geometry("800x600")

#Background meio amarelinho ou marrom sei la

principal.configure(bg="#DEB762")

#Texto nome do produto:

label_produto = tk.Label(principal, bg="#DEB762",text="Panificadora Boa Esperança:", font=("Times New Roman", 24), justify="center")
label_produto.pack(side="top", fill="x")
#label_produto.pack(padx=20, pady=20) //// alguma coisa no canvas nao permite que o texto fique
#na frente dele sem a funcao place e ainda fica meio esquisito mas eh oq temos!
label_produto.config(fg="#F1EBDF")


#Botão de cadastrar produtos
buttonCadastro = tk.Button(principal, command = janelaCadastro, text = "Cadastrar novo Produto", bg="#DEB762", justify = "center", width = 15)
buttonCadastro.pack(pady=20)
#botao retrieve
buttonRetrieve = tk.Button(principal, command = janelaRetrieve, text = "Ver cardápio", bg="#DEB762", justify = "center", width = 15)
buttonRetrieve.pack(pady=20)
#botao atualizar
buttonUpdate = tk.Button(principal, command = janelaUpdate, text = "Atualizar um Produto", bg="#DEB762", justify = "center", width = 15)
buttonUpdate.pack(pady=20)
#botao deletar
buttonDelete = tk.Button(principal, command = janelaDelete, text = "Deletar um Produto", bg="#DEB762", justify = "center", width = 15)
buttonDelete.pack(pady=20)

#Imagem de trigo no bottom:

trigo1 = tk.PhotoImage(file="trigo.png")
labelTrigo1 = tk.Label(principal, image=trigo1, bg="#DEB762")
labelTrigo1.pack(side="bottom")

#Inicia a principal:

principal.mainloop()
