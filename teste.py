from produto import Produto
from ProdutoParcelado import ProdutoParcelado
from ProdutoPromocional import ProdutoPromocional
from promocao import Promocao

banana = Produto('banana',10,10,False)
banana.compraProduto(3)
banana.compraProduto(4)
banana.vendeProduto(3)
banana.vendeProduto(4)
banana.extrato()
banana.atualizaQuantidade(25)
banana.extrato()
banana.atualizaQuantidade(0)
banana.vendeProduto(4)
banana.extrato()

banana_promocao = ProdutoPromocional(banana)
banana_promocao.definePrecoVenda()
banana.extrato()
banana_parcelado = ProdutoParcelado(banana)
banana_parcelado.definePrecoVenda()
banana.extrato()

banana_promocao = Promocao(banana)
banana_promocao.definir_promocao(100)
banana.extrato()
banana_promocao.definir_promocao(40)
banana.extrato()

