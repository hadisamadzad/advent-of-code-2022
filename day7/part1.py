f = open("input.txt", "r")
# f = open("demo-input.txt", "r")

lines = f.readlines()

for index, row in enumerate(lines):
    lines[index] = row.replace('\n', '')

files = []
dirs = []
cwd = ''

for line in lines:
    is_command = line[0] == '$'
    if is_command:
        command = line.split(' ')[1]

        if command == 'cd':
            value = line.split(' ')[2]
            if value == '/':
                cwd = '/'
            elif value == '..':
                cwd = '/' + '/'.join(cwd.split('/')[1: -2]) + '/'
                cwd = cwd.replace('//','/')
            else:
                cwd += value + '/'

        elif command == 'ls':
            None
    else:
        part1 = line.split(' ')[0]
        part2 = line.split(' ')[1]

        if part1 == 'dir':
            dirs.append([cwd, part2, 0])
        else:
            files.append((cwd, part2, int(part1)))
print('\n\n\n\ndirectories ...')
for dir in dirs:
    print(dir)

print('\n\n\n\nfiles ...')
for file in files:
    print(file)

for dir in dirs:
    total_size = 0
    path = dir[0] + dir[1] + '/'
    for file in files:
        if file[0].startswith(path):
            total_size += file[2]        
    dir[2] = total_size

print('\n\n\n\nsizes ...')
for dir in dirs:
    print(dir)

result = 0
for dir in dirs:
    if dir[2] < 100000:
        result += dir[2]

print(result)