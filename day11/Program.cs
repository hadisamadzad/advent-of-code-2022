








// var lines = File.ReadAllLines("demo-input.txt");
// Console.WriteLine("");

// var monkey_count = Convert.ToInt32(lines.Length / 7) + 1;
// var monks = new List<Monkey>();

// // read input & setup
// foreach (var ) monkey_index in range(monkey_count):
//     monkey = Monkey()


// //     line_index = monkey_index * 7
// //     monkey.items = lines[line_index + 1][18:].split(', ')
// //     for i in range(len(monkey.items)):
// //         monkey.items[i] = float(monkey.items[i]) / 1000000
// //     monkey.op_type = lines[line_index + 2][23:24]
// //     _temp_ = (lines[line_index + 2][25:]).strip()
// //     monkey.op_value = -1 if _temp_ == 'old' else int(_temp_)
// //     monkey.test_div_value = int((lines[line_index + 3][21:]).strip())
// //     monkey.test_true_monkey = int((lines[line_index + 4][29:]).strip())
// //     monkey.test_false_monkey = int((lines[line_index + 5][30:]).strip())

// //     monks.append(monkey)

// // turn_count = 10000
// // for turn in range(turn_count):
// //     if turn % 50 == 0:
// //         print('Turn: ', turn)
// //     for i in range(monkey_count):
// //         for j in range(len(monks[i].items)):

// //             stuff_worry = monks[i].items.pop(0)
// //             op = monks[i].op_type
// //             op_value = monks[i].op_value
// //             test_div_value = monks[i].test_div_value
// //             true_next_monk = monks[i].test_true_monkey
// //             false_next_monkey = monks[i].test_false_monkey

// //             monks[i].inspections += 1
// //             stuff_worry = update_worry(stuff_worry, op, op_value)

// //             next_monk = false_next_monkey
// //             if stuff_worry % test_div_value == 0:
// //                 next_monk = true_next_monk
// //             monks[next_monk].items.append(stuff_worry)

// // max1, max2 = 0, 0
// // for i in range(monkey_count):
// //     inspections = monks[i].inspections
// //     if inspections > max1:
// //         max2, max1 = max1, inspections
// //     elif inspections > max2:
// //         max2 = inspections

// // print(max1 * max2)