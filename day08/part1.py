f = open("input.txt", "r")
# f = open("demo-input.txt", "r")

trees = f.readlines()

for index, row in enumerate(trees):
    trees[index] = row.replace('\n', '')

m = len(trees)
n = len(trees[0])
total_visible = 2 * (m - 2) + 2 * (n - 2) + 4

for row in range(1, m - 1):
    for col in range(1, n - 1):

        tree = int(trees[row][col])

        tops = []
        tops.append(0)
        for i in range(0, row):
            tops.append(int(trees[i][col]))
        if tree > max(tops):
            total_visible += 1
            continue

        bottoms = []
        bottoms.append(0)
        for i in range(row + 1, m):
            bottoms.append(int(trees[i][col]))
        if tree > max(bottoms):
            total_visible += 1
            continue

        lefts = []
        lefts.append(0)
        for i in range(0, col):
            lefts.append(int(trees[row][i]))
        if tree > max(lefts):
            total_visible += 1
            continue

        rights = []
        rights.append(0)
        for i in range(col + 1, n):
            rights.append(int(trees[row][i]))
        if tree > max(rights):
            total_visible += 1
            continue

print(total_visible)