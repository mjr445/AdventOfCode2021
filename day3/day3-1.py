NUM_BITS = 12

with open("day3.txt", "r") as file:

    sums = [0 for _ in range(NUM_BITS)]
    number_lines = 0

    for line in file:
        line = line[:-1]
        for i, bit in enumerate(line):
            sums[i] = sums[i] + int(bit)
        number_lines = number_lines + 1
    
    gamma_rate = 0
    epsilon_rate = 0
    for sum in sums:
        if sum > number_lines/2:
            gamma_rate = (gamma_rate << 1) | 1
            epsilon_rate = epsilon_rate << 1
        else:
            gamma_rate = gamma_rate << 1
            epsilon_rate = (epsilon_rate << 1) | 1
    print(gamma_rate * epsilon_rate)