s = 'django'
print(s[0])
print(s[-1])
print(s[:4])
print(s[1:4])
print(s[4:])

print(f"Reverse {s[::-1]}")

ls = []
c = 0
for x in s:
    ls.insert(int(c), x)
    c = c + 1
print(ls)
ls.reverse()
print(ls)
co = ""
for x in ls:
    co = co + x
print(f"next reverse {co}")

lst = [3, 7, [1, 4, 'hello']]
lst[2][2] = 'goodbye'
print(lst)

""" lst = [3, 7, [1, 4, 'hello']]
for r in lst:
    if 'hello' in r:
        x[-1] = 'goodbye'
print(lst)
 """

mylist = set([1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3])
print(mylist)

d1 = {'simple_key': 'hello'}
d2 = {'k1': {'k2': 'hello'}}
d3 = {'k1': [{'nest_key': ['this is deep', ['ram']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
tt = d3['k1'][0]['nest_key'][1][0]
print(tt)

age = 4
name = 'Sammy'
print("Hello my dag's name is {a} and he is {b} yrars old."
      .format(a=name, b=age))
