if 1 < 2:
    print("First column")
    if 2 < 10:
        print("Second column")

if 1 < 2:
    print("Hello")
elif 3 == 3:
    print('elif ran')
else:
    print("last")

# For Loop

""" nums = (1, 2, 3, 4, 5, 6)
for num in nums:
    print(num) """

# for loop for Dictionary

d = {'Sam': 1, "Frank": 2, "Dan": 3}

for k in d:
    print(k)
    print(d[k])

# list
mypairs = [(1, 2), (3, 4), (5, 6), (7, 8)]
for item in mypairs:
    print(item)
for (a, b) in mypairs:
    print(b)
    print(a)
print(mypairs[0])
tupleeg = (1, 2, 3, 4)
print(tupleeg)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# list Comprehention
first_col = [row[0] for row in matrix]
second_col = [row[1] for row in matrix]
third_col = [row[2] for row in matrix]
print(first_col)
print(second_col)
print(third_col)
