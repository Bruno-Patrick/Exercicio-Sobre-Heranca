class Promocao:
    def __init__(self, produto):
        self._produto = produto

    def definir_promocao(self, promocao):
        self._produto.set_precoOriginal()
        preco = self._produto.get_preco()
        preco = preco - (preco*(promocao/100))
        self._produto.set_boolean(True)
        return self._produto.definePrecoVenda(preco)