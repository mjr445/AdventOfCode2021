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

def graph_search(parent_node, small_visited_count={}):
    global global_path_count

    parent_label = parent_node.get_label()

    if parent_label == "end":
        global_path_count = global_path_count + 1
        return
    
    if not parent_node.get_is_big_cave():
        if parent_label in small_visited_count:
            small_visited_count[parent_label] = small_visited_count[parent_label] + 1
        else:
            small_visited_count[parent_label] = 1
    
    visited_value_set = set(small_visited_count.values())
    for label, node in parent_node.get_edges().items():
        if (not node.get_is_big_cave() and 2 in visited_value_set and label in small_visited_count) or label == "start":
            continue
        graph_search(node, small_visited_count.copy())


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
