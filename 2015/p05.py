def parser(file_path: str):
    # returns a list of strings
    contents = []
    with open(file_path, "r") as f:
        while line := f.readline():
            contents.append(line.rstrip())
    return contents


def part_one(string: str) -> bool:
    bad_chars = ["ab", "cd", "pq", "xy"]
    for bad_char in bad_chars:
        if bad_char in string:
            return False

    vowels = ["a", "e", "i", "o", "u"]
    num_vowels = 0
    for char in string:
        if char in vowels:
            num_vowels += 1
    if num_vowels < 3:
        return False

    # iterate from 0..len(string)-1 if i i+1 are the same return true
    for idx in range(len(string)-1):
        if string[idx] == string[idx+1]:
            return True
    return False

def part_two(string: str) -> bool:
    in_between = False
    for idx in range(len(string)-2):
        c1 = string[idx]
        c2 = string[idx+1]
        c3 = string[idx+2]
        # turns out 'xxx' does work
        if c1 == c3: 
            in_between = True
            break

    # "abcdefgh"
    # ab (idx-2=a idx-1=b) cd, de, ef, fg, gh (idx, idx+1)
    contains_pair = False
    for idx in range(2, len(string)-1):
        char1 = string[idx-2]
        char2 = string[idx-1]
        for idx2 in range(idx, len(string)-1):
            char3 = string[idx2]
            char4 = string[idx2+1]
            # print(char1, char2, char3, char4)
            if char1 == char3 and char2 == char4:
                contains_pair = True
                break
    return in_between and contains_pair


    

if __name__ == "__main__":
    file_path = "./inputs/p05.txt"
    sample_inputs = ["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]

    # for sample_input in sample_inputs:
        # print(sample_input, part_one(sample_input))

    contents = parser(file_path)
    # print(contents[0:5])
    
    # nice_strings = list(map(part_one, contents))
    # print(sum(nice_strings))

    sample_inputs = ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"]
    # for sample_input in sample_inputs:
    #     print(sample_input, part_two(sample_input))
   
    count = 0
    offset = 30
    nice_strings = list(map(part_two, contents))
    print(sum(nice_strings))
    # nice_strings = list(map(part_two, contents[count:count+offset]))
    for boolean, string in zip(nice_strings[count:count+offset], contents[count:count+offset]):
        print(string, boolean)

