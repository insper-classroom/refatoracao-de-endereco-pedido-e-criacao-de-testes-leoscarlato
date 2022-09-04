#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re




class Pedido:
    EM_ABERTO = 1
    PAGO = 2

    def __init__ (self, pessoa:PessoaFisica, produtos:Carrinho, endereco_entrega:Endereco = None):
        self.pessoa = pessoa
        self.produtos = produtos
        self.endereco_entrega = endereco_entrega

    def __str__ (self):
        return f'{self.pessoa} {self.produtos} {self.endereco_entrega}'


