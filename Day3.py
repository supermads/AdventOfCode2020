def solution_a():
    with open("Day3Input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file.readlines()]
        trees = 0
        i = 0
        j = 0
        while i < len(lines):
            if lines[i][j] == '#':
                trees += 1
            j += 3
            i += 1
            j %= len(lines[0])
    return trees


def solution_b(right, down):
    with open("Day3Input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file.readlines()]
        trees = 0
        i = 0
        j = 0
        while i < len(lines):
            if lines[i][j] == '#':
                trees += 1
            j += right
            i += down
            j %= len(lines[0])
    return trees


#print(solution_a())
print(solution_b(1,1) * solution_b(3,1) * solution_b(5,1) * solution_b(7,1) * solution_b(1,2))
