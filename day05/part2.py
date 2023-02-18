f = open("input.txt", "r")
# f = open("demo-input.txt", "r")

lines = f.readlines()

for index, row in enumerate(lines):
    lines[index] = row.replace('\n', '')

stacks_count = len(lines[0]) // 4 + 1
stacks = []
for i in range(stacks_count):
    stacks.append([])

init_layer_count = 0

# Find number of crate layers
for layer, line in enumerate(lines):
    if line[1] == '1':
        init_layer_count = layer
        break

# Read Stacks
for line in lines[0 : init_layer_count]:
    for i in range(stacks_count):
        crate_lable_index = i * 4 + 1
        crate_lable = line[crate_lable_index]
        if 65 <= ord(crate_lable) and ord(crate_lable) <= 96:
            stacks[i].insert(0, crate_lable)

# Move crates
for line in lines[init_layer_count + 2 : len(lines)]:    
    move_items = int(line.split(' ')[1])
    from_stack_index = int(line.split(' ')[3]) - 1
    to_stack_index = int(line.split(' ')[5]) - 1
    
    moving_crates = stacks[from_stack_index][-move_items:]
    
    for crate in moving_crates:
        stacks[to_stack_index].append(crate)
        stacks[from_stack_index].pop()

top_lables = ''
for stack in stacks:
    top_lables = top_lables + stack.pop()

print(top_lables)