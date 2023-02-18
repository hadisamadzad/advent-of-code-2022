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
    used_space = 0
    path = dir[0] + dir[1] + '/'
    for file in files:
        if file[0].startswith(path):
            used_space += file[2]        
    dir[2] = used_space

print('\n\n\n\nsizes ...')
for dir in dirs:
    print(dir)

used_space = 0
for dir in dirs:
    if dir[0] == '/':
        used_space += dir[2]

for file in files:
    if file[0] == '/':
        used_space += file[2]

free_space = 70_000_000 - used_space
needed_space = 30_000_000 - free_space

print('used space: ', used_space)
print('free space: ', free_space)
print('needed space: ', needed_space)

deleting_dir_size = 30_000_000
for dir in dirs:
    if dir[2] >= needed_space and dir[2] < deleting_dir_size:
        deleting_dir_size = dir[2]

print('deleting dir size', deleting_dir_size)