"""Advent of Code 2020: Problem 1"""

# read input file into an array of strings
in_arr : list[int] = list()
with open ("./inputs/p01.txt", "r") as f:
    line = f.readline()
    while line:
        in_arr.append(int(line.strip()))
        line = f.readline()

# Part 1: two sum to find the the numbers that sum to 2020
def get_two_vals(arr: list[int], tar: int) -> tuple[int, int]:
    indices = dict()
    for i, val in enumerate(arr):
        if val in indices.keys():
            return arr[indices[val]], val
        indices[tar-val] = i
    return -1, -1

"""
Example:
Target: 15
Input:  [2, 4, 7, 3, 8]

i=0
Input[0] is 2, which is not in indices so we return nothing
indices[15-2] = 0 (now 13 is a key indices)

i=1
Input[1] is 4, which is not in indices so we return nothing
indices[15-4] = 1 (now 11 is a key indices)

i=2
Input[2] is 7, which is not in indices so we return nothing
indices[15-7] = 2 (now 8 is a key indices)

i=3
Input[3] is 3, which is not in indices so we return nothing
indices[15-3] = 3 (now 12 is a key indices)

i=4
Input[4] is 8, which is in indices!
We return Input[indices[8]] => Input[2] => 7, and the current value 8
"""

first, second = get_two_vals(in_arr, 2020)
print("Two Sum:", first, second, first + second, first * second)

# Part 2: three sum to find the numbers that sum to 2020
def get_three_vals(arr) -> tuple[int, int, int]:
    for i in range(1, len(arr)-2):
        tar = 2020 - arr[i]
        second, third = get_two_vals(arr[i:], tar)
        if second != -1 and third != -1:
            return arr[i], second, third
    return -1, -1, -1

one, two, three = get_three_vals(in_arr)
print("Three Sum:", one, two, three, one + two + three, one * two * three)