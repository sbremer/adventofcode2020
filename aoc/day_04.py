import re

with open('input/4.txt') as file:
    content = file.read()

# For windows
content = content.replace('\r', '')

entries = content.split('\n\n')

passports = []

for entry in entries:
    kvs = entry.replace('\n', ' ').split(' ')
    passport = {}
    for kv in kvs:
        k, v = kv.split(':')
        passport[k] = v

    passports.append(passport)

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
# not cid

valid = sum([1 if all(key in passport.keys() for key in required_fields) else 0 for passport in passports])

print(f'Found {valid} "valid" passports')


def validate_hgt(v: str) -> bool:
    unit = v[-2:]
    value = int(v[:-2])
    if unit == 'cm':
        return 150 <= value <= 193
    elif unit == 'in':
        return 59 <= value <= 76
    return False

validators = {
    'byr': lambda v: 1920 <= int(v) <= 2002,
    'iyr': lambda v: 2010 <= int(v) <= 2020,
    'eyr': lambda v: 2020 <= int(v) <= 2030,
    'hgt': validate_hgt,
    'hcl': lambda v: re.match(r'^#[0-9a-f]{6}$', v) is not None,
    'ecl': lambda v: v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda v: re.match(r'^[0-9]{9}$', v) is not None,
}

valid = 0

for passport in passports:
    is_valid = True
    for key, fun_valid in validators.items():
        try:
            if not fun_valid(passport[key]):
                is_valid = False
                break
        except:
            is_valid = False
            break

    if is_valid:
        valid += 1

print(f'Found {valid} "valid" passports (with content validation)')
