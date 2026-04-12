class Grafo:
    def __init__(self):
        self.adjacencias = {}

    def adicionar_vertice(self, vertice):
        if vertice in self.adjacencias:
            raise ValueError(f"O vértice '{vertice}' já existe no grafo.")
        self.adjacencias[vertice] = []

    def adicionar_aresta(self, origem, destino):
        if origem not in self.adjacencias or destino not in self.adjacencias:
            raise KeyError("Ambos os vértices precisam existir antes de criar uma aresta.")
        
        if destino in self.adjacencias[origem]:
            raise ValueError("Essa aresta já existe.")
            
        self.adjacencias[origem].append(destino)

    def existe_caminho(self, inicio, fim):
        """Verifica se há um caminho usando Busca em Largura (BFS)."""
        if inicio not in self.adjacencias or fim not in self.adjacencias:
            raise KeyError("Vértices de início ou fim são inválidos.")

        visitados = set()
        fila = [inicio] 

        while fila:
            atual = fila.pop(0)
            
            if atual == fim:
                return True
                
            visitados.add(atual)
            
            for vizinho in self.adjacencias[atual]:
                if vizinho not in visitados and vizinho not in fila:
                    fila.append(vizinho)
                    
        return False