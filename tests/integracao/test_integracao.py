import pytest
from app.grafo import Grafo

@pytest.fixture
def grafo():
    return Grafo()

def test_fluxo_criacao_e_busca_caminho_sucesso(grafo):
    # Montando um grafo mais complexo pra testar a integração das funções
    vertices = ["A", "B", "C", "D", "E"]
    for v in vertices:
        grafo.adicionar_vertice(v)

    # A ideia é forçar o caminho: A -> B -> D -> E (e o C aponta pro A)
    grafo.adicionar_aresta("A", "B")
    grafo.adicionar_aresta("B", "D")
    grafo.adicionar_aresta("C", "A") 
    grafo.adicionar_aresta("D", "E")

    # Vendo se a busca consegue se achar nesse emaranhado
    assert grafo.existe_caminho("A", "E") is True
    assert grafo.existe_caminho("C", "E") is True
    
    # O caminho de volta não pode rolar porque o grafo é direcionado
    assert grafo.existe_caminho("E", "A") is False 

def test_integracao_falha_por_vertice_inexistente(grafo):
    grafo.adicionar_vertice("A")
    
    # Forçando erro ao tentar buscar um caminho com um vértice que a gente esqueceu de integrar
    with pytest.raises(KeyError):
        grafo.existe_caminho("A", "B")

def test_fluxo_grafo_ciclico(grafo):
    # Testando loop infinito. O set de 'visitados' no nosso while tem que segurar a onda aqui.
    grafo.adicionar_vertice("A")
    grafo.adicionar_vertice("B")
    grafo.adicionar_aresta("A", "B")
    grafo.adicionar_aresta("B", "A") # Virou um ciclo fechado A <-> B

    assert grafo.existe_caminho("A", "B") is True
    assert grafo.existe_caminho("B", "A") is True