from classes.Carrinho import *
from classes.Produto import *
from classes.Pagamentos import *
from classes.Pedido import *
from classes.PessoaFisica import *
import pytest

@pytest.mark.adicionar_item
def test_adicionar_item():

    sabonete = Produto("0010342967", "Sabonete")
    carrinho = Carrinho()

    carrinho.adicionar_item(sabonete, 2)

    if (Carrinho.__str__(carrinho)) != {}:   # se o dicionário existir após a adição do item no carrinho, o teste irá passar.
        assert True == True





@pytest.mark.remover_item
def test_remover_item():

    sabonete = Produto("0010342967", "Sabonete")
    carrinho = Carrinho()

    carrinho.adicionar_item(sabonete, 2)
    
    if (Carrinho.__str__(carrinho)) != {}:
        carrinho.remover_item("0010342967")
        if Carrinho.__str__(carrinho) == {}:   # confirma se o item foi realmente removido do pedido
            assert True == True








    
