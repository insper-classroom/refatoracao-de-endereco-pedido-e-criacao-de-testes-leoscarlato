#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------


class Produto:

    lista_produtos = []


    def __init__(self, id_produto, nome=''):
        self.__id = id_produto
        self.__nome = nome
        Produto.lista_produtos.append(self)

    def set_id(self, id_novo):
        self.__id = id_novo

    def get_id(self):
        return self.__id

    def nome(self, nome_novo):
        self.nome = nome_novo

    def buscar_nome(produto):
        for prod in Produto.lista_produtos:
            if produto in prod.nome.lower():
                return [prod.nome]


    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome[0] != 'T':
            self.__nome = novo_nome

    def to_dict(self):
        return {'id': self.__id, 'nome': self.__nome}

    @nome.getter
    def nome(self):
        return self.__nome



