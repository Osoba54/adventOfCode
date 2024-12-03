def is_safe(my_list):
    def check(lst):
        asc = lst[0] < lst[1]
        desc = lst[0] > lst[1]
        for ele, nextEle in zip(lst, lst[1:]):
            if asc and ele > nextEle:
                return False
            if desc and ele < nextEle:
                return False
            if abs(ele - nextEle) < 1 or abs(ele - nextEle) > 3:
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
