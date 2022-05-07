class Produto:
    def __init__(self, nome = "", precoDeCompra = 0, quantidadeEstoque = 0, promocao = 0):
        self._nome = nome
        self._precoDeCompra = precoDeCompra
        self._quantidadeEstoque = quantidadeEstoque
        self._promocao = promocao
        self._preco_original = precoDeCompra
        self._historico = []

    def extrato(self):
        return print(f"{self._nome} | {self._precoDeCompra} | {self._quantidadeEstoque} | {self._promocao} \n")

    # def atualizaQuantidade(self, valor):
    #     self._quantidadeEstoque = valor

    def definePrecoVenda(self, valor):
        self._precoDeCompra = valor

    # def set_precoOriginal(self):
    #     self._precoDeCompra = self._preco_original

    # def get_preco(self):
    #     return self._precoDeCompra
    
    # def set_boolean(self, boolean):
    #     self._promocao = boolean

    def vendeProduto(self, valor):
        if (valor < self._precoDeCompra) or (self._quantidadeEstoque <= 0):
            return print("A quantia é insuficiente ou não há estoque disponivel! \n")
        else:
            self._quantidadeEstoque -= 1
            self._historico.append(f'Venda de 1 {self._nome} por R${valor}')
            return print("Venda efetuada com sucesso! \n")

    def compraProduto(self, valor):
        if valor < self._precoDeCompra:
            return print("A quantia é insuficiente! \n")
        else:
            self._quantidadeEstoque += 1
            self._historico.append(f'Compra de 1 {self._nome} por R${valor}')
            return print("Compra efetuada com sucesso! \n")
