import itertools
import operator
from functools import lru_cache, reduce

import numpy as np

with open('input/10.txt') as file:
    content = file.read()

adapters = list(map(int, content.splitlines()))
joltage = np.array(sorted(adapters + [0, max(adapters) + 3]))

differences = joltage[1:] - joltage[:-1]

diff_1 = np.sum(differences == 1)
diff_3 = np.sum(differences == 3)

print(f'Product of number of 1-step and 3-step joltages: {diff_1 * diff_3}')


@lru_cache
def possibilities(n: int) -> int:

    if n == 0:
        return 1

    elif n <= 2:
        return n

    return possibilities(n-3) + possibilities(n-2) + possibilities(n-1)


blocks_of_1 = [len(list(iterator))
               for value, iterator in itertools.groupby(differences == 1, lambda x: x)
               if value == True]

n_possibilities = reduce(operator.mul, map(possibilities, blocks_of_1))

print(f'Number of possibilities: {n_possibilities}')
