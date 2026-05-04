import pytest
from app.grafo import Grafo

# Fixtures pra não ter que instanciar o grafo do zero em todo teste
@pytest.fixture
def grafo_vazio():
    return Grafo()

@pytest.fixture
def grafo_com_dados():
    g = Grafo()
    for v in ["A", "B", "C", "D"]:
        g.adicionar_vertice(v)
    
    # A estrutura fica: A -> B -> C (e o D fica isolado)
    g.adicionar_aresta("A", "B")
    g.adicionar_aresta("B", "C")
    return g

#  Testes que devem passar direto 

def test_adicionar_vertice_sucesso(grafo_vazio):
    grafo_vazio.adicionar_vertice("A")
    assert "A" in grafo_vazio.adjacencias

def test_existe_caminho_verdadeiro(grafo_com_dados):
    assert grafo_com_dados.existe_caminho("A", "C") is True

def test_existe_caminho_falso(grafo_com_dados):
    assert grafo_com_dados.existe_caminho("A", "D") is False

#  Testes de erros e validações 

def test_adicionar_vertice_duplicado(grafo_vazio):
    grafo_vazio.adicionar_vertice("A")
    with pytest.raises(ValueError, match="já existe no grafo"):
        grafo_vazio.adicionar_vertice("A")

def test_adicionar_aresta_vertice_inexistente(grafo_vazio):
    grafo_vazio.adicionar_vertice("A")
    with pytest.raises(KeyError, match="precisam existir antes"):
        grafo_vazio.adicionar_aresta("A", "Z")

def test_adicionar_aresta_duplicada(grafo_vazio):
    # cobrir a linha de erro no pytest-cov e bater os 100% 
    grafo_vazio.adicionar_vertice("A")
    grafo_vazio.adicionar_vertice("B")
    grafo_vazio.adicionar_aresta("A", "B")
    
    with pytest.raises(ValueError, match="Essa aresta já existe."):
        grafo_vazio.adicionar_aresta("A", "B")

def test_busca_com_vertice_invalido(grafo_com_dados):
    with pytest.raises(KeyError, match="inválidos"):
        grafo_com_dados.existe_caminho("A", "X")