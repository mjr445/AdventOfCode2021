from numpy import array, zeros
from itertools import count
from heapq import heappop, heappush

graph = []

# Begin: https://docs.python.org/3/library/heapq.html#theory
pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

# End: https://docs.python.org/3/library/heapq.html#theory

# Begin: Pseudocode from https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Using_a_priority_queue used as basis
def djikstra(start_node):
    dist = {(0, 0): 0}
    prev = {}
    global pq

    num_rows, num_cols = graph.shape
    for row in range(num_rows):
        for col in range(num_cols):
            point = (row, col)
            if point != start_node:
                dist[point] = float('inf')
                prev[point] = None
            add_task(point, dist[point])
    
    while True:
        try:
            source = pop_task()
        except KeyError:
            break
        for neighbor in find_neighboring_points(source):
            alt = dist[source] + graph[neighbor]
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = source
                add_task(neighbor, alt)

    return dist
# End: Pseudocode from https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Using_a_priority_queue used as basis

def find_neighboring_points(point):
        """
        Return the neighboring points in the global array. Neighbors can be found
        directly above, under, left, and right of the point in the array

        :param point: array of x and y points
        :return neighboring_nodes: tuple of neighboring points
        """

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        row_limit, col_limit = graph.shape
        row_num, col_num = point
        neighboring_points = []

        for direction in directions:
            adjacent_row, adjacent_col = row_num + direction[0], col_num + direction[1]
            if 0 <= adjacent_row < row_limit and 0 <= adjacent_col < col_limit:
                neighboring_points.append((adjacent_row, adjacent_col))
        
        return tuple(neighboring_points)

with open("day15.txt", "r") as file:

    for line in file:
        line = line.strip()
        row = zeros(len(line), dtype=int)
        for column, number in enumerate(line):
            row[column] = int(number)
        graph.append(row)
    graph = array(graph)

    AXIS_LENGTH = graph.shape[0]  # input is square
    START = (0, 0)
    END = (AXIS_LENGTH - 1, AXIS_LENGTH - 1)

    lowest_total_risks = djikstra(START)
    lowest_total_risk = lowest_total_risks[END]
    print(lowest_total_risk)