from SearchAlgorithm import load_json, BFS, DFS

if __name__ == '__main__':
    graph = load_json('graphs/graph1.json')
    print(graph)
    print('-'*5, 'BFS', '-'*5)
    bfs = BFS(graph=graph, start='S', goal='G')
    route = bfs.search('S', 'G', verbose=-1)
    print(route)

    print('-'*5, 'DFS', '-'*5)
    bfs = DFS(graph=graph, start='S', goal='G')
    route = bfs.search('S', 'G', verbose=-1)
    print(route)