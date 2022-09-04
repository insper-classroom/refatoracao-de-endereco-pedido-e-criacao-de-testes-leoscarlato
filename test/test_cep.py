import pytest
from classes.Endereco import *

@pytest.mark.cep
def test_cep_e_numero_residencia():
    cep = '08320330'
    numero = 430
    adress = Endereco(cep, numero).__str__()
    
    assert Endereco('08320330', 430).__str__() == adress



@pytest.mark.verifica_cep
def test_verifica_cep():
    cep = '08320330'
    assert True == isinstance(cep, (int, str))


@pytest.mark.consulta_cep
def test_consulta_cep():

    # pytest.raises(requests.exceptions.JSONDecodeError)

    assert Endereco.consultar_cep('99999999', 120) == False



@pytest.mark.verifica_rede
def test_verifica_rede():
    with pytest.raises(requests.exceptions.ConnectionError) as internet_error:
        Endereco.consultar_cep('083203300', 120)

    assert 'ConnectionError' in str(internet_error.value)
