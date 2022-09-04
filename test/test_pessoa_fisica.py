from classes.Carrinho import *
from classes.Produto import *
from classes.Pagamentos import *
from classes.Pedido import *
from classes.PessoaFisica import *
import pytest

@pytest.mark.adicionar_e_listar_endereco
def test_adicionar_e_listar_endereco():
    pessoa1 = PessoaFisica('524.222.452-6', 'tiago@email.com', 'Carlos')
    end1 = Endereco('08320330', 430)

    pessoa1.adicionar_endereco('casa', end1)

    assert pessoa1.listar_enderecos() == ['casa']


@pytest.mark.remover_endereco
def test_remover_endereco():
    pessoa1 = PessoaFisica('524.222.452-6', 'tiago@email.com', 'Carlos')
    end1 = Endereco('08320330', 430)

    pessoa1.adicionar_endereco('casa', end1)

    pessoa1.remover_endereco('casa')

    assert pessoa1.listar_enderecos() == []


@pytest.mark.buscar_nome
def test_buscar_nome():
    nome = 'Carlos'

    for cliente in PessoaFisica.lista_clientes:
        if nome == cliente.lower():
            assert nome == cliente.lower()
