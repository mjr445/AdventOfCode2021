with open("day5.txt", "r") as file:
    
    visited = set()
    overlapped = set()

    for line in file:
        points = line.split("->")
        p1 = [int(coord) for coord in points[0].strip().split(",")]
        p2 = [int (coord) for coord in points[1].strip().split(",")]
        x1, y1 = p1
        x2, y2 = p2

        if x1 != x2 and y1 != y2:
            if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):  # TL to BR
                if x1 > x2:
                    y1, y2, x1, x2 = y2, y1, x2, x1
                y = y1
                for x in range(x1, x2+1):
                    point = (x, y)
                    if point in visited:
                        overlapped.add(point)
                        visited.remove(point)
                    else:
                        visited.add(point)
                    y = y + 1
                
            else:  # BL to TR
                if y1 > y2:
                    y1, y2, x1, x2 = y2, y1, x2, x1
                x = x1
                for y in range(y1, y2+1):
                    point = (x, y)
                    if point in visited:
                        overlapped.add(point)
                        visited.remove(point)
                    else:
                        visited.add(point)
                    x = x - 1

        elif x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2+1):
                point = (x1, y)
                if point in overlapped:
                    continue
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
                if point in overlapped:
                    continue
                if point in visited:
                    overlapped.add(point)
                    visited.remove(point)
                else:
                    visited.add(point)
    print(len(overlapped))
