class Node:
    adjacent = []
    distance = -1

    def __init__(self):
        self.adjacent = list()

    def connect_node(self, index):
        if index not in self.adjacent:
            self.adjacent.append(index)

    def set_distance(self, new_dist):
        self.distance = new_dist


class Graph:
    adj_graph = {}

    def __init__(self, node_count):
        self.adj_graph = dict()
        for i in range(node_count):
            self.adj_graph[i] = Node()

    def add_edge(self, nodei1, nodei2) -> None:
        self.adj_graph[nodei1].connect_node(nodei2)
        self.adj_graph[nodei2].connect_node(nodei1)


def read_test_case():
    node_count, edge_count = map(int, input().strip().split())
    graph = Graph(node_count)

    for i in range(edge_count):
        nodei1, nodei2 = map(int, input().strip().split())
        graph.add_edge(nodei1 - 1, nodei2 - 1)

    start = int(input()) - 1

    return graph, start


def process_test_case(graph, start):
    graph.adj_graph[start].distance = 0
    queue = [start]

    while len(queue) > 0:
        queue.sort(key=lambda k: graph.adj_graph[k].distance)
        current = queue.pop(0)

        for ni in graph.adj_graph[current].adjacent:
            if graph.adj_graph[ni].distance == -1:
                graph.adj_graph[ni].set_distance(graph.adj_graph[current].distance + 6)
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
