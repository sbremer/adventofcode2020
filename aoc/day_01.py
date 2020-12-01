from itertools import combinations

with open('input/1.txt') as file:
    content = file.read()

inputs = list(map(int, content.splitlines()))

pairs = combinations(inputs, 2)

x, y = next((x, y) for x, y in pairs if x + y == 2020)

print(f'Solution is {x*y}')

# Part 2
pairs = combinations(inputs, 3)

x, y, z = next((x, y, z) for x, y, z in pairs if x + y + z == 2020)

print(f'Solution is {x*y*z}')
