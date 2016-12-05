class Node:
    def __init__(self):
        self.adjacent = list()

    def connect_node(self, index):
        if index not in self.adjacent:
            self.adjacent.append(index)


class Graph:
    def __init__(self, node_count):
        self.adj_graph = dict()
        self.edges = dict()
        for i in range(node_count):
            self.adj_graph[i] = Node()

    def add_edge(self, nodei1, nodei2, weight):
        if (nodei1, nodei2) in self.edges:
            self.edges[(nodei1, nodei2)] = min([weight, self.edges[(nodei1, nodei2)]])
        else:
            self.edges[(nodei1, nodei2)] = weight

        if (nodei2, nodei1) in self.edges:
            self.edges[(nodei2, nodei1)] = min([weight, self.edges[(nodei2, nodei1)]])
        else:
            self.edges[(nodei2, nodei1)] = weight

        self.adj_graph[nodei1].connect_node(nodei2)
        self.adj_graph[nodei2].connect_node(nodei1)


def read_test_case():
    node_count, edge_count = map(int, input().strip().split())
    graph = Graph(node_count)

    for i in range(edge_count):
        nodei1, nodei2, weight = map(int, input().strip().split())
        graph.add_edge(nodei1 - 1, nodei2 - 1, weight)

    start = int(input()) - 1

    return graph, start


def process_test_case(graph, start):
    weights = 0
    edges = [(start, e) for e in graph.adj_graph[start].adjacent]
    edges.sort(key=lambda a: graph.edges[a])
    vertices = [start]

    while len(vertices) < len(graph.adj_graph.keys()):
        edge = edges.pop(0)
        while edge[1] in vertices:
            edge = edges.pop(0)
        vertices += [edge[1]]
        weights += graph.edges[edge]
        edges += [(edge[1], e) for e in graph.adj_graph[edge[1]].adjacent]
        edges.sort(key=lambda a: graph.edges[a])

    return weights


test_graph, test_start = read_test_case()
result = process_test_case(test_graph, test_start)
print(result)
