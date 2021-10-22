# function_double_char
def doublechar(mystring):
    result = ''
    c = 0
    for char in mystring:
        result += char*2
    return result


print(doublechar('santosh'))
