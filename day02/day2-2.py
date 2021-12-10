with open("day2.txt", "r") as file:
    depth = 0
    horizontal = 0
    aim = 0
    for line in file.readlines():
        direction, value = line.split()
        value = int(value)
        if direction == 'forward':
            horizontal = horizontal + value
            depth = depth + (aim * value)
        elif direction == 'up':
            aim = aim - value
        elif direction == 'down':
            aim = aim + value
    result = horizontal * depth
    print(result)