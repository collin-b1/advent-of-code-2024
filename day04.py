# Day 4: Ceres Search

test_input = \
    ['MMMSXXMASM',
     'MSAMXMSMSA',
     'AMXSXMAAMM',
     'MSAMASMSMX',
     'XMASAMXAMM',
     'XXAMMXXAMA',
     'SMSMSASXSS',
     'SAXAMASAAA',
     'MAMMMXMMMM',
     'MXMXAXMASX']


# Part 1
def part1(puzzle: [str]) -> int:
    total = 0
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            letter_one = puzzle[y][x]
            if letter_one != 'X':
                continue

            for j in range(-1, 2):
                y_end = y + (3 * j)
                if y_end < 0 or y_end >= len(puzzle):
                    continue

                for i in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    x_end = x + (3 * i)
                    if x_end < 0 or x_end >= len(puzzle[y]):
                        continue

                    letter_two = puzzle[y + j][x + i]
                    letter_three = puzzle[y + (2 * j)][x + (2 * i)]
                    letter_four = puzzle[y + (3 * j)][x + (3 * i)]
                    if letter_two == 'M' and letter_three == 'A' and letter_four == 'S':
                        total += 1

    return total


# Part 2
def part2(puzzle: [str]) -> int:
    total = 0
    for y in range(1, len(puzzle) - 1):
        for x in range(1, len(puzzle[y]) - 1):
            letter_one = puzzle[y][x]
            if letter_one != 'A':
                continue

            corners = [puzzle[y - 1][x + 1], puzzle[y + 1][x + 1], puzzle[y + 1][x - 1], puzzle[y - 1][x - 1]]
            if corners.count('S') == 2 and corners.count('M') == 2 and corners[0] != corners[2]:
                total += 1

    return total


if __name__ == '__main__':
    with open('./inputs/day04', 'r') as file:
        puzzle_input = file.readlines()
        print(f'{part1(puzzle_input)=}')
        print(f'{part2(puzzle_input)=}')
