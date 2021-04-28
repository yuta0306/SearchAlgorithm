from SearchAlgorithm import load_json, BFS

if __name__ == '__main__':
    graph = load_json('graphs/graph1.json')
    print(graph, type(graph))

    bfs = BFS(graph=graph, start='S', goal='G')
    bfs.search('S', 'G')