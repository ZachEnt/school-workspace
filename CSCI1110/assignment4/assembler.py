import sys

OPCODES = {
    "LOAD": "0000",
    "STORE": "0001",
    "CLEAR": "0010",
    "ADD": "0011",
    "INCREMENT": "0100",
    "SUBTRACT": "0101",
    "DECREMENT": "0110",
    "COMPARE": "0111",
    "JUMP": "1000",
    "JUMPGT": "1001",
    "JUMPEQ": "1010",
    "JUMPLT": "1011",
    "JUMPNEQ": "1100",
    "IN": "1101",
    "OUT": "1110",
    "HALT": "1111",
}


def main():

    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = input("Assembly source file: ")
    try:
        with open(filepath) as fin:
            source = fin.readlines()
    except FileNotFoundError:
        print(f'Error: No file "{filepath}" found.')
        return

    labels = {}

    line_number = 1
    memory_address = 0
    for line in source:
        if "/" in line:
            line = line[: line.index("/")]
        line = line.strip()
        if line != "":
            if ":" in line:
                label = line[: line.index(":")]
                if len(label.split()) > 1:
                    print(f'Error: Invalid label "{label}" on line {line_number}.')
                    return
                if label in labels:
                    print(f'Error: Redundant label "{label}" on line {line_number}.')
                    return
                else:
                    labels[label] = memory_address
            memory_address += 1

        line_number += 1

    bin_text = []

    line_number = 1
    for line in source:
        if "/" in line:
            line = line[: line.index("/")]
        line = line.strip()
        if line != "":
            if ":" in line:
                line = line[line.index(":") + 1 :]
            tokens = line.split()

            op_name = tokens[0].upper()
            if op_name not in OPCODES and op_name != ".DATA":
                print(
                    f'Error: Unknown operation/directive "{op_name}" on line {line_number}.'
                )
                return
            elif op_name == "HALT" and len(tokens) > 1:
                print(f"Error: HALT given unneeded arguments on line {line_number}.")
                return
            elif op_name != "HALT" and len(tokens) < 2:
                print(
                    f"Error: {op_name} missing needed argument on line {line_number}."
                )
                return
            elif op_name != "HALT" and len(tokens) > 2:
                print(f"Error: {op_name} given extra arguments on line {line_number}.")
                return

            if op_name == ".DATA":
                try:
                    int_val = int(tokens[1])
                except ValueError:
                    print(
                        f'Error: .DATA received non-integer argument "{tokens[1]}" on line {line_number}.'
                    )
                    return

                if int_val < -(2**15) or int_val >= (2**15):
                    print(
                        f"Error: .DATA value {int_val} on line {line_number} out of range."
                    )
                    return

                bin_text.append(int_to_16b_2s_bitstring(int_val))

            elif op_name == "HALT":
                bin_text.append(OPCODES["HALT"] + ("0" * 12))

            else:
                if tokens[1] not in labels:
                    print(f'Error: Unknown label "{tokens[1]}" on line {line_number}.')
                    return
                address = labels[tokens[1]]
                opcode = OPCODES[op_name]
                address_bits = int_to_12b_uns_bitstring(address)
                bin_text.append(opcode + address_bits)
        line_number += 1

    if len(sys.argv) > 2:
        with open(sys.argv[2], "w") as fout:
            for line in bin_text:
                fout.write(line)
                fout.write("\n")
    else:
        for line in bin_text:
            print(line)


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


def int_to_12b_uns_bitstring(the_int):
    bitstring = ""
    for n in range(11, -1, -1):
        place = 2**n
        if place <= the_int:
            bitstring += "1"
            the_int -= place
        else:
            bitstring += "0"
    assert the_int == 0
    return bitstring


if __name__ == "__main__":
    main()
