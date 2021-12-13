class Node:
    def __init__(self, label):
        self.label = label
        self.edges = {}
        self.is_big_cave = label.isupper()
    
    def __str__(self):
        return f"Label: {self.get_label()}\nEdges: {self.get_edges().keys()}\n"

    def __eq__(self, object):
        return self.label == object.label

    def get_label(self):
        return self.label
    
    def get_edges(self):
        return self.edges
    
    def get_is_big_cave(self):
        return self.is_big_cave

    def add_edge(self, connecting_vertex):
        if connecting_vertex.get_label() in self.edges:
            return
        self.edges[connecting_vertex.get_label()] = connecting_vertex

global_path_count = 0

def graph_search(parent_node, small_caves_visited=set()):
    global global_path_count

    if not parent_node.get_is_big_cave():
        small_caves_visited.add(parent_node.get_label())

    if parent_node.get_label() == "end":
        global_path_count = global_path_count + 1
        return
    
    for label, node in parent_node.get_edges().items():
        if label in small_caves_visited:
            continue
        graph_search(node, small_caves_visited.copy())


with open("day12.txt", "r") as file:

    graph = {}

    for line in file:
        vertex1_label, vertex2_label = line.strip().split("-")
        if vertex1_label not in graph:
            vertex1 = Node(vertex1_label)
            graph[vertex1_label] = vertex1
        else:
            vertex1 = graph[vertex1_label]
        
        if vertex2_label not in graph:
            vertex2 = Node(vertex2_label)
            graph[vertex2_label] = vertex2
        else:
            vertex2 = graph[vertex2_label]
        
        vertex1.add_edge(vertex2)
        vertex2.add_edge(vertex1)
    
    graph_search(graph['start'])
    print(global_path_count)
