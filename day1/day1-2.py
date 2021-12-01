with open("day1.txt", "r") as file:
    increases = 0
    
    first = int(file.readline())
    second = int(file.readline())
    third = int(file.readline())
    for line in file:
        newNum = int(line)
        if newNum > first:
            increases = increases + 1
        first = second
        second = third
        third = newNum
    print(increases)