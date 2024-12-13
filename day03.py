# Day 3: Mull It Over
import re


# Part 1
def part1(puzzle: str) -> int:
    matches = re.findall(r"mul\((\d*),(\d*)\)", puzzle)
    products = [int(a) * int(b) for a, b in matches]
    return sum(products)


# Part 2
def part2(puzzle: str) -> int:
    matches = re.findall(r"(do\(\))|(don't\(\))|mul\((\d*),(\d*)\)", puzzle)
    enabled = True
    total = 0
    for do, dont, a, b in matches:
        if do:
            enabled = True
        if dont:
            enabled = False
        if a and b and enabled:
            total += int(a) * int(b)
    return total


if __name__ == '__main__':
    with open('./inputs/day03', 'r') as file:
        puzzle_input = file.read()
        print(f'{part1(puzzle_input)=}')
        print(f'{part2(puzzle_input)=}')
