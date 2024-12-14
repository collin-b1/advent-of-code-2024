# Day 5: Print Queue
from typing import Dict, List, Tuple

test_input_rules = \
    [(47, 53), (97, 13), (97, 61), (97, 47), (75, 29), (61, 13), (75, 53), (29, 13), (97, 29), (53, 29), (61, 53),
     (97, 53), (61, 29), (47, 13), (75, 47), (97, 75), (47, 61), (75, 61), (47, 29), (75, 13), (53, 13)]

test_input_updates = \
    [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13], [75, 97, 47, 61, 53], [61, 13, 29], [97, 13, 75, 29, 47]]


# Part 1
def part1(rules: List[Tuple[int, ...]], updates: List[List[int]]) -> int:
    rules_dict = get_rules_dict(rules)
    middle_pages_sum = 0
    for update in updates:
        invalid = False
        for i in range(len(update) - 1):
            current_page = update[i]
            next_page = update[i + 1]
            if current_page in rules_dict.get(next_page, []):
                invalid = True
                break

        if not invalid:
            middle_page = update[len(update) // 2]
            middle_pages_sum += middle_page

    return middle_pages_sum


# Part 2
def part2(rules: List[Tuple[int, ...]], updates: List[List[int]]) -> int:
    rules_dict = get_rules_dict(rules)
    middle_pages_sum = 0
    for update in updates:
        for i in range(len(update) - 1):
            current_page = update[i]
            next_page = update[i + 1]
            if current_page in rules_dict.get(next_page, []):
                corrected = get_correct_order(rules_dict, update)
                middle_pages_sum += corrected[len(corrected) // 2]
                break

    return middle_pages_sum


# Maps numbers to a list of numbers it should come before
def get_rules_dict(rules: List[Tuple[int, ...]]) -> Dict[int, List[int]]:
    rules_dict: Dict[int, List[int]] = {}
    for rule in rules:
        # Initialize empty array if it doesn't exist
        rules_dict.setdefault(rule[0], [])
        rules_dict[rule[0]].append(rule[1])

    return rules_dict


# Sorts numbers to correct order based on given rules dictionary
def get_correct_order(rules_dict: Dict[int, List[int]], update: List[int]) -> List[int]:
    valid = False
    while not valid:
        valid = True
        for i in range(len(update) - 1):
            current_item = update[i]
            for j in range(i + 1, len(update)):
                next_item = update[j]
                if current_item in rules_dict.get(next_item, []):
                    update[i], update[j] = update[j], update[i]
                    valid = False

    return update


if __name__ == '__main__':
    with open('./inputs/day05', 'r') as file:
        puzzle_input = file.readlines()
        rules_end_index = puzzle_input.index('\n')
        puzzle_rules = [tuple([int(i) for i in rule.split('|')]) for rule in puzzle_input[:rules_end_index]]
        puzzle_updates = [[int(i) for i in page.split(',')] for page in puzzle_input[(rules_end_index + 1):]]
        print(f'{part1(test_input_rules, test_input_updates)=}')
        print(f'{part2(test_input_rules, test_input_updates)=}')
        print(f'{part1(puzzle_rules, puzzle_updates)=}')
        print(f'{part2(puzzle_rules, puzzle_updates)=}')
