from typing import Tuple

import numpy as np
import pandas as pd

with open('input/5.txt') as file:
    content = file.read()

seats = content.splitlines()


def convert_seat(raw: str) -> Tuple[int, int]:
    row = raw[:7]
    col = raw[7:]

    row = row.replace('F', '0').replace('B', '1')
    col = col.replace('L', '0').replace('R', '1')

    row = int(row, 2)
    col = int(col, 2)

    return row, col


hightest_id = -1

all_seats = pd.Series(False, pd.Index(np.arange(128 * 8)))

for seat in seats:
    row, col = convert_seat(seat)

    id = row * 8 + col

    all_seats[id] = True

    if id > hightest_id:
        hightest_id = id

print(f'Highest id: {hightest_id}')

taken = all_seats[all_seats == True].index
first_taken = taken.min()
last_taken = taken.max()

all_seats_filtered = all_seats[first_taken:last_taken]

your_seat = all_seats_filtered[all_seats_filtered == False].index

print(f'Your seat: {your_seat[0]}')
