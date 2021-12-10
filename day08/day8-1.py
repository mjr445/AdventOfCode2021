counts = {
    2: 0,  # 1
    4: 0,  # 4
    3: 0,  # 7
    7: 0   # 8
}

counts_set = set((2, 4, 3, 7))

with open("day8.txt", "r") as file:
    for line in file:
        for sequence in line.split("|")[1].split():
            sequence = sequence.strip()
            length = len(sequence)
            if length in counts_set:
                counts[length] = counts[length] + 1
    print(sum(counts.values()))