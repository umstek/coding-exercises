class Node:
    def __init__(self):
        self.distance = -1
        self.adjacent = list()

    def connect_node(self, index):
        if index not in self.adjacent:
            self.adjacent.append(index)

    def set_distance(self, new_dist):
        self.distance = new_dist


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
    graph.adj_graph[start].distance = 0
    queue = [start]

    while len(queue) > 0:
        queue.sort(key=lambda k: graph.adj_graph[k].distance)
        current = queue.pop(0)

        for ni in graph.adj_graph[current].adjacent:
            if graph.adj_graph[ni].distance == -1 or graph.adj_graph[current].distance + graph.edges[(current, ni)] < \
                    graph.adj_graph[ni].distance:
                graph.adj_graph[ni].set_distance(graph.adj_graph[current].distance + graph.edges[(current, ni)])
                queue.append(ni)

    return map(lambda key: graph.adj_graph[key].distance,
               filter(lambda key: key != start, sorted(graph.adj_graph.keys())))


def x_print(l):
    print(" ".join(map(str, l)))


test_count = int(input())

for t in range(test_count):
    test_graph, test_start = read_test_case()
    result = process_test_case(test_graph, test_start)
    x_print(result)
