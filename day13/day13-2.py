from numpy import flipud, fliplr, full, savetxt

with open("day13.txt") as file:
    y_max = x_max = -1
    points = set()

    for line in file:
        if line == "\n":
            break
        y, x = line.strip().split(",")
        y, x = int(y), int(x)
        if y > y_max:
            y_max = y
        if x > x_max:
            x_max = x
        points.add((x, y))
    
    grid = full((x_max+1, y_max+1), False)

    for point in points:
        grid[point] = True
    
    for line in file:
        fold_line = line.split()[2].strip()
        axis, value = fold_line.split('=')
        value = int(value)
        if axis=='y':
            upper_fold = grid[:value, :]
            lower_fold = grid[value+1:, :]

            lower_fold = flipud(lower_fold)
            grid = upper_fold | lower_fold

        else:  # axis == 'x'
            left_fold = grid[:, :value]
            right_fold = grid[:, value+1:]

            right_fold = fliplr(right_fold)
            grid = left_fold | right_fold

    string_grid = full(grid.shape, ' ')
    string_grid[grid] = '#'
    savetxt('day13_out.txt', string_grid, fmt='%s')  # I'm not writing code to detect a letter, I'm just going to look visually
