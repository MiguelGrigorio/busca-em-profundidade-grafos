class Grafo:

  def __init__(self, vertices):
    self.vertices = vertices
    self.grafo = [[0] * vertices for i in range(vertices)]
  
  def add_no(self, u, v):
    self.grafo[u - 1][v - 1] = 1
    self.grafo[v - 1][u - 1] = 1
  
  def dfs(self, u, visitados=None):
    if visitados is None:
        visitados = [False] * self.vertices

    # Marcar o vértice atual como visitado
    visitados[u - 1] = True
    print(f'Visitando vértice {u}')

    # Recurso para todos os vértices adjacentes ainda não visitados
    for v in range(self.vertices):
        if self.grafo[u - 1][v] == 1 and not visitados[v]:
            self.dfs(v + 1, visitados)

  def mostrar_grafo(self):
    for linha in self.grafo:
      print(linha)

g = Grafo(19)

g.add_no(1, 3)
g.add_no(3, 4)
g.add_no(4, 19)
g.add_no(19, 18)
g.add_no(19, 16)
g.add_no(18, 17)
g.add_no(17, 16)
g.add_no(16, 15)
g.add_no(15, 14)
g.add_no(16, 12)
g.add_no(12, 14)
g.add_no(14, 13)
g.add_no(13, 5)
g.add_no(5, 6)
g.add_no(14, 10)
g.add_no(10, 11)
g.add_no(11, 8)
g.add_no(10, 9)
g.add_no(10, 8)
g.add_no(9, 6)
g.add_no(9, 8)
g.add_no(8, 7)
g.add_no(7, 6)
g.add_no(6, 2)
g.add_no(12, 2)
g.add_no(2, 1)

g.mostrar_grafo()

print("Busca em Profundidade:")
g.dfs(5)