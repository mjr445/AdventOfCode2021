from collections import deque

incomplete_token_table = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
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

    scores = []

    for line in file:
        stack = deque()

        line = line.strip()
        stack.append(line[0])
        corrupt = False

        for i, character in enumerate(line[1:]):
            if is_inner_character(character):
                stack.append(character)
            elif stack[-1] != outer_to_inner_map[character]:
                corrupt = True
                break
            else:
                stack.pop()
        
        if not corrupt:
            final_score = 0
            while stack:
                incomplete_token = stack.pop()
                final_score = 5 * final_score + incomplete_token_table[incomplete_token]
            scores.append(final_score)
    scores.sort()
    middle_score = scores[(len(scores) - 1) // 2]
    print(middle_score)
