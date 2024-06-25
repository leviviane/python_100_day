#create a heads or tails exercise

import random

random_num = random.randint(0, 1)
print(random_num)

if random_num == 1:
    print("Heads")
else:
    print("Tails")
