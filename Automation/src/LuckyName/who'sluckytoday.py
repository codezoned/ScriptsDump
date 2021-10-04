import random

ran = []

group = [i for i in range(1,50)]
random.shuffle(group)
ran = group[:6]

print("Here are your 'lucky dip' numbers:")
print(ran)
print("Remember to split any winnings with me!")
print("Happy Coding!")
