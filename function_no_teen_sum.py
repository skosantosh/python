# function_no_teen_sum

def no_teen_sum(a, b, c):

    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    if n in {13, 14, 17, 18, 19}:  # if this number in def no_teen_sun sum as 0
        return 0
    return n


print(no_teen_sum(1, 13, 3))
