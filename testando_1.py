from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.Carrinho import Carrinho
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento

import copy

# Criando um cliente 
pessoa = PessoaFisica('Leonardo', 'leo.scarlato@email.com', '123-390-880-55')
print(pessoa)


# Criando um endereço
end1 = Endereco('04546041', 222)
print(end1)


# Criando um outro endereço
end2 = Endereco('17560246', 1620)
print(end2)


# Adicionando endereço ao cliente
pessoa.adicionar_endereco('Casa', end1)


# Listando os endereços designados ao cliente
print("Endereços da pessoa")
(pessoa.listar_enderecos()) 


# Adicionando um endereço à lista dos endereços designados ao cliente
pessoa.adicionar_endereco('Trabalho', end2)
print("Endereços da pessoa após inclusão")
(pessoa.listar_enderecos())

ends = (pessoa.listar_enderecos())
if len(ends) > 0:
    endereco = ends[0]


# Criando um produto
headset = Produto("0010342967", "Headset")

carrinho = Carrinho()
carrinho.adicionar_item(headset, 2)

pedido = Pedido(pessoa, carrinho)
pedido.endereco_entrega = copy.deepcopy(endereco) 


# Realiza o pagamento
pag = Pagamento(pedido)
pag.processa_pagamento()
if pag.pagamento_aprovado:
    pedido.status = Pedido.PAGO 


# Exibe o pedido
print("Resumo do pedido")
print(pedido)




