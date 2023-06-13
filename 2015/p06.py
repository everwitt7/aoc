import re

def parser(file: str):

    with open(file, "r") as f:
        contents = []
        for line in f:
            match = re.match(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', line)

            if match:
                action = match.group(1)
                start = (int(match.group(2)), int(match.group(3)))
                end = (int(match.group(4)), int(match.group(5)))
                contents.append((action, start, end))
            else:
                raise ValueError("Invalid instruction format: " + line)
    return contents

def one(instruction: tuple, grid: list):
    x_range = range(instruction[1][0], instruction[2][0]+1)
    y_range = range(instruction[1][1], instruction[2][1]+1)
    if instruction[0] == "turn on":
        for x in x_range:
            for y in y_range:
                grid[x][y] = 1
    elif instruction[0] == "turn off":
        for x in x_range:
            for y in y_range:
                grid[x][y] = 0
    elif instruction[0] == "toggle":
        for x in x_range:
            for y in y_range:
                grid[x][y] = grid[x][y] ^ 1
    else:
        print("Bad Instruction", instruction)


def two(instruction: tuple, grid: list):
    x_range = range(instruction[1][0], instruction[2][0]+1)
    y_range = range(instruction[1][1], instruction[2][1]+1)
    if instruction[0] == "turn on":
        for x in x_range:
            for y in y_range:
                grid[x][y] += 1
    elif instruction[0] == "turn off":
        for x in x_range:
            for y in y_range:
                if grid[x][y] > 0:
                    grid[x][y] -= 1
    elif instruction[0] == "toggle":
        for x in x_range:
            for y in y_range:
                grid[x][y] += 2
    else:
        print("Bad Instruction", instruction)


if __name__ == "__main__":
    file = "./inputs/p06.txt"
    contents = parser(file)
    print(contents[0:5])

    length = 1000
    grid = [[0 for _ in range(length)] for _ in range(length)]

    for content in contents:
        # lists are mutable, so this updates in place
        # one(content, grid)
        two(content, grid)

    total = 0
    for x in range(length):
        for y in range(length):
            total += grid[x][y]
    print(total)
