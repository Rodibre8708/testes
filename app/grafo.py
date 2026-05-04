class Grafo:
    def __init__(self):
        # Guarda quem se conecta com quem
        self.adjacencias = {}

    def adicionar_vertice(self, vertice):
        if vertice in self.adjacencias:
            raise ValueError(f"O vértice '{vertice}' já existe no grafo.")
        self.adjacencias[vertice] = []

    def adicionar_aresta(self, origem, destino):
        # Só cria a aresta se os dois nós já existirem no grafo
        if origem not in self.adjacencias or destino not in self.adjacencias:
            raise KeyError("Ambos os vértices precisam existir antes de criar uma aresta.")
        
        # Evita criar a mesma aresta duas vezes
        if destino in self.adjacencias[origem]:
            raise ValueError("Essa aresta já existe.")
            
        self.adjacencias[origem].append(destino)

    def existe_caminho(self, inicio, fim):
        # Dá erro logo de cara se tentarem buscar um nó fantasma
        if inicio not in self.adjacencias or fim not in self.adjacencias:
            raise KeyError("Vértices de início ou fim são inválidos.")

        visitados = set()
        # TODO: Mudar essa fila pra collections.deque depois. Usar pop(0) numa lista é O(N) e vai dar gargalo em grafos grandes.
        fila = [inicio] 

        while fila:
            atual = fila.pop(0)
            
            if atual == fim:
                return True
                
            visitados.add(atual)
            
            # Coloca os vizinhos na fila pra continuar a busca (padrão BFS)
            for vizinho in self.adjacencias[atual]:
                if vizinho not in visitados and vizinho not in fila:
                    fila.append(vizinho)
                    
        return False