
import numpy as np
from scipy import ndimage as ndi
from llc import jit_filter_function

with open('input/11.txt') as file:
    content = file.read()

seats = (np.array(list(map(list, content.splitlines()))) == 'L') * -1.0


@jit_filter_function
def change(neighbors):
    seat = neighbors[4]
    if seat == 0:
        return 0.0

    n_occupied = (neighbors == 1).sum() - (seat == 1)

    if seat == -1 and n_occupied == 0:
        return 1.0
    elif seat == 1 and n_occupied >= 4:
        return -1.0
    else:
        return seat


fp = np.ones((3, 3))
at = 0

while True:
    at += 1
    if at%20 == 0:
        print(f'At iteration {at}', end='\r', flush=True)

    seats_next = ndi.generic_filter(seats, change, footprint=fp, mode='constant')

    # print('_______')
    # for y in range(seats_next.shape[1]):
    #     row = seats_next[y, :]
    #     to_string = lambda x: '#' if x == 1 else '.' if x == 0 else 'L'
    #     print(''.join(map(to_string, row)))

    if (seats == seats_next).all():
        break

    seats = seats_next

n_occupied = (seats_next == 1).sum().sum()
print(f'Stable after {at} iterations with {n_occupied} seats occupied')
