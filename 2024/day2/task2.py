def is_safe(my_list):
    def check(list):
        asc = list[0] < list[1]
        desc = list[0] > list[1]
        for ele, next_ele in zip(list, list[1:]):
            if asc and ele > next_ele:
                return False
            if desc and ele < next_ele:
                return False
            if abs(ele - next_ele) < 1 or abs(ele - next_ele) > 3:
                return False
        return True

    if check(my_list):
        return True

    for i in range(len(my_list)):
        modified_list = my_list[:i] + my_list[i+1:]
        if check(modified_list):
            return True
    return False



counter = 0
with open("input.txt", "r") as file:
    for line in file:
        numbers = list(map(int, line.split()))
        if is_safe(numbers):
            counter += 1

print(f"Safe lines: {counter}")
