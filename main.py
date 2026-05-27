from app.grafo import Grafo

def iniciar_sistema():
    print("--- Sistema de Rotas em Grafos ---")
    grafo_interativo = Grafo()
    
    while True:
        print("\nOpções:")
        print("1. Adicionar Vértice (Nó)")
        print("2. Adicionar Aresta (Conexão)")
        print("3. Verificar Caminho")
        print("4. Sair")
        
        escolha = input("Escolha um comando: ")
        
        if escolha == '1':
            nome_vertice = input("Digite o nome do vértice: ")
            try:
                grafo_interativo.adicionar_vertice(nome_vertice)
                print(f"Vértice '{nome_vertice}' adicionado com sucesso!")
            except ValueError as erro:
                print(f"Erro: {erro}")
                
        elif escolha == '2':
            origem = input("Digite o vértice de origem: ")
            destino = input("Digite o vértice de destino: ")
            try:
                grafo_interativo.adicionar_aresta(origem, destino)
                print(f"Conexão de '{origem}' para '{destino}' criada!")
            except (KeyError, ValueError) as erro:
                print(f"Erro: {erro}")
                
        elif escolha == '3':
            inicio = input("De onde você quer sair? ")
            fim = input("Para onde quer ir? ")
            try:
                existe = grafo_interativo.existe_caminho(inicio, fim)
                if existe:
                    print(f"SIM! Existe um caminho possível entre '{inicio}' e '{fim}'.")
                else:
                    print(f"NÃO! É impossível chegar de '{inicio}' até '{fim}'.")
            except KeyError as erro:
                print(f"Erro: {erro}")
                
        elif escolha == '4':
            print("Encerrando o sistema...")
            break
        else:
            print("Comando inválido!")

if __name__ == "__main__":
    iniciar_sistema()