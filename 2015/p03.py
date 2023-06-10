def part_one(file_contents: str, houses: dict = None) -> int:

    houses = houses or {"(0, 0, 0, 0)": 1}
    count_n, count_s, count_w, count_e = 0, 0, 0, 0

    north = "^"
    south = "v"
    west = "<"
    east = ">"


    # file_contents = "^>v<"

    for c in file_contents:
        # match statements are nice for rust
        if c == north:
            if count_s > 0:
                count_s -= 1
            else:
                count_n += 1

        elif c == south:
            if count_n > 0:
                count_n -= 1
            else:
                count_s += 1

        elif c == east:
            if count_w > 0:
                count_w -= 1
            else:
                count_e += 1

        elif c == west:
            if count_e > 0:
                count_e -= 1
            else:
                count_w += 1

        else:
            print("unexpected character")
            continue


        # create string key:
        key = str(tuple([count_n, count_s, count_w, count_e]))
        # print(key)
        # key = str(count_n) + str(count_s) + str(count_w) + str(count_e)
        houses[key] = 1 if key not in houses else houses[key] + 1
        # Example of Collision... how to handle 
        # 120, 0, 0, 0 => 120000
        # 1, 200, 0, 0 => 120000
    return houses


def part_two(file_contents: str) -> int:
    s = slice(1, len(file_contents), 2)
    santa_path = file_contents[::2]
    # robo_path = file_contents[s]
    robo_path = file_contents[1::2]

    houses = part_one(santa_path)
    houses = part_one(robo_path, houses)
    return houses

    # I can just use part_one() to add to an existing dictionary

    count_n, count_s, count_w, count_e = 0, 0, 0, 0

    north = "^"
    south = "v"
    west = "<"
    east = ">"

    houses = {"(0, 0, 0, 0)": 2}

    for c in santa_path:
        # match statements are nice for rust
        if c == north:
            if count_s > 0:
                count_s -= 1
            else:
                count_n += 1

        elif c == south:
            if count_n > 0:
                count_n -= 1
            else:
                count_s += 1

        elif c == east:
            if count_w > 0:
                count_w -= 1
            else:
                count_e += 1

        elif c == west:
            if count_e > 0:
                count_e -= 1
            else:
                count_w += 1

        else:
            print("unexpected character")
            continue

        key = str(tuple([count_n, count_s, count_w, count_e]))
        houses[key] = 1 if key not in houses else houses[key] + 1

    count_n, count_s, count_w, count_e = 0, 0, 0, 0
    for c in robo_path:
        # match statements are nice for rust
        if c == north:
            if count_s > 0:
                count_s -= 1
            else:
                count_n += 1

        elif c == south:
            if count_n > 0:
                count_n -= 1
            else:
                count_s += 1

        elif c == east:
            if count_w > 0:
                count_w -= 1
            else:
                count_e += 1

        elif c == west:
            if count_e > 0:
                count_e -= 1
            else:
                count_w += 1

        else:
            print("unexpected character")
            continue

        key = str(tuple([count_n, count_s, count_w, count_e]))
        houses[key] = 1 if key not in houses else houses[key] + 1
    
    return len(houses)

if __name__ == "__main__":
    with open("./inputs/p03", "r") as f:
        file_contents = f.read()

    #print(len(part_one(file_contents)))

    # this is an example of something that should be run as a TEST automatically
    # file_contents = "^v"
    houses = part_two(file_contents)
    # print(part_two(file_contents))
    print(len(houses))

 
