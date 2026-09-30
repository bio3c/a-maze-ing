import random

rng = random.Random(42)

def adjacent(v: tuple) -> list[tuple]:
    edges = []
    x, y = v
    if (x, y - 1) in grid:
        edges.append((x, y - 1))
    if (x + 1, y) in grid:
        edges.append((x + 1, y))
    if (x, y + 1) in grid:
        edges.append((x, y + 1))
    if (x - 1, y) in grid:
        edges.append((x - 1, y))
    rng.shuffle(edges)
    return edges


if __name__ == "__main__":
    width = 2
    height = 2
    grid = [(x, y) for x in range(width) for y in range(height)]
    top = (0, 0)
    stack = [top]
    remaining = {v: adjacent(v) for v in grid}
    discovered = {top}
    parents = {top: None}
    while stack:
        v = stack[-1]
        if remaining[v]:
            neighbor = remaining[v].pop()
            if neighbor not in discovered:
                discovered.add(neighbor)
                parents[neighbor] = v
                stack.append(neighbor)
            else:
                wall[neighor] = current node
        else:
            stack.pop()
    for k, v in parents.items():
        print(k, v)

(0, 0), (1, 0) A, B
(0, 1), (1, 1) C, D


(0, 0) None
(1, 0) (0, 0)
(1, 1) (1, 0)
(0, 1) (1, 1)


A -> B-> D > C
