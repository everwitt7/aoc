"""Advent of Code 2020: Problem 4"""
import re

def parser(content):
    return dict(re.findall(r'([a-z]+):([^\s]+)', content))

def get_data(parser=str, sep="\n"):
    # Passports are separated by blank lines.
    with open ("./inputs/p04.txt", "r") as f:
        contents = f.read().strip().split(sep)
        arr = [parser(content) for content in contents]
    return arr

arr = get_data(parser=parser, sep="\n\n")

# Part 1
def num_val_pports(arr: list[dict]) -> int:
    n_val = 0
    keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} # this defines a set
    for d in arr:
        if  keys.issubset(d.keys()): # a good way to check if a set contains another set
            n_val += 1
    return n_val

n_val = num_val_pports(arr)
print("Part 1:", n_val)

# Part 2
validator = dict(
    byr=lambda v: 1920 <= int(v) <= 2002,
    iyr=lambda v: 2010 <= int(v) <= 2020,
    eyr=lambda v: 2020 <= int(v) <= 2030,
    hgt=lambda v: (v[-2] == "in" and 59 <= int(v[:-2]) <= 76) or (v[-2] == "cm" and 150 <= int(v[:-2]) <= 193),
    hcl=lambda v: re.match('^#[0-9a-f]{6}$', v),
    ecl=lambda v: re.match('^amb|blu|brn|gry|grn|hzl|oth$', v),
    pid=lambda v: re.match('^[0-9]{9}$', v)
)

def n_val_pass(arr, val):
    n_val = 0
    keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    for d in arr:
        if keys.issubset(d.keys()):
            if all(val[k](d[k]) for k in keys):
                n_val += 1
    return n_val

n_val = n_val_pass(arr, validator)
print("Part 2:", n_val)



