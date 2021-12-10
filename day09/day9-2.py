global_graph = []

class Node:
    def __init__(self, value, point):
        self.value = value
        self.point = point
        self.visited_status = False
        self.edge_status = True if value == 9 else False
    
    def __str__(self):
        return f"Value: {self.value}\nVisited: {self.visited_status}\nEdge: {self.edge_status}"
    
    def get_value(self):
        return self.value

    def get_point(self):
        return self.point

    def get_edge_status(self):
        return self.edge_status
    
    def get_visited_status(self):
        return self.visited_status
    
    def find_neighboring_nodes(self):
        """
        Return the neighboring nodes in the global graph. Neighbors can be found
        directly above, under, left, and right of the node in the graph

        :return neighboring_nodes: tuple of neighboring nodes
        """

        directions = ((1, 0), (0, -1), (-1, 0), (0, 1))
        row_num, col_num = self.point
        row_limit, col_limit = len(global_graph), len(global_graph[0])
        neighboring_nodes = []

        for direction in directions:
            adjacent_row, adjacent_col = row_num + direction[0], col_num + direction[1]
            if 0 <= adjacent_row < row_limit and 0 <= adjacent_col < col_limit:
                neighboring_nodes.append(global_graph[adjacent_row][adjacent_col])
        
        return tuple(neighboring_nodes)

    def visit(self):
        self.visited_status = True

    def is_searchable(self):
        """
        True if node is not an edge or already visited - False otherwise
        """
        
        return not self.get_edge_status() and not self.get_visited_status()


def dfs(node, basin_size):
    basin_size = basin_size + 1
    node.visit()

    for neighbor in node.find_neighboring_nodes():
        if neighbor.is_searchable():
            basin_size = dfs(neighbor, basin_size)

    return basin_size

with open("day9.txt", "r") as file:
    for row_num, line in enumerate(file):
        line = line.strip()
        row = [None for _ in range(len(line))]
        for col_num, number in enumerate(line):
            row[col_num] = Node(int(number), (row_num, col_num))
        global_graph.append(row)
    
    three_largest_basin_sizes = (-1, -1, -1)
    for row in global_graph:
        for node in row:
            if node.is_searchable():
                basin_size = dfs(node, 0)
                if basin_size > three_largest_basin_sizes[0]:
                    three_largest_basin_sizes = basin_size, three_largest_basin_sizes[0], three_largest_basin_sizes[1]
                elif basin_size > three_largest_basin_sizes[1]:
                    three_largest_basin_sizes = three_largest_basin_sizes[0], basin_size, three_largest_basin_sizes[1]
                elif basin_size > three_largest_basin_sizes[2]:
                    three_largest_basin_sizes = three_largest_basin_sizes[0], three_largest_basin_sizes[1], basin_size

    basin_size_product = 1
    for basin_size in three_largest_basin_sizes:
        basin_size_product = basin_size_product * basin_size
    
    print(basin_size_product)