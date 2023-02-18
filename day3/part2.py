f = open("input.txt", "r")
# f = open("demo-input.txt", "r")
rucksacks = f.readlines()
groups_count = len(rucksacks) // 3
group_length = 3
total_priority = 0

group_badges = []

for group_index in range(groups_count):
    smallest_rucksack_index = group_index * 3
    for item1 in rucksacks[smallest_rucksack_index]:
        found_in_2 = False
        found_in_3 = False
        
        for item2 in rucksacks[smallest_rucksack_index + 1]:
            if item1 == item2:
                found_in_2 = True
                break
        
        if found_in_2:
            for item3 in rucksacks[smallest_rucksack_index + 2]:
                if item1 == item3:
                    found_in_3 = True
                    break
        
        if found_in_2 and found_in_3:
            group_badges.append(item1)
            break

for badge in group_badges:
    if badge.isupper():
        priority = ord(badge) - 38
    else:
        priority = ord(badge) - 96
    
    total_priority += priority

print(total_priority)