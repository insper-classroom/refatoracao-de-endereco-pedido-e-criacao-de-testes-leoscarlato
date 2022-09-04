#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
import re


class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''

    lista_clientes = []
    enderecos = []

    def __init__(self, cpf, email, nome='Visitante'):
        PessoaFisica.lista_clientes.append(self)
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.__enderecos = {}

    # escolher o estilo de retorno

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        self.__enderecos[apelido_endereco] = end

    def remover_endereco(self, apelido_endereco):
        del(self.__enderecos[apelido_endereco])

    def get_endereco(self, apelido_endereco):
        return self.__enderecos[apelido_endereco]

    def listar_enderecos(self):
        enderecos = []
        for endereco in self.__enderecos:
            print(endereco)
            enderecos.append(endereco)
        return enderecos
            

    def buscar_nome(buscar):
        for pessoa in PessoaFisica.lista_clientes:
            if buscar in pessoa.nome:
                return [pessoa.nome]


    def __str__ (self):
        return f'{self.nome}, {self.email}, {self.cpf}'

     

    