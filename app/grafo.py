from collections import deque

class Grafo:
    def __init__(self):
        # Guarda quem se conecta com quem
        self.adjacencias = {}

    def _validar_vertice_existe(self, *vertices):
        """Método privado (Helper) para reduzir duplicação de código na validação."""
        for v in vertices:
            if v not in self.adjacencias:
                raise KeyError(f"Vértice inválido ou inexistente: {v}")

    def adicionar_vertice(self, vertice):
        if vertice in self.adjacencias:
            raise ValueError(f"O vértice '{vertice}' já existe no grafo.")
        self.adjacencias[vertice] = []

    def adicionar_aresta(self, origem, destino):
        # Substituiu os ifs repetidos pela nova função validadora (Prática DRY)
        self._validar_vertice_existe(origem, destino)
        
        # Evita criar a mesma aresta duas vezes
        if destino in self.adjacencias[origem]:
            raise ValueError("Essa aresta já existe.")
            
        self.adjacencias[origem].append(destino)

    def _busca_em_largura(self, inicio, fim):
        """Lógica do algoritmo separada da validação para aumentar a coesão."""
        visitados = set()
        # Refatoração crítica: troca de lista por deque para performance otimizada
        fila = deque([inicio]) 

        while fila:
            atual = fila.popleft()
            
            if atual == fim:
                return True
                
            visitados.add(atual)
            
            for vizinho in self.adjacencias[atual]:
                if vizinho not in visitados and vizinho not in fila:
                    fila.append(vizinho)
                    
        return False

    def existe_caminho(self, inicio, fim):
        # Código mais legível: Valida as entradas e depois delega a busca para o método especialista
        self._validar_vertice_existe(inicio, fim)
        return self._busca_em_largura(inicio, fim)