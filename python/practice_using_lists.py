data = ["B", 78, 69, "E", "S", 73, "P", 80, 83, 66, "I", "N"]
data_str = []
data_num = []

for item in data:
    if isinstance(item, str):
        data_str.append(item)
    else:
        data_num.append(item)

print("\nOriginal list: ", data)

print("\nCharacter list: ", data_str)
print("Number list: ", data_num)

print("\nCharacter list in descending order: ", sorted(data_str, reverse=True))
print("Character list in ascending order: ", sorted(data_str))

print("\nNumber list in descending order: ", sorted(data_num, reverse=True))
print("Number list in ascending order: ", sorted(data_str))
print()


def print_ln_by_ln(str_list, num_list):
    if len(str_list) > len(num_list):
        iterate = str_list
    else:
        iterate = num_list

    x = 0
    for row in iterate:
        print(str_list[x], num_list[x])
        x += 1


print_ln_by_ln(data_str, data_num)
