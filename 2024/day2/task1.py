def is_safe(myList):
    asc = myList[0] < myList[1]
    desc = myList[0] > myList[1]
    for a, b in zip(myList, myList[1:]):
        if asc and a > b:
            return False
        if desc and a < b:
            return False
        if abs(a - b) < 1 or abs(a - b) > 3:
            return False
    return True
        
counter = 0
with open("input.txt","r") as file:
    for line in file:
        if is_safe(list(map(int, line.split()))):
            counter += 1

print(f"Safe lines: {counter}")