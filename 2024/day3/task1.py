from re import findall

def mul(a,b):
    return a*b

with open("input.txt","r") as file:
    corr_func = findall("mul\([0-9]{1,3},[0-9]{1,3}\)", file.read())

print(f"Result: {sum([eval(ele) for ele in corr_func])}")