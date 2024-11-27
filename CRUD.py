from armazenamento import novoProduto, atualizarProduto, deletarProduto

def Create(nome, categoria, valor):

    produto = {
      "categoria": 0, "nome": "a", "valor": 0     
    } 
    
    produto['nome'] = nome
    produto['valor'] = valor
    produto['categoria'] = categoria
  
    novoProduto(produto)



def Update(nome, selecaoDeMudanca, novoValor):
    atualizarProduto(nome, selecaoDeMudanca, novoValor)

    
def Delete(item):
    deletarProduto(item)
