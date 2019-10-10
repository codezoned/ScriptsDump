import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
seeds = [476514654, 845147865, 147865134, 1468513476, 8461568]


def shuffle(seed, letter):
    random.seed(seeds[seed])
    if letter.islower():
        keys = alphabet
    else:
        keys = alphabet2
    random.shuffle(keys)
    keymap = {}
    for j in range(26):
        keymap[keys[j]] = keys[(j + 1) * -1]
    return keymap[letter]


string = raw_input()
message = string.split()
new_string = new_message = ""
for string in message:
    for character in range(len(string)):
        try:
            new_string += shuffle(character % len(seeds), string[character])
        except LookupError:
            new_string += string[character]
    new_message += new_string + " "
    new_string = ""
print new_message
