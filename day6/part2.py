f = open("input.txt", "r")
# f = open("demo-input.txt", "r")

lines = f.readlines()

for index, row in enumerate(lines):
    lines[index] = row.replace('\n', '')

stream = lines[0]

marker = 0
key_length = 14
for index in range(len(stream) - key_length):
    marker = key_length + (index)
    
    marker_found = True
    for i in range(key_length):
        for j in range(i + 1, key_length):
            one = stream[index + i]
            two = stream[index + j]
            if one == two:
                marker_found = False
                break
    
    if marker_found:
        break

print(marker)