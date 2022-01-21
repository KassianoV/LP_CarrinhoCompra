from ProdutoEstoque import ProdutoEstoque

class EstoqueProduto:
    ListaProdutos = []
    def adicionarProduto(self, produto):            #acrescentar produto ao estoque de produtos 
        self.ListaProdutos.append(produto)
    
    def getProduto(self, nome):                             #definir produto
        for produtos in  self.ListaProdutos:
            if produtos.getNome() == nome:
                return produtos

    def getListaProdutos(self):                              #definir o vetor de produtos 
        return self.ListaProdutos   