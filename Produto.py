class Produto():                                                    #criei a classe produto com suas caracteristicas 
    nome: str
    preco: float
    quantidade: int

    def __init__(self, nome, val, qtd):
        self.nome = nome
        self.preco = val
        self.quantidade = qtd

    def atualizaQuantidade(self, qtd):                 # atualizar a quantidade do "Produto" e printa na tela 
        self.quantidade = qtd
        print("nova quantidade:", qtd)

    def setQuantidade(self, qtd):                                 #definir a quantidade 
        self.quantidade = qtd
    
    def setPreco(self, val):                                            #definir o preço
        self.preco = val
    
    def getQuantidade(self):                                        #pegar essa quantidade 
        return self.quantidade

    def getNome(self):                                                   #pegar esse nome
        return self.nome

    def getPreco(self):                                                    #pegar esse preço
        return self.preco
