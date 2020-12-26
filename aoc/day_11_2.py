from itertools import product

import numpy as np

with open('input/11.txt') as file:
    content = file.read()

seats = (np.array(list(map(list, content.splitlines()))) == 'L') * -1.0

ny, nx = seats.shape

directions = list(product([-1, 0, 1], repeat=2))
directions.remove((0, 0))
directions = np.array(directions)

seat_loopup = {}

for x in range(nx):
    for y in range(ny):

        pos = np.array([x, y])
        seats_to_check = []

        for direction in directions:

            seat_to_check = None

            pos_check = pos + direction
            while 0 <= pos_check[0] < nx and 0 <= pos_check[1] < ny:
                if seats[pos_check[1], pos_check[0]] == -1:
                    seat_to_check = pos_check
                    break
                pos_check += direction

            if seat_to_check is not None:
                seats_to_check.append(seat_to_check)

        seat_loopup[(x, y)] = seats_to_check


seats_next = seats.copy()
at = 0

while True:
    at += 1

    for x in range(nx):
        for y in range(ny):
            seat = seats[y, x]
            n_occupied = 0
            for seat_pos in seat_loopup[(x, y)]:
                n_occupied += seats[seat_pos[1], seat_pos[0]] == 1

            if seat == -1 and n_occupied == 0:
                seats_next[y, x] = 1.0
            elif seat == 1 and n_occupied >= 5:
                seats_next[y, x] = -1.0

    if (seats == seats_next).all():
        break

    seats = seats_next.copy()

n_occupied = (seats_next == 1).sum().sum()
print(f'Stable after {at} iterations with {n_occupied} seats occupied')
