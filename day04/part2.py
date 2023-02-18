f = open("input.txt", "r")
# f = open("demo-input.txt", "r")

pairs = f.readlines()

for index, row in enumerate(pairs):
    pairs[index] = row.replace('\n', '')

total_overlaps = 0

for pair in pairs:
    work1 = pair.split(',')[0].split('-')
    work2 = pair.split(',')[1].split('-')

    overlap = False

    if int(work1[0]) <= int(work2[0]) and int(work2[0]) <= int(work1[1]):
        overlap = True
    elif int(work1[0]) <= int(work2[1]) and int(work2[1]) <= int(work1[1]):
        overlap = True
    elif int(work2[0]) <= int(work1[0]) and int(work1[0]) <= int(work2[1]):
        overlap = True
    elif int(work2[0]) <= int(work1[1]) and int(work1[1]) <= int(work2[1]):
        overlap = True
    
    if overlap:
        total_overlaps += 1

print(total_overlaps)