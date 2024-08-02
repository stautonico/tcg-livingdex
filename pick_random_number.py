import os
from random import choice

has = os.listdir("images")

pool = [x for x in range(1, 1025 + 1)]

for h in has:
    pool.remove(int(h))



print(f"Cards left: {len(pool)}")

#print(choice(pool))
