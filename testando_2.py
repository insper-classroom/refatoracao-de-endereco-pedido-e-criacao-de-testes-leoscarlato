#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.Carrinho import Carrinho
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento



import copy


# Criando uma pessoa 
pessoa1 = PessoaFisica('122-832-988-01', 'jose@email.com', 'José')
print(pessoa1)


# Criando  um endereço
end1 = Endereco('04546041', 222)
print(end1)


# Cria um outro endereço
end2 = Endereco('17560246', 1620)
print(end2)


# Adiciona endereço à pessoa
pessoa1.adicionar_endereco('casa', end1)

print("Endereços da pessoa")
pessoa1.listar_enderecos()

pessoa1.adicionar_endereco('trabalho', end2)
print("Endereços da pessoa após inclusão")
pessoa1.listar_enderecos()

# Criando um produto
sabonete = Produto("0012342362", "Shampoo")


pessoas = PessoaFisica.buscar_nome('José')
if len(pessoas) > 0:
    pessoa = pessoas[0]  #Pega a primeira pessoa
print(pessoas)



produtos = Produto.buscar_nome("sham")

if len(produtos) > 0: 
    produto = produtos[0]

print(produtos)



carrinho = Carrinho()
carrinho.adicionar_item(sabonete, 2)
print(carrinho)


pedido = Pedido(pessoas, carrinho)

ends = (pessoa1.listar_enderecos())


if len(ends) > 0:
    endereco = ends[0]

# Lembre-se de adicionar estes atributos ao endereço
pedido.endereco_entrega = copy.deepcopy(endereco) 
pedido.endereco_faturamento = copy.deepcopy(endereco)


pag = Pagamento(pedido)
pag.processa_pagamento()
if pag.pagamento_aprovado:
    pedido.status = Pedido.PAGO 

print("Pedido aguardando coleta")

## Pedido deve imprir todos os detalhes da compra - pessoa, endereço e produtos
print(pedido)



