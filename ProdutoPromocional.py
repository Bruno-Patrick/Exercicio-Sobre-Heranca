from produto import Produto

class ProdutoPromocional(Produto):
    def __init__(self, produto):
        self._produto = produto

    def definePrecoVenda(self):
        self._produto.set_precoOriginal()
        preco = self._produto.get_preco()
        preco = preco - (preco*0.20)
        self._produto.set_boolean(True)
        return self._produto.definePrecoVenda(preco)
        