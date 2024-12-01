listLeft = []
listRight = []
distance = 0
similarityScore = 0

with open("input.txt", "r") as file:
    for line in file:
        elements = line.split("   ")
        listLeft.append(int(elements[0]))
        listRight.append(int(elements[1].strip("\n")))

listLeft.sort()
listRight.sort()

for eleLeft, eleRight in zip(listLeft, listRight):
    print(abs(eleLeft - eleRight))
    distance += abs(eleLeft - eleRight)

print(f"Distance: {distance}")


for eleLeft in listLeft:
    similarityScore += eleLeft * listRight.count(eleLeft)
    
print(f"Similarity: {similarityScore}")
