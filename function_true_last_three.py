def end_other(a, b):
    a = a.lower()
    b = b.lower()

    return b.endswith(a) or a.endswith(b)


print(end_other('Santosh', 'Dahal'))

# or

"""
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a[-(len(b)):] == b or a == b[-len(a)]



print(end_other('Santosh', 'Dahal'))
"""
