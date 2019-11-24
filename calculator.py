position = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
            "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def is_not_compatible(x, b):
    for i in x:
        if i not in position[:b]:
            return True
    return False


def to_array_of_numbers(x):
    array = []
    for i in x:
        array.append(position.index(i))
    return array


def to_ten(x, b):
    count = total = 0
    x = to_array_of_numbers(x[::-1])
    for i in x:
        total += int(i) * (int(b) ** count)
        count += 1
    return total


def to_desired_base(decimal, b):
    array = []
    while decimal > 0:
        array.append(position[decimal % b])
        decimal = decimal // b
    final = ''.join(array[::-1])
    return final


number_to_convert = input()
original_base = input()
final_base = int(input())

if is_not_compatible(number_to_convert, int(original_base)):
    print("Wrong base, number or number not compatible with base")
else:
    print(to_desired_base(to_ten(number_to_convert, original_base), final_base))
