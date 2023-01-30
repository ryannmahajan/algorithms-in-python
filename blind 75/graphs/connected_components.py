# name = input()                  # Reading input from STDIN
# print('Hi, %s.' % name)         # Writing output to STDOUT

from collections import defaultdict

def main(adjacent_nodes = None, n = -1, e = -1):
    if adjacent_nodes is None:
        n, e = read_first_line()
        adjacent_nodes = make_graph_from_input(e)
    print(adjacent_nodes)

    satisfied = set()
    res = 0

    def dfs(point, visited):
        print(point)
        if point in satisfied or point in visited:
            return
        
        nonlocal res
        if len(visited)==0: 
            res+=1

        if point in adjacent_nodes:
            visited.add(point)
            for neighbour in adjacent_nodes[point]:
                dfs(neighbour, visited)
            
            visited.remove(point)
        satisfied.add(point)

    for point in range(1, n+1):
        dfs(point, visited = set())

    return res

def read_first_line():
    line = input()
    n, e = tuple(line.strip().split(','))
    n, e = int(n), int(e)
    return n, e

def make_graph_from_input(e):
    graph = defaultdict(list)
    for i in range(e):
        line = input().strip()
        u, v = line.split(" ")
        u, v = int(u), int(v)
        graph[u].append(v)
        graph[v].append(u)
    
    return graph

print(main({1: [2, 3], 2: [1, 3], 3: [1, 2], 4: [5], 5: [4]}, n=6, e=4))
# print(make_graph_from_input(5))