from itertools import combinations


#Solves Day 1, Question 1
def problem_a():
    with open("Day1Input.txt", "r") as input_file:
        expenses = [int(line.strip()) for line in input_file.readlines()]
        for combo in combinations(expenses, 2):
            if combo[0] + combo[1] == 2020:
                return combo[0] * combo[1]


#Solves Day 1, Question 2
def problem_b():
    with open("Day1Input.txt", "r") as input_file:
        expenses = [int(line.strip()) for line in input_file.readlines()]
        for combo in combinations(expenses, 3):
            if combo[0] + combo[1] + combo[2] == 2020:
                return combo[0] * combo[1] * combo[2]


#General Solution to Solve Question 1 and Question 2
def problem_c(n):
    with open("Day1Input.txt", "r") as input_file:
        expenses = [int(line.strip()) for line in input_file.readlines()]
        for combo in combinations(expenses, n):
            product = 1
            if sum(combo) == 2020:
                for x in combo:
                    product = product * x
                return product


print(problem_c(2))
print(problem_c(3))