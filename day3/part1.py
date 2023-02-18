f = open("input.txt", "r")
# f = open("demo-input.txt", "r")
rucksacks = f.readlines()

total_priority = 0

for rucksack in rucksacks:
    for index_item, item in enumerate(rucksack):
        pair_found = False
        for pair_index in range(len(rucksack) // 2, len(rucksack) - 1):
            if item == rucksack[pair_index]:
                pair = rucksack[pair_index]
                if pair.isupper():
                    priority = ord(pair) - 38
                else:
                    priority = ord(pair) - 96
                total_priority += priority 
                pair_found = True
                
                break
        if pair_found:
            break

print(total_priority)