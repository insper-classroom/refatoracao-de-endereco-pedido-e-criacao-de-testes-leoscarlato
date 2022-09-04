from classes.Carrinho import *
from classes.Produto import *
from classes.Pagamentos import *
from classes.Pedido import *
from classes.PessoaFisica import *
import pytest

@pytest.mark.busca_nome
def test_busca_nome():
    produto = 'sabon'

    for prod in Produto.lista_produtos:
        if produto == prod.lower():
            assert produto == prod.lower()




