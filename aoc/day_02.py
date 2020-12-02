import re

with open('input/2.txt') as file:
    content = file.read()

inputs = content.splitlines()

pattern = re.compile(r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')

valid = 0

for line in inputs:
    match = pattern.findall(line)[0]

    letter = match[2]
    min_occur = int(match[0])
    max_occur = int(match[1])

    pw = match[3]

    if min_occur <= pw.count(letter) <= max_occur:
        valid += 1

print(f'Number of valid: {valid}')

# Part 2
valid = 0

for line in inputs:
    match = pattern.findall(line)[0]

    letter = match[2]
    pos1 = int(match[0]) - 1
    pos2 = int(match[1]) - 1

    pw = match[3]

    if (pw[pos1] == letter) != (pw[pos2] == letter):
        valid += 1

print(f'Part 2: Number of valid: {valid}')
