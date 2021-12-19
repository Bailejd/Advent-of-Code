# Day 12: Passage Pathing
#
# Results
# Part 1: 3000
# Part 2:

from collections import defaultdict

def part_one(adjacencyList, vertex="start", valid_paths=None, visited=None, path=None):
    if(valid_paths is None):
        valid_paths = []
    if(visited is None):
        visited = set()
    if(path is None):
        path = []
    
    visited.add(vertex)
    path.append(vertex)

    if(vertex == 'end'):
        valid_paths.append(path)
    
    for neighbor in adjacencyList[vertex]:
        if(neighbor not in visited or neighbor.isupper()):
            part_one(adjacencyList, neighbor, valid_paths, visited, path)
    
    path.pop()
    if(vertex.islower()):
        visited.remove(vertex)
    
    return len(valid_paths)


def part_two(adjacencyList, vertex="start", valid_paths=None, visited=None, path=None, visited_small_twice=False):
    pass


def main():
    # Read input file
    with open("./input.txt", "r") as f:
        edges = f.read().split('\n')

    edges = [ele.split('-') for ele in edges]
    
    adjacencyList = defaultdict(list)
    small_caves = set()

    for u, v in edges:
        adjacencyList[u].append(v)
        adjacencyList[v].append(u)

    # Part 1
    print(f'Part 1: {part_one(adjacencyList)}')

    # Part 2
    # print(f'Part 2: {part_two(adjacencyList)}')


if __name__ == '__main__':
    main()
