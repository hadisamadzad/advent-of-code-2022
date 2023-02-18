f = open("input.txt", "r")
# f = open("demo-input.txt", "r")

moves = f.readlines()
dim = 1200
dim2 = dim // 2

for index, row in enumerate(moves):
    moves[index] = row.replace('\n', '')


def need_tail_move(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail

    if max(abs(head_x - tail_x), abs(head_y - tail_y)) <= 1:
        return False
    return True

def print_bridge(mesh):
    for i in reversed(range(dim)):
        for j in range(dim):
            print(mesh[i, j], end='   ')
        print('\n')


H = { (i,j):0 for i in range(dim) for j in range(dim) }
# H = [[0] * dim] * dim
H[dim2,dim2] = 2
H_current_x = dim2
H_current_y = dim2
H_prev_x = dim2
H_prev_y = dim2

T = { (i,j):0 for i in range(dim) for j in range(dim) }
# T = [[0] * dim] * dim
T[dim2,dim2] = 2
T_current_x = dim2
T_current_y = dim2

# Main
for move in moves:
    # print(move)
    
    dir = move.split(' ')[0]
    steps = int(move.split(' ')[1])

    # Move
    for step in range(steps): 
        # Save prev location
        H_prev_x, H_prev_y = H_current_x, H_current_y
        
        H[H_current_x, H_current_y] = 1
        if dir == 'U':
            H_current_x += 1
        elif dir == 'D':
            H_current_x -= 1
        elif dir == 'R':
            H_current_y += 1
        elif dir == 'L':
            H_current_y -= 1
        H[H_current_x, H_current_y] = 2

        is_needed_tail_move = need_tail_move((H_current_x, H_current_y), (T_current_x, T_current_y))
        # print(is_needed_tail_move)
        if is_needed_tail_move:
            T[T_current_x, T_current_y] = 1
            T_current_x, T_current_y = H_prev_x, H_prev_y
            T[T_current_x, T_current_y] = 2

    # print("Head Mesh")
    # print_bridge(H)
    # print("Tail Mesh")
    # print_bridge(T)

    # input("Next Move ?")


    
total_tail_locs = 0
for i in range(dim):
    for j in range(dim):
        if T[i, j] > 0:
            total_tail_locs += 1

print(total_tail_locs)