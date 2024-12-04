from re import findall
accept = True
def mul(a,b):
    if accept:
        return a*b
    return 0

def do():
    global accept 
    accept = True
    return 0

def dont():
    global accept
    accept = False
    return 0
    
with open("input.txt","r") as file:
    corr_func = findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", file.read())

print(f"Result: {sum([eval(ele.replace("'","")) for ele in corr_func])}")
