import re
from functools import reduce

with open('input/7.txt') as file:
    content = file.read()

lines = content.splitlines()

pattern_parent = re.compile(r'^([a-z]+ [a-z]+) bags contain ')
pattern_children = re.compile(r'([0-9]+) ([a-z]+ [a-z]+) bags?')

bags = {}

for line in lines:
    match_parent = pattern_parent.match(line)
    color_parent = match_parent.groups()[0]

    match_children = pattern_children.findall(line)

    bags[color_parent] = {match[1]: int(match[0]) for match in match_children}


def has_color(color_parent: str, color_has: str) -> bool:
    children_colors = bags[color_parent].keys()

    if color_has in children_colors:
        return True

    return any(has_color(color, color_has) for color in children_colors)


my_color = 'shiny gold'
n_possible_parents = 0

for color in bags.keys():
    if has_color(color, my_color):
        n_possible_parents += 1

print(f'Bags which can contain a {my_color} bag: {n_possible_parents}')
# Part 2


def children_bags(color: str) -> int:
    return 1 + sum(n * children_bags(c) for c, n in bags[color].items())


n_children_bags = children_bags(my_color) - 1
print(f'Bags contained in a {my_color} bag: {n_children_bags}')
