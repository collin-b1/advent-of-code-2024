# Advent of Code Day 1: Historian Hysteria
if __name__ == '__main__':
    # Part 1
    list1: [int] = []
    list2: [int] = []
    with open('./inputs/day01', 'r') as file:
        for line in file:
            split = line.strip().split()
            list1.append(int(split[0]))
            list2.append(int(split[1]))
    list1.sort()
    list2.sort()
    distances: [int] = []
    for i in range(len(list1)):
        distances.append(abs(list1[i] - list2[i]))
    part1 = sum(distances)
    print(f'{part1=}')

    # Part 2
    similarities: [int] = []
    for i in range(len(list1)):
        similarities.append(list1[i] * list2.count(list1[i]))
    part2 = sum(similarities)
    print(f'{part2=}')