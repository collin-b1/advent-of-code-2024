# Advent of Code Day 2: Red-Nosed Reports

# Provided test input
test_input = \
    [[7, 6, 4, 2, 1],
     [1, 2, 7, 8, 9],
     [9, 7, 6, 2, 1],
     [1, 3, 2, 4, 5],
     [8, 6, 4, 4, 1],
     [1, 3, 6, 7, 9]]

# Edge case tests for part 2
# All of these should be valid!
test_input_edges = \
    [[48, 46, 47, 49, 51, 54, 56],
     [1, 1, 2, 3, 4, 5],
     [1, 2, 3, 4, 5, 5],
     [5, 1, 2, 3, 4, 5],
     [1, 4, 3, 2, 1],
     [1, 6, 7, 8, 9],
     [1, 2, 3, 4, 3],
     [9, 8, 7, 6, 7],
     [7, 10, 8, 10, 11],
     [29, 28, 27, 25, 26, 25, 22, 20]]


# Part 1
def part1(puzzle: [[int]]) -> int:
    return sum([is_valid_report(row) for row in puzzle])


# Part 2
def part2(puzzle: [[int]]) -> int:
    return sum([is_valid_report_dampened(row) for row in puzzle])


# Returns if a report has more than 1 violation
def is_valid_report_dampened(nums: [int]) -> bool:
    valid = is_valid_report(nums)
    if not valid:
        for i in range(0, len(nums)):
            if is_valid_report(nums[:i] + nums[(i + 1):]):
                return True
        return False
    else:
        return True


# Returns if a report has a violation
def is_valid_report(nums: [int]) -> bool:
    last = nums[0]
    direction = 0
    for num in nums[1:]:
        diff = num - last

        # Check if difference is greater than 3 or less than 1
        if abs(diff) < 1 or abs(diff) > 3:
            return False

        # Check if direction changes
        current_direction = -1 if diff < 1 else 1
        if current_direction != direction and direction != 0:
            return False
        else:
            direction = current_direction

        # Continue to next number
        last = num
    return True


if __name__ == '__main__':
    with open('./inputs/day02', 'r') as file:
        puzzle_input = [[int(n) for n in line.strip().split()] for line in file.readlines()]
        print(f'{part1(test_input)=}')
        print(f'{part2(test_input)=}')
        print(f'{part1(puzzle_input)=}')
        print(f'{part2(puzzle_input)=}')
