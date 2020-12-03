from typing import Tuple

import numpy as np

with open('input/3.txt') as file:
    content = file.read()

inputs = content.splitlines()

data = np.array(list(map(list, inputs)))
data = data == '#'

height, width = data.shape


def get_slope(x_step: int, y_step: int) -> Tuple[np.ndarray, np.ndarray]:
    x = np.arange(height, step=x_step)
    y = x//x_step * y_step % width
    return x, y


x, y = get_slope(1, 3)

trees = np.sum(data[x, y])

print(f'Trees with slope 1x3: {trees}')

# Step 2

mult_result = 1
for x_step, y_step in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
    x, y = get_slope(x_step, y_step)
    trees = np.sum(data[x, y])
    mult_result *= int(trees)

print(f'Tree multiplication of all slopes: {mult_result}')
