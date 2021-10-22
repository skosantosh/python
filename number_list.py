my_income = 1000000
tax_rate = 0.1
my_tax = my_income * tax_rate
print(f"My Tax  {my_tax}")

mystring = 'Hello John How Are You.'
print(mystring[5])
print(mystring[2:])
print(mystring[2:5])
print(mystring[2::])
print(mystring[::2])

x = mystring.split()
print(x)

x = "ITem one: {} Item two: {} Item Third: {} ".format("dog", "cat", "cow")
print(x)
x = "ITem one: {x} Item two: {y} Item Third: {z} ".format(x="dog", y="cat",
                                                          z="cow")
print(x)

# List
mylist = ['ram', 'hari', 'sam', 'gita', 'rita']
mylist.reverse()
print(mylist)
mylist.sort()
print(f"Sort {mylist}")

# More list

mylist = ['ram', 'hari', 'sam', 'gita', 'rita', ['Kumar', 'Dahal', 'K.C']]
print(mylist)

mylist = [1, 2, 3, ['x', 'y', 'z'], ['a,', 'b', 'c']]
print(mylist)

print(mylist[4][1])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = []
# list Comprehention
first_col = [row[0] for row in matrix]
second_col = [row[1] for row in matrix]
third_col = [row[2] for row in matrix]
print(first_col)
print(second_col)
print(third_col)
matrix2.insert(0, first_col)
matrix2.insert(1, second_col)
matrix2.insert(2, third_col)
print(matrix2)

first_col = [row[0] for row in matrix2]
second_col = [row[0] for row in matrix2]
third_col = [row[0] for row in matrix2]

print(first_col)
print(second_col)
print(third_col)
matrix2 = []
matrix2.insert(0, first_col)
matrix2.insert(1, second_col)
matrix2.insert(2, third_col)
print(matrix2)
