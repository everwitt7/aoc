"""Advent of Code 2020: Problem 3"""

arr: list[str] = list()
with open ("./inputs/p03.txt", "r") as f:
    line = f.readline()
    while line:
        arr.append(line.strip())
        line = f.readline()


# Part 1: 3 right, 1 down starting at the top-left corner
# We know that map continuous infinitely, so we can just wrap
# the index back to the beginning => use modulo to get the remainder!
def num_trees(arr: list[str]) -> int:
    """Counts the number of trees we encounter by going right 3 units and down 1 unit

    Args:
        arr (list[str]): the map

    Returns:
        int: the number of trees we encounter
    """
    trees_encountered = j = 0
    tree = "#"
    # go from 0 to len(arr), incrementing by 1 each time because we go down 1 at a time
    for i in range(0, len(arr), 1):
        if arr[i][j % len(arr[0])] == tree:
            trees_encountered += 1
        j += 3
    return trees_encountered

sol = num_trees(arr)
print("Part 1:", sol)

# Part 2: we need to calculate part 1 but for different `strides` of moving up and down...
# let's right a general function (which was hinted at by denoting, start, stop, stride in range)
def num_gen_trees(arr: list[str], right:int, down:int) -> int:
    """Counts the number of trees we encounter by going right and down variable units

    Args:
        arr (list[str]): input map
        right (int): how far we go to the right after each iteration
        down (int): how far we go down after each iteration

    Returns:
        int: number of trees we encounter
    """
    trees_encountered = j = 0
    tree = "#"
    for i in range(0, len(arr), down):
        if arr[i][j % len(arr[0])] == tree:
            trees_encountered += 1
        j += right
    return trees_encountered

x1 = num_gen_trees(arr, right=1, down=1)
x2 = num_gen_trees(arr, right=3, down=1)
x3 = num_gen_trees(arr, right=5, down=1)
x4 = num_gen_trees(arr, right=7, down=1)
x5 = num_gen_trees(arr, right=1, down=2)

print("Part 2:", x1, x2, x3, x4, x5, x1 * x2 * x3 * x4 * x5)