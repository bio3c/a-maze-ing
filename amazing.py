class MazeGenerator:
	def __init__(self, 
                 largura: int, 
                 altura: int, 
                 seed: int,
                 entrada: tuple[int, int],
                 saida: tuple[int, int]):
		self._largura = largura
		self._altura = altura
		self._seed = seed
		self._perfect = True
		self._entrada = entrada
		self._saida = saida
		#cells: representam as celulas do grid em si
		#criar funcao para preencher as celulas
		self._cells: set[tuple[int, int]] = set()
		#graph: dicionario, onde a chave = celula, e valor lista de visinhos
		#e.g: dict = {(0, 0): {(0, 1), (1, 0)}} 
		self._graph: dict[
            tuple[int, int],
            list[tuple[int, int]]
        ] = {}
		#visited: um set que salva todas as celulas ja visitadas
		self._visited: set[tuple[int, int]] = set()
		#a lista em si que representa as celulas que podemos visitar
		self._stack: list[tuple[int, int]] = []


    def _create_cells(self, c: set[tuple[int, int]]):
        for x in range(0, self._largura):
            for y in range(0, self._altura):
                  c.add((x, y))


if __name__ == "__main__":
    Maze = MazeGenerator(3, 3, 1000, (0,0), (2,2))
