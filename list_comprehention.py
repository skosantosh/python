# list Comprehention
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first_col = [row[0] for row in matrix]
second_col = [row[1] for row in matrix]
third_col = [row[2] for row in matrix]
print(first_col)
print(second_col)
print(third_col)