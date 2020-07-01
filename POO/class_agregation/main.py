#NA AGREGAÇÃO UMA CLASSE DEPENDE DA OUTRA PARA FUNCIONAR
from classes import Cart, Produto

carrinho = Cart()

p1 = Produto('Camiseta', 50)
p2 = Produto('Tenis', 140)
p3 = Produto('calça', 100)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)

carrinho.lista_produto()

print(carrinho.soma_produto())