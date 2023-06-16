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
def lshift(obits, num):
    bits = obits[:]
    if isinstance(num, str):
        num = int(num)
    bits[:len(bits)-num] = bits[num:]
    bits[len(bits)-num:] = [0 for _ in range(num)]
    return bits

def rshift(obits, num):
    bits = obits[:]
    if isinstance(num, str):
        num = int(num)
    bits[num:] = bits[:len(bits)-num]
    bits[:num] = [0 for _ in range(num)]
    return bits

# convert literal into bit array before
def bit_and(bits1, bits2):
    if len(bits1) != len(bits2):
        print(f"Bit Array Length Mismath, {len(bits1)=}, {len(bits2)=}")
    arr = [0 for _ in range(len(bits1))]

    for idx in range(len(bits1)):
        arr[idx] = bits1[idx] & bits2[idx]

    return arr

def bit_or(bits1, bits2):
    if len(bits1) != len(bits2):
        print(f"Bit Array Length Mismath, {len(bits1)=}, {len(bits2)=}")
    arr = [0 for _ in range(len(bits1))]

    for idx in range(len(bits1)):
        arr[idx] = bits1[idx] | bits2[idx]

    return arr

def bit_not(bits):
    # XOR so 1 XOR 1 = 0 and 0 ^ 1 = 1... we can use xor to not a bit
    arr = [bits[i] ^ 1 for i in range(len(bits))]
    return arr

def int_to_bits(num: int):
    if isinstance(num, str):
        num = int(num)
    if num > 65535:
        print(f"{num=} larger than unsigned 16 bit int")
    return [(num >> i) & 1 for i in range(BIT_LENGTH-1, -1, -1)]

def bits_to_int(bits):
    num = 0
    for i in range(BIT_LENGTH):
        num += pow(2, BIT_LENGTH-1-i) * bits[i]
    return num

def parser(file: str):
    contents = []
    with open(file, "r") as f:
        for line in f:
            contents.append(line.rstrip())
    return contents 

def one(contents: list, signals: dict):
    """
    signals can come BEFORE they get a value
        - lookup signal, if it does not exist pass 0
    we can AND (or other gates) with a literal instead of a signal
        - check if `int(left/right)` is possible
    16 bit representation for LSHIFT
        - make an array of bits of length 16?
    """

    for line in contents: 
        input, output = line.split(" -> ")
        # print(line)
        # print(signals)

        # its possible to have a literal instead of a signal as an argument
        # 1 AND cc -> cd
        if AND in input:
            # use string.isnumeric() to check if literal or signal
            sig1, sig2 = input.split(AND)

            if sig1.isnumeric() and sig2.isnumeric():
                signals[output] = bit_and(int_to_bits(sig1), int_to_bits(sig2))
            elif sig1 in signals and sig2.isnumeric():
                signals[output] = bit_and(signals[sig1], int_to_bits(sig2))
            elif sig1.isnumeric() and sig2 in signals:
                signals[output] = bit_and(int_to_bits(sig1), signals[sig2])
            elif sig1 in signals and sig2 in signals:
                signals[output] = bit_and(signals[sig1], signals[sig2])

        elif OR in input:
            sig1, sig2 = input.split(OR)
            
            if sig1.isnumeric() and sig2.isnumeric():
                signals[output] = bit_or(int_to_bits(sig1), int_to_bits(sig2))
            elif sig1 in signals and sig2.isnumeric():
                signals[output] = bit_or(signals[sig1], int_to_bits(sig2))
            elif sig1.isnumeric() and sig2 in signals:
                signals[output] = bit_or(int_to_bits(sig1), signals[sig2])
            elif sig1 in signals and sig2 in signals:
                signals[output] = bit_or(signals[sig1], signals[sig2])

        elif LSHIFT in input:
            sig, num = input.split(LSHIFT)

            if sig in signals:
                signals[output] = lshift(signals[sig], num)

        elif RSHIFT in input:
            sig, num = input.split(RSHIFT)

            if sig in signals:
                signals[output] = rshift(signals[sig], num)

        elif NOT in input:
            sig = input.split(NOT)[-1]

            if sig in signals:
                signals[output] = bit_not(signals[sig])

        else:
            # set the value of the signal, `0 -> c`
            if input.isnumeric():
                signals[output] = int_to_bits(input)
            else:
                if input in signals:
                    signals[output] = signals[input]

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

def test_or():
    t_one = [0, 0, 1, 1]
    t_two = [0, 1, 0, 1]
    t_ans = bit_or(t_one, t_two)

    assert t_ans == [0, 1, 1, 1]

def test_not():
    test = [0, 1, 0, 1]
    ans = bit_not(test)
    assert ans == [1, 0, 1, 0]

def test_int_to_bits():
    test = 49372
    ans = int_to_bits(test)
    assert ans == [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0]

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

    # I misunderstood - `a gate provides no signal until all of its inputs have a signal`
    # means as soon as the inputs have a value, the output then gets a value, and this
    # chain occurs until every wire has a value, otherwise you get like 6 wires with
    # values, which is what I was seeing
    signals = {}
    while 'a' not in signals:
        signals = one(contents, signals)

    for k, v in signals.items():
        signals[k] = bits_to_int(v)

    print(signals['a'])

    test_lshift()
    test_rshift()
    test_and()
    test_or()
    test_not()


