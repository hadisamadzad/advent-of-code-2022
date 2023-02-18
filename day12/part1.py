f = open("input.txt", "r")
# f = open("demo-input.txt", "r")

ops = f.readlines()

for index, row in enumerate(ops):
    ops[index] = row.replace('\n', '')

def do_cycle(cycle, register, signal_strenght):
    cycle += 1
    
    if cycle == 20 or (cycle - 20) % 40 == 0:
        signal_strenght += cycle * register

    return (cycle, signal_strenght)

cycle = 0
register = 1
signal_strenght = 0

for op in ops:
    cycle_count = 0
    has_update = False
    
    if op.startswith('addx'):
        cycle_count = 2
        has_update = True
    elif op.startswith('noop'):
        cycle_count = 1
    
    for i in range(cycle_count):
            (cycle, signal_strenght) = do_cycle(cycle, register, signal_strenght)
    if has_update:
        register += int(op.split(' ')[1])

print(signal_strenght)