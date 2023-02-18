f = open("input.txt", "r")
# f = open("demo-input.txt", "r")

lines = f.readlines()

for index, row in enumerate(lines):
    lines[index] = row.replace('\n', '')

class Monkey:
    items = []
    op_type = ''
    op_value = ''
    test_div_value = 0
    test_true_monkey = 0
    test_false_monkey = 0
    inspections = 0

def update_worry(worry, op, value):
    if value == 'old':
        worry *= worry
    elif op == '*':
        worry *= int(value)
    elif op == '+':
        worry += int(value)
    
    worry = worry // 3
    return worry

monkey_count = len(lines) // 7 + 1
monks = []

# read input & setup
for monkey_index in range(monkey_count):
    monkey = Monkey()
    
    line_index = monkey_index * 7
    monkey.items = lines[line_index + 1][18:].split(', ')
    for i in range(len(monkey.items)):
        monkey.items[i] = int(monkey.items[i])
    monkey.op_type = lines[line_index + 2][23:24]
    monkey.op_value = (lines[line_index + 2][25:]).strip()
    monkey.test_div_value = (lines[line_index + 3][21:]).strip()
    monkey.test_true_monkey = (lines[line_index + 4][29:]).strip()
    monkey.test_false_monkey = (lines[line_index + 5][30:]).strip()

    monks.append(monkey)


# for i in range(monkey_count):

#     print("\n\nmonkeys: ", i)
#     print(monks[i].items)
#     print(monks[i].op_type)
#     print(monks[i].op_value)
#     print(monks[i].test_div_value)
#     print(monks[i].test_true_monkey)
#     print(monks[i].test_false_monkey)
#     print('inspections: ', monks[i].inspections)

turn_count = 20
for turn in range(turn_count):
    for i in range(monkey_count):
        for j in range(len(monks[i].items)):

            stuff_worry = int(monks[i].items.pop(0))
            op = monks[i].op_type
            op_value = monks[i].op_value
            test_div_value = int(monks[i].test_div_value)
            true_next_monk = int(monks[i].test_true_monkey)
            false_next_monkey = int(monks[i].test_false_monkey)

            monks[i].inspections += 1
            stuff_worry = update_worry(stuff_worry, op, op_value)

            next_monk = false_next_monkey
            if int(stuff_worry) % test_div_value == 0:
                next_monk = true_next_monk
            monks[next_monk].items.append(stuff_worry)


# for i in range(monkey_count):
#     print("\n\nmonkeys: ", i)
#     # print(monks[i].items)
#     # print(monks[i].op_type)
#     # print(monks[i].op_value)
#     # print(monks[i].test_div_value)
#     # print(monks[i].test_true_monkey)
#     # print(monks[i].test_false_monkey)
#     print('inspections: ', monks[i].inspections)

max1 = 0
max2 = 0
for i in range(monkey_count):
    inspections = monks[i].inspections
    if inspections > max1:
        max2 = max1
        max1 = inspections
    elif inspections > max2:
        max2 = inspections

print(max1 * max2)