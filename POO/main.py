from encapsulamento import BaseDeDados

bd = BaseDeDados()

bd.inserir_cliente(123, 'Yago')
bd.inserir_cliente(1234, 'Diego')
bd.apagar_cliente(1234)
bd.listar_clientes()




