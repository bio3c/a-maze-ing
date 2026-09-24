if __name__ == "__main__":
    width = 3
    height = 3
    grid = [(x, y) for x in range(width) for y in range(height)]
    discovered = set()
    
    stack = []
    start = (0, 0)
    
    stack.append(adjacent(start))
    discovered.add(start)
    
    while stack:
        if stack[-1]:
            neighbour = stack[-1].pop()
            #descer
            if neighbour not in discovered:
                discovered.add(neighbour)
                stack.append(adjacent(neighbour))
        else:
            stack.pop()
        

def adjacent(self, v: tuple) -> list[tuple]:
    possible_edges = []
    # we understand thaat this may perhaps be better randommized?
    #N
    if there is a vector above...
        add to possible_edges...
    #same for all the other directions

    return possible_edges

// INCOMPLETO!! 