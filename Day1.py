from itertools import combinations


def solution():
    with open("Day1Input.txt", "r") as input_file:
        expenses = [int(line.strip()) for line in input_file.readlines()]
        for combo in combinations(expenses, 2):
            if combo[0] + combo[1] == 2020:
                return combo[0] * combo[1]


print(solution())