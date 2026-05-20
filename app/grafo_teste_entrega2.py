import unittest
from grafo import Grafo

class TestIntegracaoGrafo(unittest.TestCase):

    def setUp(self):
        """Inicializa um novo grafo para cada teste."""
        self.grafo = Grafo()

    def test_fluxo_criacao_e_busca_caminho_sucesso(self):
        """Teste de integração: Criar estrutura complexa e validar caminho."""
        # Adicionando múltiplos vértices
        vertices = ["A", "B", "C", "D", "E"]
        for v in vertices:
            self.grafo.adicionar_vertice(v)

        # Criando conexões (arestas) que formam um caminho de A até E
        # A -> B -> D -> E
        self.grafo.adicionar_aresta("A", "B")
        self.grafo.adicionar_aresta("B", "D")
        self.grafo.adicionar_aresta("C", "A") # C aponta para A
        self.grafo.adicionar_aresta("D", "E")

        # Valida se o sistema integra a estrutura de dados com o algoritmo BFS
        self.assertTrue(self.grafo.existe_caminho("A", "E"))
        self.assertTrue(self.grafo.existe_caminho("C", "E"))
        self.assertFalse(self.grafo.existe_caminho("E", "A")) # Caminho direcionado não existe

    def test_integracao_falha_por_vertice_inexistente(self):
        """Valida a comunicação entre a validação de existência e a busca."""
        self.grafo.adicionar_vertice("A")
        
        # Tenta buscar caminho para um vértice que não foi integrado ao grafo
        with self.assertRaises(KeyError):
            self.grafo.existe_caminho("A", "B")

    def test_fluxo_grafo_ciclico(self):
        """Valida se o algoritmo lida corretamente com ciclos integrados."""
        self.grafo.adicionar_vertice("A")
        self.grafo.adicionar_vertice("B")
        self.grafo.adicionar_aresta("A", "B")
        self.grafo.adicionar_aresta("B", "A") # Ciclo

        self.assertTrue(self.grafo.existe_caminho("A", "B"))
        self.assertTrue(self.grafo.existe_caminho("B", "A"))

if __name__ == "__main__":
    unittest.main()