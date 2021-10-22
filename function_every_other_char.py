def stringBits(str):
    return str[0::2]


print(stringBits('Heeololeo'))

# or


def stringBits(mystring):
    result = ""
    for i in range(len(mystring)):
        if i % 2 == 0:
            result = result + mystring[i]
    return result


print(stringBits('Hello'))
