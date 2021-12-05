with open("day5.txt", "r") as file:
    
    visited = set()
    overlapped = set()

    for line in file:
        points = line.split("->")
        start = [int(coord) for coord in points[0].strip().split(",")]
        stop = [int (coord) for coord in points[1].strip().split(",")]
        x1, y1 = start
        x2, y2 = stop

        if x1 != x2 and y1 != y2:
            continue

        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2+1):
                point = (x1, y)
                if point in visited:
                    overlapped.add(point)
                    visited.remove(point)
                else:
                    visited.add(point)

        else:  # y1 == y2
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2+1):
                point = (x, y1)
                if point in visited:
                    overlapped.add(point)
                    visited.remove(point)
                else:
                    visited.add(point)
    print(len(overlapped))
        