f = open("input.txt", "r")
# f = open("demo-input.txt", "r")
input = f.read()
tmp1 = input.split('\n\n')
elves_count = len(tmp1)
elves_calories = []

# Part 1
for elf in range(elves_count):
    calories = 0
    for index in range(len(tmp1[elf].split('\n'))):
        calories += int(tmp1[elf].split('\n')[index])
    
    elves_calories.append(calories)

max_elf_calories = max(elves_calories)
print(max_elf_calories)

# Part 2
total_backup_calories = 0
total_backup_calories += max_elf_calories
elves_calories.pop(elves_calories.index(max_elf_calories))

max_elf_calories = max(elves_calories)
total_backup_calories += max_elf_calories
elves_calories.pop(elves_calories.index(max_elf_calories))

max_elf_calories = max(elves_calories)
total_backup_calories += max_elf_calories
elves_calories.pop(elves_calories.index(max_elf_calories))

print(total_backup_calories)