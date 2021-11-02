def func():
    print("func() in one.py")


print('Top level one.py')


if __name__ == '__main__':
    print('one.py is being run directory!')
else:
    print('one.py has nee imported.')
