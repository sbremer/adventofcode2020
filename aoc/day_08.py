from typing import List, Optional

with open('input/8.txt') as file:
    content = file.read()

lines = content.splitlines()

acc_by_line_exe = {}
acc = 0
at = 0

while True:
    if at in acc_by_line_exe.keys():
        break

    acc_by_line_exe[at] = acc

    line = lines[at]
    cmd, value = line.split(' ')

    if cmd == 'acc':
        acc += int(value)
        at += 1
    elif cmd == 'jmp':
        at += int(value)
    else:
        at += 1

print(f'Acc just before second execution: {acc}')

# == Part 2


def does_terminate(lines: List[str]) -> Optional[int]:
    acc_by_line_exe = {}
    acc = 0
    at = 0

    while True:
        if at in acc_by_line_exe.keys():
            return None
        if at == len(lines):
            return acc

        acc_by_line_exe[at] = acc

        line = lines[at]
        cmd, value = line.split(' ')

        if cmd == 'acc':
            acc += int(value)
            at += 1
        elif cmd == 'jmp':
            at += int(value)
        else:
            at += 1


acc_terminates = None
for i in range(len(lines)):

    if lines[i].startswith('acc'):
        continue

    lines_altered = lines.copy()

    if lines[i].startswith('nop'):
        lines_altered[i] = lines_altered[i].replace('nop', 'jmp')
    elif lines[i].startswith('jmp'):
        lines_altered[i] = lines_altered[i].replace('jmp', 'nop')

    acc = does_terminate(lines_altered)
    if acc is not None:
        acc_terminates = acc
        break

print(f'Acc of terminating switch: {acc_terminates}')
