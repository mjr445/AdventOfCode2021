from collections import deque

illegal_token_table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

outer_to_inner_map = {
    ']': '[',
    ')': '(',
    '}': '{',
    '>': '<'
}

def is_inner_character(character):
    return character not in outer_to_inner_map

def is_opposite_characters(inner_character, outer_character):
    return inner_character == outer_to_inner_map[outer_character]

with open("day10.txt", "r") as file:
    illegal_token_value_sum = 0

    for line in file:
        stack = deque()

        line = line.strip()
        stack.append(line[0])
        illegal_token_found = False

        for i, character in enumerate(line[1:]):
            if is_inner_character(character):
                stack.append(character)
            elif stack[-1] != outer_to_inner_map[character]:
                illegal_token = character
                illegal_token_found = True
                break
            else:
                stack.pop()
        
        if illegal_token_found:
            illegal_token_value_sum = illegal_token_value_sum + illegal_token_table[illegal_token]
    
    print(illegal_token_value_sum)