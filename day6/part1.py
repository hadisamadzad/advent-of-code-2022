f = open("input.txt", "r")
# f = open("demo-input.txt", "r")

lines = f.readlines()

for index, row in enumerate(lines):
    lines[index] = row.replace('\n', '')

stream = lines[0]

marker = 0
key_length = 4
for index in range(len(stream)):
    marker = key_length + (index)
    _1st = stream[index + 0]
    _2nd = stream[index + 1]
    _3rd = stream[index + 2]
    _4th = stream[index + 3]

    if _1st != _2nd and _1st != _3rd and _1st != _4th and _2nd != _3rd and _2nd != _4th and _3rd != _4th:
        break

print(marker)