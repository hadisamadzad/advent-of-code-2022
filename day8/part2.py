f = open("input.txt", "r")
# f = open("demo-input.txt", "r")

trees = f.readlines()

for index, row in enumerate(trees):
    trees[index] = row.replace('\n', '')

m = len(trees)
n = len(trees[0])

max_scene_score = 0

for row in range(1, m - 1):
    for col in range(1, n - 1):
        
        tree = int(trees[row][col])
        scene_score = 1

        top_score = 0
        for i in reversed(range(0, row)):
            top_score += 1
            if int(trees[i][col]) >= tree:
                break

        bottom_score = 0
        for i in range(row + 1, m):
            bottom_score += 1
            if int(trees[i][col]) >= tree:
                break

        left_score = 0
        for i in reversed(range(0, col)):
            left_score += 1
            if int(trees[row][i]) >= tree:
                break

        right_score = 0
        for i in range(col + 1, n):
            right_score += 1
            if int(trees[row][i]) >= tree:
                break

        scene_score = top_score * bottom_score * right_score * left_score
        print(f"tree {row} x {col} = {tree} => scene: {scene_score}")
        if scene_score > max_scene_score:
            max_scene_score = scene_score
print(max_scene_score)