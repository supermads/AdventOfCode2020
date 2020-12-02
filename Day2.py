def problem_a():
    with open("Day2Input.txt", "r") as input_file:
        entries = [line.strip() for line in input_file.readlines()]
        count = 0
        for entry in entries:
            colon = entry.find(':')
            dash = entry.find('-')
            bound_a = int(entry[0:dash])
            bound_b = int(entry[dash + 1: colon - 2])
            letter = entry[colon - 1]
            password = entry[(colon + 2):]
            if bound_b >= password.count(letter) >= bound_a:
                count += 1
        return count


def problem_b():
    with open("Day2Input.txt", "r") as input_file:
        entries = [line.strip() for line in input_file.readlines()]
        count = 0
        for entry in entries:
            colon = entry.find(':')
            dash = entry.find('-')
            idx_a = int(entry[0:dash])
            idx_b = int(entry[dash + 1: colon - 2])
            letter = entry[colon - 1]
            password = entry[(colon + 2):]
            if (password[idx_a - 1] == letter) != (password[idx_b - 1] == letter):
                count += 1
        return count



print(problem_a())
print(problem_b())