with open("day1.txt", "r") as f:
    numIncreases = 0
    prevNum = float('inf')
    for line in f:
        curNum = int(line)
        if curNum > prevNum:
            numIncreases = numIncreases + 1
        prevNum = curNum
    print(numIncreases)