from classes.Carrinho import *
from classes.Produto import *
from classes.Pagamentos import *
from classes.Pedido import *
from classes.PessoaFisica import *
import pytest, copy

@pytest.mark.pedido_final
def test_pedido_final():

    #Dados do cliente

    pessoa = PessoaFisica('524.222.452-6', 'tiago@email.com', 'Carlos')
    cliente = PessoaFisica.buscar_nome('Carlos')
    endereco = Endereco('08320330', 430)
    pessoa.adicionar_endereco('casa', endereco)

    ends = (pessoa.listar_enderecos())


    if len(ends) > 0:
        endereco = ends[0]

    #Pedido

    carrinho = Carrinho()
    sabonete = Produto("0010342967", "Sabonete")
    carrinho.adicionar_item(sabonete, 2)

    #Finalizando o pedido

    pedido = Pedido(cliente, carrinho)
    pedido.endereco_entrega = copy.deepcopy(endereco)

    assert Pedido.__str__(pedido) == "['Carlos'] {'0010342967': 2} casa"