with open("day9.txt", "r") as file:
    global_array = []
    for line in file:
        line = line.strip()
        row = [None for _ in range(len(line))]
        for i, number in enumerate(line):
            row[i] = int(number)
        global_array.append(row)
    
    directions = ((1, 0), (0, -1), (-1, 0), (0, 1))
    risk_level_sum = 0
    row_limit, col_limit = len(global_array), len(global_array[0])

    for row_num, row in enumerate(global_array):
        for col_num, value in enumerate(row):
            low_point = True
            for direction in directions:
                adjacent_row, adjacent_col = row_num + direction[0], col_num + direction[1]
                if 0 <= adjacent_row < row_limit and 0 <= adjacent_col < col_limit:
                    if value >= global_array[adjacent_row][adjacent_col]:
                        low_point = False
                        break
            if low_point:
                risk_level_sum = risk_level_sum + value + 1

    print(risk_level_sum)