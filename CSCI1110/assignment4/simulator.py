import sys

OPSYMBOLS = {
    0: "LOAD",
    1: "STORE",
    2: "CLEAR",
    3: "ADD",
    4: "INCREMENT",
    5: "SUBTRACT",
    6: "DECREMENT",
    7: "COMPARE",
    8: "JUMP",
    9: "JUMPGT",
    10: "JUMPEQ",
    11: "JUMPLT",
    12: "JUMPNEQ",
    13: "IN",
    14: "OUT",
    15: "HALT",
}


def main():

    pc = 0
    ir = 0
    lt = False
    eq = False
    gt = False
    r = 0

    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = input("Binary text file: ")
    mem = read_bin_text(filepath)
    if len(sys.argv) == 1:
        step = input("Do you wish to step slowly (y/n): ").upper() == "Y"
    else:
        step = len(sys.argv) > 2 and sys.argv[2] == "-s"
    print()

    while True:

        if step:
            print_system_state(pc, ir, lt, eq, gt, r, mem)
            input("\n***ENTER TO FETCH***\n")

        # fetch
        ir = mem[pc]
        pc += 1

        if step:
            print_system_state(pc, ir, lt, eq, gt, r, mem)
            input("\n***ENTER TO DECODE***\n")

        opcode = ir >> 12
        if opcode < 0:
            opcode += 2**4
        address = ir & 0b0000111111111111
        if address > len(mem):
            print(
                f"Error: Attempt to access address {address} outside of allocated memory."
            )
            sys.exit(1)

        if step:
            print(f"IR decoded as {OPSYMBOLS[opcode]} {address}")
            input("\n***ENTER TO EXECUTE***\n")

        # load
        if opcode == 0:
            r = mem[address]
        # store
        elif opcode == 1:
            mem[address] = r
        # clear
        elif opcode == 2:
            mem[address] = 0
        # add
        elif opcode == 3:
            r += mem[address]
        # increment
        elif opcode == 4:
            mem[address] += 1
        # subtract
        elif opcode == 5:
            r -= mem[address]
        # decrement
        elif opcode == 6:
            mem[address] -= 1
        # compare
        elif opcode == 7:
            lt = r < mem[address]
            eq = r == mem[address]
            gt = r > mem[address]
        # jump
        elif opcode == 8:
            pc = address
        # jumpgt
        elif opcode == 9:
            if gt:
                pc = address
        # jumpeq
        elif opcode == 10:
            if eq:
                pc = address
        # jumplt
        elif opcode == 11:
            if lt:
                pc = address
        # jumpneq
        elif opcode == 12:
            if not eq:
                pc = address
        # in
        elif opcode == 13:
            mem[address] = get_int_input()
            print()
        # out
        elif opcode == 14:
            print(f"System output: {mem[address]}\n")
        # halt
        elif opcode == 15:
            break


def get_int_input():
    min_val = -(2**15)
    max_val = (2**15) - 1
    while True:
        try:
            user_int = int(input("Provide integer input: "))
            if user_int > max_val:
                print(f"Invalid input, maximum value is {max_val}.")
            elif user_int < min_val:
                print(f"Invalid input, minimum value is {min_val}.")
            else:
                return user_int

        except ValueError:
            print("Invalid input, enter an integer.")


def int_to_16b_2s_bitstring(the_int):
    if the_int < 0:
        bitstring = "1"
        the_int += 2**15
    else:
        bitstring = "0"
    for n in range(14, -1, -1):
        place = 2**n
        if place <= the_int:
            bitstring += "1"
            the_int -= place
        else:
            bitstring += "0"
    assert the_int == 0
    return bitstring


def read_bin_text(filepath):
    try:
        with open(filepath) as fin:
            bin_text = fin.readlines()
    except FileNotFoundError:
        print(f'Error: No file "{filepath}" found.')
        sys.exit(1)

    bin_vals = []

    line_number = 1
    for line in bin_text:
        line = line.rstrip()
        if len(line) != 16 or len(set(line) - {"0", "1"}) != 0:
            print(f"Error: Line {line_number} malformed.")
            sys.exit(1)

        uns_val = int(line, 2)

        if uns_val < (2**15):
            bin_vals.append(uns_val)
        # convert to 2's
        else:
            bin_vals.append(uns_val - (2**16))
        line_number += 1

    return bin_vals


def print_system_state(pc, ir, lt, eq, gt, r, mem):
    print(f"PC:\t{int_to_16b_2s_bitstring(pc)} ({pc})")
    print(f"IR:\t{int_to_16b_2s_bitstring(ir)} ({ir})")
    print(f"LT:\t{lt}")
    print(f"EQ:\t{eq}")
    print(f"GT:\t{gt}")
    print(f"R:\t{int_to_16b_2s_bitstring(r)} ({r})")
    print("MEMORY:")
    for addr in range(len(mem)):
        print(f"M[{addr}]:\t{int_to_16b_2s_bitstring(mem[addr])} ({mem[addr]})")


if __name__ == "__main__":
    main()
