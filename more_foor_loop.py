for x in range(7):
    print(x)
print("All done")

for x in range(1, 5):
    print(x)
print("done")

for x in "Santosh":
    print(x)
print("done")

for x in ["Santosh", "Sarita", "Prashna", "Prexya"]:
    print(x)
print("Done")

name = ["Santosh", "Sarita", "Prashna", "Prexya", "Neesh", "Rima"]
for x in name:
    print(x)
print("Done")

answers = ["A", "B", "C", "D"]
for answer in answers:
    if answer == "":
        print("incomplete")
        break
    print(answer)
print("Loop Done")

answers = ["A", "B", "", "D"]
for answer in answers:
    if answer == "":
        print("incomplete")
        break
    print(answer)
print("Loop Done")

answers = ["A", "B", "", "D"]
for answer in answers:
    if answer == "":
        print("incomplete")
        continue
    print(answer)
print("Loop Done")
# nested loop
for outer in ["First", "Second", "Third"]:
    print(outer)
    for inner in range(3):
        print(inner+1)

print("All Done Loop")
