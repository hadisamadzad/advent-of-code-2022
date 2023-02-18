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

rules = {
    'AA': 3,
    'AB': 0,
    'AC': 6,
    'BA': 6,
    'BB': 3,
    'BC': 0,
    'CA': 0,
    'CB': 6,
    'CC': 3,
}

f = open("input.txt", "r")
# f = open("demo-input.txt", "r")
turns = f.readlines()

turn_count = len(turns)

point_shape = 0
point_win = 0

for turn in turns:
    turn = turn.replace('\n', '')
    mine = turn.split(' ')[1]
    opponent = turn.split(' ')[0]
    
    mine = shape_equiv[mine]
    point_shape += shape_points[mine]
    point_win += rules[mine+opponent]

print(point_shape + point_win)