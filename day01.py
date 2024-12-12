# Advent of Code Day 1: Historian Hysteria
if __name__ == '__main__':
    list1: [int] = []
    list2: [int] = []

    with open('./inputs/day01', 'r') as file:
        for line in file.readlines():
            split = line.strip().split()
            list1.append(int(split[0]))
            list2.append(int(split[1]))

    list1.sort()
    list2.sort()
    part1 = 0
    part2 = 0
    for left, right in zip(list1, list2):
        part1 += abs(left - right)
        part2 += left * list2.count(left)

    print(f'{part1=}\n{part2=}')
