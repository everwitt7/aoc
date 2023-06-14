import ctypes

# circuit instruction set for 16 bit signals
AND = " AND "
OR = " OR "
LSHIFT = " LSHIFT "
RSHIFT = " RSHIFT "
NOT = "NOT "
BIT_LENGTH = 16

# represent most significant bit at index 0, LSB at index 15
# this bit shifting, is technicaly agnostic to bit array length
def lshift(bits, num):
    bits[:len(bits)-num] = bits[num:]
    bits[len(bits)-num:] = [0 for _ in range(num)]
    return bits

def rshift(bits, num):
    bits[num:] = bits[:len(bits)-num]
    bits[:num] = [0 for _ in range(num)]
    return bits

# convert literal into bit array before
def bit_and(bits1, bits2):
    if len(bits1) != len(bits2):
        print(f"Bit Array Length Mismath, {len(bits1)=}, {len(bits2)=}")
    and_arr = [0 for _ in range(len(bits1))]

    for idx in range(len(bits1)):
        and_arr[idx] = bits1[idx] & bits2[idx]

    return and_arr




def parser(file: str):
    contents = []
    with open(file, "r") as f:
        for line in file:
            contents.append(line.rstrip())
    return contents 

def one(contents: list):
    """
    signals can come BEFORE they get a value
        - lookup signal, if it does not exist pass 0
    we can AND (or other gates) with a literal instead of a signal
        - check if `int(left/right)` is possible
    16 bit representation for LSHIFT
        - make an array of bits of length 16?
    """
    signals = {}
    for line in contents: 
        input, output = line.split(" -> ")

        if AND in input:
            sig1, sig2 = input.split(AND)
            # signals[output] = signals[sig1].value & signals[sig2].value
            signals[output] = signals[sig1] & signals[sig2]
        elif OR in input:
            sig1, sig2 = input.split(OR)
            signals[output] = signals[sig1] | signals[sig2]
        elif LSHIFT in input:
            sig, num = input.split(LSHIFT)
            signals[output] = signals[sig] << int(num) 
        elif RSHIFT in input:
            sig, num = input.split(RSHIFT)
            signals[output] = signals[sig] >> int(num) 
        elif NOT in input:
            sig = input.split(NOT)[-1]
            # deal with twos complement to make it unsigned
            signals[output] = ~signals[sig] & 0xFFFF
        else:
            # set the value of the signal
            # bit_rep = ctypes.c_uint16(int(input))
            # signals[output] = bit_rep
            signals[output] = int(input)

    return signals

def two():
    pass

def test_lshift():
    test = [1, 1, 1, 1,
                0, 0, 0, 0,
                0, 0, 0, 0,
                1, 1, 1, 1]

    assert lshift(test, 5) == [0, 0, 0, 0,
                                   0, 0, 0, 1,
                                   1, 1, 1, 0,
                                   0, 0, 0, 0]

def test_rshift():
    test = [1, 1, 1, 1,
                0, 0, 0, 0,
                0, 0, 0, 0,
                1, 1, 1, 1]

    assert rshift(test, 3) == [0, 0, 0, 1,
                                   1, 1, 1, 0,
                                   0, 0, 0, 0,
                                   0, 0, 0, 1]

def test_and():
    t_one = [0, 0, 1, 1]
    t_two = [0, 1, 0, 1]
    t_ans = bit_and(t_one, t_two)

    assert t_ans == [0, 0, 0, 1]


if __name__ == "__main__":
    file = "./inputs/p07.txt"
    contents = parser(file)

    sample = ["123 -> x",
              "456 -> y",
              "x AND y -> d",
              "x OR y -> e",
              "x LSHIFT 2 -> f",
              "y RSHIFT 2 -> g",
              "NOT x -> h",
              "NOT y -> i"]

    signals = {}

    for line in sample:
        input, output = line.split(" -> ")

        if AND in input:
            sig1, sig2 = input.split(AND)
            # signals[output] = signals[sig1].value & signals[sig2].value
            signals[output] = signals[sig1] & signals[sig2]
        elif OR in input:
            sig1, sig2 = input.split(OR)
            signals[output] = signals[sig1] | signals[sig2]
        elif LSHIFT in input:
            sig, num = input.split(LSHIFT)
            signals[output] = signals[sig] << int(num) 
        elif RSHIFT in input:
            sig, num = input.split(RSHIFT)
            signals[output] = signals[sig] >> int(num) 
        elif NOT in input:
            sig = input.split(NOT)[-1]
            # deal with twos complement to make it unsigned
            signals[output] = ~signals[sig] & 0xFFFF
        else:
            # set the value of the signal
            # bit_rep = ctypes.c_uint16(int(input))
            # signals[output] = bit_rep
            signals[output] = int(input)

    # print(signals)

    # syms = one(contents)
    # print(syms['a'])

    test_lshift()
    test_rshift()
    test_and()


