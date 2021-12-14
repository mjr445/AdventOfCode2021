NUM_STEPS = 40

with open("day14.txt", "r") as file:
    letter_counts = {}
    rule_counts = {}
    rules = {}

    problem_string = file.readline().strip()
    for character in problem_string:
        letter_counts[character] = letter_counts.setdefault(character, 0) + 1
    
    file.readline()
    for line in file:
        key, value = line.split("->")
        rules[key.strip()] = value.strip()

    for i, character in enumerate(problem_string[:-1]):
        rule = f"{character}{problem_string[i+1]}"
        rule_counts[rule] = rule_counts.setdefault(rule, 0) + 1

    for i in range(NUM_STEPS):
        new_rule_counts = {}
        for rule, rule_count in rule_counts.items():
            character_to_insert = rules[rule]
            letter_counts[character_to_insert] = letter_counts.setdefault(character_to_insert, 0) + rule_count

            new_rule = f"{rule[0]}{character_to_insert}"
            new_rule_counts[new_rule] = new_rule_counts.setdefault(new_rule, 0) + rule_count

            new_rule = f"{character_to_insert}{rule[1]}"
            new_rule_counts[new_rule] = new_rule_counts.setdefault(new_rule, 0) + rule_count
        
        rule_counts = new_rule_counts

    max, min = -1, float('inf')
    for value in letter_counts.values():
        if value > max:
            max = value
        if value < min:
            min = value
    print(f"Max Count - Min Count = {max - min}")