from produto import Produto

class ProdutoPromocional(Produto):
    def __init__(self, produto):
        self._produto = produto

    def definePrecoVenda(self):
        self._produto._promocao = True
        self._produto._precoDeCompra = self._produto._preco_original
        self._produto._precoDeCompra -= self._produto._precoDeCompra * 0.20
        self._produto._quantidadeEstoque -= 1
        self._produto_historico.append(f'Compra de 1 {self._nome} com desconto de 20% por R${self._produto._precoDeCompra}')
        return self._produto._precoDeCompra