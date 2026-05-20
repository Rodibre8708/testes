import pytest
from app.grafo import Grafo

@pytest.fixture
def grafo():
    return Grafo()

def test_fluxo_criacao_e_busca_caminho_sucesso(grafo):
    vertices = ["A", "B", "C", "D", "E"]
    for v in vertices:
        grafo.adicionar_vertice(v)

    grafo.adicionar_aresta("A", "B")
    grafo.adicionar_aresta("B", "D")
    grafo.adicionar_aresta("C", "A") 
    grafo.adicionar_aresta("D", "E")

    assert grafo.existe_caminho("A", "E") is True
    assert grafo.existe_caminho("C", "E") is True
    assert grafo.existe_caminho("E", "A") is False 

def test_integracao_falha_por_vertice_inexistente(grafo):
    grafo.adicionar_vertice("A")
    
    with pytest.raises(KeyError, match="Vértice inválido"):
        grafo.existe_caminho("A", "B")

def test_fluxo_grafo_ciclico(grafo):
    grafo.adicionar_vertice("A")
    grafo.adicionar_vertice("B")
    grafo.adicionar_aresta("A", "B")
    grafo.adicionar_aresta("B", "A") 

    assert grafo.existe_caminho("A", "B") is True
    assert grafo.existe_caminho("B", "A") is True