from produto import Produto


class ProdutoParcelado(Produto):
    def __init__(self, produto):
        self._produto = produto

    def definePrecoVenda(self, parcelas):
        self._produto._promocao = False
        self._produto._precoDeCompra = self._produto._preco_original
        juros = parcelas * 0.05
        self._produto._precoDeCompra += juros
        self._produto._precoDeCompra = self._produto._precoDeCompra/parcelas
        self._produto._quantidadeEstoque -= 1
        self._produto_historico.append(f'Compra de 1 {self._nome} parcelado em {parcelas}x' +
        'por R${self._produto._precoDeCompra} cada parcela')
        return self._produto._precoDeCompra