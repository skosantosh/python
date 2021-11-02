import s11_one
print('Top level two.py')
s11_one.func()

if __name__ == '__nain__':
    print('Two.py being run directly.')
else:
    print('Two os being imported.')