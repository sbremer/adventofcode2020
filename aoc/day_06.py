from functools import reduce

with open('input/6.txt') as file:
    content = file.read()

# For windows
content = content.replace('\r', '')

entries = content.split('\n\n')

total_yes = 0

for entry in entries:
    yes_answers = set(list(entry.replace('\n', '')))
    n_yes = len(yes_answers)
    total_yes += n_yes

print(f'Total yes answers summed: {total_yes}')

# Part 2
total_yes = 0

for entry in entries:
    yes_answers = reduce(lambda x, y: x.intersection(y), [set(answers) for answers in entry.splitlines()])
    n_yes = len(yes_answers)
    total_yes += n_yes

print(f'Total yes answers summed (Part 2): {total_yes}')
