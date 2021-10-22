for item in range(10):
    print(item)

x = [1, 2, 3, 4]

out = []
for num in x:
    out.append(num**2)

print(out)

# or

out = [num**2 for num in x]
print(out)
