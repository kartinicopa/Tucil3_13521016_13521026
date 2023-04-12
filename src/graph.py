import heapq

class Node:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.edges = []

    def add_edge(self, node, weight):
        self.edges.append((node, weight))

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

def read_file(filename):
    graph = Graph()

    with open(filename) as f:
        for line in f:
            if line.strip().isdigit():
                matrix_size = int(line.strip())
                adjacency_matrix = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
                for i in range(matrix_size):
                    line = f.readline().strip().split()
                    node_name = line[0]
                    node_lat = float(line[1])
                    node_lon = float(line[2])
                    node = Node(node_name, node_lat, node_lon)
                    graph.add_node(node)
                for i in range(matrix_size):
                    line = f.readline().strip().split()
                    for j in range(matrix_size):
                        adjacency_matrix[i][j] = int(line[j])
                for i in range(matrix_size):
                    for j in range(matrix_size):
                        if adjacency_matrix[i][j] == 1:
                            node1 = graph.nodes[i]
                            node2 = graph.nodes[j]
                            weight = ((node1.lat - node2.lat)**2 + (node1.lon - node2.lon)**2)**0.5
                            node1.add_edge(node2, weight)
                            node2.add_edge(node1, weight)

    return graph

def A_star(start_node, goal_node):
    frontier = []
    heapq.heappush(frontier, (0, start_node))
    came_from = {}
    cost_so_far = {}
    came_from[start_node] = None
    cost_so_far[start_node] = 0

    while len(frontier) > 0:
        current_node = heapq.heappop(frontier)[1]

        if current_node == goal_node:
            break

        for neighbor, weight in current_node.edges:
            new_cost = cost_so_far[current_node] + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + ((neighbor.lat - goal_node.lat)**2 + (neighbor.lon - goal_node.lon)**2)**0.5
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current_node

    path = []
    current_node = goal_node
    while current_node != start_node:
        path.append(current_node)
        current_node = came_from[current_node]
    path.append(start_node)
    path.reverse()

    return path

def ucs(start_node, goal_node):
    frontier = []
    heapq.heappush(frontier, (0, start_node))
    came_from = {}
    cost_so_far = {}
    came_from[start_node] = None
    cost_so_far[start_node] = 0

    while len(frontier) > 0:
        current_node = heapq.heappop(frontier)[1]

        if current_node == goal_node:
            break

        for neighbor, weight in current_node.edges:
            new_cost = cost_so_far[current_node] + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current_node

    path = []
    current_node = goal_node
    while current_node != start_node:
        path.append(current_node)
        current_node = came_from[current_node]
    path.append(start_node)
    path.reverse()

    return path