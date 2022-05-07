class Promocao:
    def __init__(self, produto):
        self._produto = produto

    def definir_promocao(self):
        self._produto._promocao = True
        self._produto._precoDeCompra = self._produto._preco_original
        self._produto._precoDeCompra = self._produto._precoDeCompra * 0.5
        self._produto._quantidadeEstoque -= 1
        self._produto_historico.append(f'Compra de 1 {self._nome} com desconto de 50% por R${self._produto._precoDeCompra}')