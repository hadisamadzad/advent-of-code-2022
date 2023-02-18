f = open("input.txt", "r")
# f = open("demo-input.txt", "r")

ops = f.readlines()

for index, row in enumerate(ops):
    ops[index] = row.replace('\n', '')

def do_cycle(cycle, register, crt):
    x = cycle % 40
    y = cycle // 40

    drawing_char = ' '
    if abs(register - x) <= 1:
        drawing_char = '#'

    cycle += 1
    crt[x, y] = drawing_char

    return (cycle, crt)

x_dim, y_dim = 40, 6
crt = { (i,j):0 for i in range(x_dim) for j in range(y_dim) }

cycle = 0
register = 1

for op in ops:
    cycle_count = 0
    has_register_update = False

    if op.startswith('addx'):
        cycle_count = 2
        has_register_update = True
    elif op.startswith('noop'):
        cycle_count = 1

    for i in range(cycle_count):
        (cycle, crt) = do_cycle(cycle, register, crt)
    if has_register_update:
        register += int(op.split(' ')[1])

for j in range(y_dim):
    for i in range(x_dim):
        print(crt[i, j], end='  ')
    print('\n')