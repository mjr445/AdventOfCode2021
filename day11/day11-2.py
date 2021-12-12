from numpy import all, any, array, count_nonzero, where, zeros

DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))

def find_neighboring_points(point):
        """
        Return the neighboring points in the global array. Neighbors can be found
        directly above, under, left, and right of the point in the array

        :param point: array of x and y points
        :return neighboring_nodes: tuple of neighboring points
        """

        directions = (  (1, 0), 
                        (0, -1), 
                        (-1, 0), 
                        (0, 1), 
                        (1, 1), 
                        (-1, -1), 
                        (1, -1), 
                        (-1, 1))
        
        row_limit, col_limit = input_array.shape
        row_num, col_num = point
        neighboring_points = []

        for direction in directions:
            adjacent_row, adjacent_col = row_num + direction[0], col_num + direction[1]
            if 0 <= adjacent_row < row_limit and 0 <= adjacent_col < col_limit:
                neighboring_points.append((adjacent_row, adjacent_col))
        
        return tuple(neighboring_points)

def increase_flashed_neighbors(neighboring_points):
    x_vals, y_vals = neighboring_points
    for i, x in enumerate(x_vals):
        neighbors = find_neighboring_points((x, y_vals[i]))
        for neighbor in neighbors:
            neighbor_x, neighbor_y = neighbor
            input_array[neighbor_x, neighbor_y] += 1

input_array = []

with open("day11.txt", "r") as file:

    for line in file:
        line = line.strip()
        row = zeros(len(line), dtype=int)
        for column, number in enumerate(line):
            row[column] = int(number)
        input_array.append(row)
    input_array = array(input_array)

    # First Step Begins

    input_array = input_array + 1
    do_flashes_occur = input_array > 9

    # while any(do_flashes_occur):
    steps = 0
    while True:
        
        neighboring_points = where(do_flashes_occur)
        increase_flashed_neighbors(neighboring_points)
        are_there_new_flashes = do_flashes_occur ^ (input_array > 9)
        previous_flashes = do_flashes_occur

        while any(are_there_new_flashes):
            previous_flashes = are_there_new_flashes | previous_flashes

            neighboring_points = where(are_there_new_flashes)
            increase_flashed_neighbors(neighboring_points)
            are_there_new_flashes = previous_flashes ^ (input_array > 9)

        final_flash_locations = input_array > 9
        if all(final_flash_locations):
            steps = steps + 1
            break
        input_array[final_flash_locations] = 0
        # Step Complete

        # Next Step Begins
        input_array = input_array + 1
        do_flashes_occur = input_array > 9
        steps = steps + 1
    
    print(f"Step where all positions flashed: {steps}")
