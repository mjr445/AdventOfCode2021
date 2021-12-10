with open("day2.txt", "r") as file:
    depth = 0
    horizontal = 0
    for line in file.readlines():
        direction, value = line.split()
        value = int(value)
        if direction == 'forward':
            horizontal = horizontal + value
        elif direction == 'up':
            depth = depth - value
        elif direction == 'down':
            depth = depth + value
    result = horizontal * depth
    print(result)