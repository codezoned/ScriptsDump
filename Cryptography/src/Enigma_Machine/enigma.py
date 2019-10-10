import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
seeds = [476514654, 845147865, 147865134, 1468513476, 8461568]


def shuffle(seed, letter):
    random.seed(seeds[seed])
    keys = alphabet
    random.shuffle(keys)
    keymap = {}
    for j in range(26):
        keymap[keys[j]] = keys[(j + 1) * -1]
    return keymap[letter]


string = "uxdioleizdnh bg axnw"
message = string.split()
new_message = ""
for string in message:
    new_string = ""
    for character in range(len(string)):
        new_string += shuffle(character % len(seeds), string[character])
    new_message += new_string + " "
print new_message
