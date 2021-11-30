"""Advent of Code 2020: Problem 2"""

# Example Input - Digits can be different length, but `char`: `string` is a constant format that we can use a regular expression to textract
# There will only ever be a single colon
# 3-14 v: vvpvvvmvvvvvvvv
# 2-5 m: mfvxmmm
in_arr : list[tuple[int, int, str, str]] = list()
with open ("./inputs/p02.txt", "r") as f:
    line = f.readline()
    while line:
        s = line.strip().split(" ")
        mn, mx = s[0].split("-")
        in_arr.append((int(mn), int(mx), s[1][0], s[2]))
        line = f.readline()

# Part 1: check the number of character occurences in a string
def count_chars(mn: int, mx: int, char: str, paswd: str) -> bool:
    """This function counts the number of time a character appears in a string and 
    checks whether it is between the minimum and maximum amount of required occurences

    Args:
        mn (int): minimum number of necessasry occurences
        mx (int): maximum number of necessary occurences
        char (str): the character that has the min, max requirements
        paswd (str): the password

    Returns:
        bool: true if the password is valid, false if not
    """
    n_chars = paswd.count(char)
    return 1 if mn <= n_chars <= mx else 0


# Part 2: check the value of string indices (but we can now index out of bounds)
def check_indices(ix: int, iy: int, char: str, paswd: str) -> bool:
    """Determines if a password if valid by checking if the char occurs at most once
    at either the first or second index, ix and iy, respectively.

    Args:
        ix (int): first index
        iy (int): second index
        char (str): required character
        paswd (str): password

    Returns:
        bool: true if the password is valid
    """
    ix -= 1
    iy -= 1
    retX = retY = False 

    # make sure that we do not index out of bounds
    if -1 < ix < len(paswd) - 1:
        if paswd[ix] == char:
            retX = True

    if 0 < iy < len(paswd):
        if paswd[iy] == char:
            retY = True
    
    # we can use exclusive or to return false if neither or both are true
    return retX ^ retY


n_char_valid = n_ind_valid = 0
for v in in_arr:
    if count_chars(*v):
        n_char_valid += 1
    if check_indices(*v):
        n_ind_valid += 1

print("Number of Char Valid Password:", n_char_valid)
print("Number of Index Valid Password:", n_ind_valid)