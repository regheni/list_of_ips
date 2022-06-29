# build_graph(edges)
# {1: [2, 3], 2: [1, 3, 5], 3: [1, 2], 5: [2, 7], 7: [5], 8: [9], 9: [8, 10], 10: [9]}

from queue import Queue

number_of_nodes = 10
edges = [(1, 2), (1, 3), (2, 3), (2, 5), (5, 7), (5, 8), (8, 9), (9, 10)]


def build_graph_bi(edges):
    graph = dict()
    for node, neighbour in edges:
        current = graph.get(node, [])
        current.append(neighbour)
        graph[node] = current
        current = graph.get(neighbour, [])
        current.append(node)
        graph[neighbour] = current
    return graph


graph = build_graph_bi(edges)
print("BI: ", graph)


def build_graph_uni(edges):
    graph = dict()
    for node, neighbour in edges:
        current = graph.get(node, [])
        current.append(neighbour)
        graph[node] = current
    return graph


graph = build_graph_uni(edges)
print("UNI: ", graph)


# BFS

visited = {}
level = {}
parent = {}
bfs_output = []
queue = Queue()


for node in build_graph_bi(edges):
    visited[node] = False
    parent[node] = None
    level[node] = -1

start_node = "1"
visited[start_node] = True
level[start_node] = 0
queue.put(start_node)

while not queue.empty():
    u = queue.get()
    bfs_output.append(u)

    for v in build_graph_bi(edges):
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] + 1
            queue.put(v)


print("BFS: ", bfs_output)


# DFS

color = {}  # W, G, B
parent = {}
# trav_time = {}  # start, end
dfs_output = []
start_node = []

for node in build_graph_bi(edges):
    color[node] = "W"
    parent[node] = None
    # trav_time[node] = [-1, -1]
# print(color)
# print(parent)
# print(trav_time)


# time = 0


def dfs(start_node):
    # global time
    color[start_node] = "G"
    # trav_time[start_node][0] = time
    dfs_output.append(start_node)
    # time += 1
    for current_node in build_graph_bi(edges):
        if color[current_node] == "W":
            parent[current_node] = start_node
            dfs(current_node)
    color[start_node] = "B"
    # trav_time[start_node][1] = time
    # time += 1


dfs(1)
print("DFS: ", dfs_output)
# print(parent)
# print(trav_time)

# number_of_nodes = 10
# edges = [(1, 2), (1, 3), (2, 3), (2, 5), (5, 7), (8, 9), (9, 10)]
# graph = build_graph(edges)
# def build_graph(edges):

#     # TODO

# def bfs(graph, starting_node):
#     #TODO

# print(bfs(graph, 7))
# => [7, 5, 2, 1, 3]

# print(bfs(graph, 10))
# => [10, 9, 8]


# import random


# def generate_edges(number_of_edges, max_node):
#     edges = []
#     for edge in range(0, number_of_edges):
#         edge = sorted([random.choice(range(1, max_node)), random.choice(range(1, max_node))])
#         edges.append(edge)
#     return edges
