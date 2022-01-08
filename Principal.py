from CarrinhoCompra import CarrinhoCompra
from EstoqueProduto import EstoqueProduto
from ProdutoEstoque import ProdutoEstoque

class Principal:
        def executar():
            estoque = EstoqueProduto()
            estoque.adicionarProduto(ProdutoEstoque("monitor", 500, 100))
            estoque.adicionarProduto(ProdutoEstoque("telefone", 150, 300))
            estoque.adicionarProduto(ProdutoEstoque("teclado", 70, 50))
            estoque.adicionarProduto(ProdutoEstoque("mouse", 50, 50))

            carrinho = CarrinhoCompra(estoque)
            carrinho.adicionarItem("monitor", 2)
            carrinho.adicionarItem("telefone", 5)
            carrinho.adicionarItem("teclado",2)

            carrinho.FinalizarCompra()

            print("A soma dos produtos é:", carrinho.ValorTotal())

Principal.executar()