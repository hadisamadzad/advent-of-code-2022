shape_equiv = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

shape_points = {
    'A': 1,
    'B': 2,
    'C': 3,
}

result_points = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

rules = {
    'AX': 'C',
    'AY': 'A',
    'AZ': 'B',
    'BX': 'A',
    'BY': 'B',
    'BZ': 'C',
    'CX': 'B',
    'CY': 'C',
    'CZ': 'A',
}

f = open("input.txt", "r")
# f = open("demo-input.txt", "r")
turns = f.readlines()

turn_count = len(turns)

point_shape = 0
point_win = 0

for turn in turns:
    turn = turn.replace('\n', '')
    opponent = turn.split(' ')[0]
    result = turn.split(' ')[1]
    mine = rules[opponent+result]
    
    point_shape += shape_points[mine]
    point_win += result_points[result]

print(point_shape + point_win)