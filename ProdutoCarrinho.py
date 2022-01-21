from ProdutoEstoque import ProdutoEstoque

class ProdutoCarrinho():                     
    nome: str
    quantidade: int

    def __init__(self, nome, qtd):
        self.nome = nome
        self.quantidade = qtd

    def nomeProduto(self, nome):
        self.nome = nome
        print("Qual produto deseja:", nome)

    def atualizaQuantidade(self, qtd):                 # atualizar a quantidade do "Produto" e printa na tela 
        self.quantidade = qtd
        print("nova quantidade:", qtd)

    def setQuantidade(self, qtd):                                 #definir a quantidade 
        self.quantidade = qtd

    def setNome(self,nome):
        self.nome = nome

    def getQuantidade(self):                                        #pegar essa quantidade 
        return self.quantidade

    def getNome(self):                                                   #pegar esse nome
        return self.nome


