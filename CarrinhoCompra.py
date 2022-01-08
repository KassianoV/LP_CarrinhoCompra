from EstoqueProduto import EstoqueProduto
from ProdutoEstoque import ProdutoEstoque
from ProdutoCarrinho import ProdutoCarrinho

class CarrinhoCompra:
    Carrinho = []
    def __init__(self, estq):
        self.estoque = estq
    
    def adicionarItem(self, nome, qtd):
        produto = self.estoque.getProduto(nome)
        self.Carrinho.append(ProdutoCarrinho(nome, produto.getPreco(), qtd))

    def FinalizarCompra(self):
        for prodCarrinho in self.Carrinho:
            for prodEstoque in self.estoque.getListaProdutos():
                if prodEstoque.getNome() == prodCarrinho.getNome():
                    prodEstoque.atualizaQuantidade(-prodCarrinho.getQuantidade())

    def ValorTotal(self):
        total = 0
        for produto in self.Carrinho:
            total += produto.getPreco() * produto.getQuantidade
        return total