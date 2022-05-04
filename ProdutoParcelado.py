from produto import Produto


class ProdutoParcelado(Produto):
    def __init__(self, produto):
        self._produto = produto

    def definePrecoVenda(self):
        self._produto.set_precoOriginal()
        juros = self._produto.get_preco()*0.05
        preco = self._produto.get_preco() + juros
        return self._produto.definePrecoVenda(preco)