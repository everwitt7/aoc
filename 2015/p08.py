def parser(file):
    contents = []
    with open(file, "r") as f:
        for line in f.readlines():
            contents.append(line.rstrip())
    return contents

def one(contents):
    new_contents = []
    for line in contents:
        string = eval(line)
        new_contents.append(string)
    return new_contents

def two(contents):
    new_contents = []
    for line in contents:
        string = '"' + line.replace('\\', '\\\\').replace('"', '\\"') + '"'
        new_contents.append(string)
    return new_contents


def calculate_code_minus_memory(filename):
    total_code_length = 0
    total_memory_length = 0

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()

            # Update total code length
            total_code_length += len(line)

            # Remove surrounding double quotes and evaluate escape sequences
            memory_string = eval(line)

            # Update total memory length
            total_memory_length += len(memory_string)

    return total_code_length - total_memory_length

if __name__ == "__main__":
    file = "./inputs/p08.txt"
    contents = parser(file)

    n = one(contents)
    c1, c2 = 0, 0

    for s in contents:
        c1 += len(s)
    for s in n:
        c2 += len(s)

    print(c1, c2, c1-c2)

    nn = two(contents)
    c1, c2 = 0, 0

    for s in contents:
        c1 += len(s)
    for s in nn:
        c2 += len(s)

    print(c1, c2, c2-c1)

