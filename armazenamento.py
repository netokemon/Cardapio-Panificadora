import pandas as pd
import tkinter as tk
from tkinter import messagebox

caminhoArquivo = "cardapio.csv"

def novoProduto(produto):
    dfProduto = pd.DataFrame([produto])
    dfProduto.to_csv(caminhoArquivo, mode="a", header= False, index=False, encoding="utf-8")


def atualizarProduto(nomeProduto, selecaoMudanca, novoValor):
    dfCardapio = pd.read_csv(caminhoArquivo)
    if dfCardapio[dfCardapio['Item'] == nomeProduto].empty:
        messagebox.showerror("erro", "Produto não existe")
        return
    else:
        if selecaoMudanca == 1:
            mudarValor(nomeProduto, novoValor)
            return
        elif selecaoMudanca == 2:
            mudarCategoria(nomeProduto, novoValor)
            return
        
def mudarValor(nomeProduto, novoValor):
    dfCardapio = pd.read_csv(caminhoArquivo)
    dfCardapio.loc[dfCardapio['Item'] == nomeProduto, 'Valor'] = novoValor
    dfCardapio.to_csv(caminhoArquivo, index=False)

def mudarCategoria(nomeProduto, novoValor):
    dfCardapio = pd.read_csv(caminhoArquivo)
    dfCardapio.loc[dfCardapio['Item'] == nomeProduto, 'Categoria'] = novoValor
    dfCardapio.to_csv(caminhoArquivo, index=False)

def deletarProduto(nomeProduto):
    dfCardapio = pd.read_csv(caminhoArquivo)
    if dfCardapio[dfCardapio['Item'] == nomeProduto].empty:
        messagebox.showerror("erro", "Produto não existe")
        return
    else:
        dfCardapio = dfCardapio[dfCardapio['Item'] != nomeProduto]
        dfCardapio.to_csv(caminhoArquivo, index=False)
