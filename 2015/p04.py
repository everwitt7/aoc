import hashlib

def get_hash(string: str) -> str:
    return hashlib.md5(string.encode()).hexdigest()

def part_one(key: str) -> int:
    num = 0

    while True:
        num += 1
        res = get_hash(key + str(num))
        if res[:5] == "00000":
            break

    return num


def part_two(key: str) -> int:
    num = 0

    while True:
        num += 1
        res = get_hash(key + str(num))
        if res[:6] == "000000":
            break

    return num


if __name__ == "__main__":
    # sample puzzle_input
    # print(get_hash("abcdef609043"))
    sample_input = "abcdef"

    puzzle_input = "iwrupvqb"
    # print(part_one(puzzle_input))
    print(part_two(puzzle_input))
