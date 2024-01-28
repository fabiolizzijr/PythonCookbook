# Caesar Cypher example from Practical Cryptography in Python
# ============================================================
# Partial listing: Some assembly is required

import string


def create_shift_substitutions(n):
    encoding = {}
    decoding = {}
    alphabet_size = len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter       = string.ascii_uppercase[i]
        subst_letter = string.ascii_uppercase[(i+n) % alphabet_size]

        encoding[letter] = subst_letter
        decoding[subst_letter] = letter
    return encoding, decoding


# Encode takes a message and a subst dictionary
def encode(message, subst):
    cypher = ""
    # For each letter in message, subst if possible
    for letter in message:
        if letter in subst:
            cypher += subst[letter]
        # If It can't transform, include character itself (blank and lines)
        else:
            cypher += letter
    return cypher


# Decode function works the same, only subst dictionary needs to change
def decode(message, subst):
    return encode(message, subst)


def printable_substitution(subst):
    # Sort by source characters so things are alphabetized.
    mapping = sorted(subst.items())

    # Then create two lines, SOURCE above, TARGET beneath.
    alphabet_line = " ".join(letter for letter, _ in mapping)
    cypher_line = " ".join(subst_letter for _, subst_letter in mapping)
    return "{}\n{}".format(alphabet_line, cypher_line)


if __name__ == "__main__":
    n = 1
    encoding, decoding = create_shift_substitutions(n)
    while True:
        print("\nShift Encoder Decoder")
        print("------------------------")
        print("\tCurrent Shift: {}\n".format(n))
        print("\t1. Print Encoding/Decoding Tables.")
        print("\t2. Encode Message.")
        print("\t3. Decode Message.")
        print("\t4. Change Shift.")
        print("\t5. Quit.\n")
        choice = input(">> ")
        print()

        if choice == '1':
            print("Encoding Table:")
            print(printable_substitution(encoding))
            print("Decoding Table:")
            print(printable_substitution(decoding))

        elif choice == '2':
            message = input("\nMessage to encode: ")
            print("Encoded Message: {}".format(encode(
                message.upper(), encoding)))

        elif choice == '3':
            message = input("\nMessage to decode: ")
            print("Decoded Message: {}".format(decode(
                message.upper(), decoding)))

        elif choice == '4':
            new_shift = input("\nNew shift (currently {}): ".format(n))
            try:
                new_shift = int(new_shift)
                if new_shift < 1:
                    raise Exception("Shift must be greater than 0")
            except ValueError:
                print("Shift {} is not a valid number.".format(new_shift))
            else:
                n = new_shift
                encoding, decoding = create_shift_substitutions(n)

        elif choice == '5':
            print("\nTerminating. The program will self destroy in 5 "
                  "seconds. \n")
            break

        else:
            print("Unknown option {}.".format(choice))
