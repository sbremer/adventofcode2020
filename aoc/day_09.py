from itertools import combinations
from typing import List, Iterable

with open('input/9.txt') as file:
    content = file.read()

numbers = list(map(int, content.splitlines()))

cur = numbers[:25]

at = 25


def number_works(number: int, available: List[int]) -> bool:
    for a, b in combinations(available, 2):
        if a + b == number:
            return True
    return False


while at < len(numbers):
    number = numbers[at]

    if not number_works(number, cur):
        print(f'First number to not work: {number}!')
        break

    cur[at % 25] = number
    at += 1

# == Part 2


def build_cont_numbers(n: int) -> Iterable[int]:
    for i in range(len(numbers) - n):
        yield numbers[i:i+n]


done = False
for a in range(2, len(numbers)):
    for number_range in build_cont_numbers(a):
        s = sum(number_range)
        if s == number:
            print(f'Found a match for range {number_range}')
            min_max = min(number_range) + max(number_range)
            print(f'Resulting sum of min and max: {min_max}')
            done = True
            break

    if done:
        break
