try:
    f = open('simple.txt', 'r')
    # f = open('simple.txt', 'w')
    f.write("Test write to simple text!")
# except: we can use this instade
except IOError:
    print("ERROR: Could not find file or read data!\n")
else:
    print("Success!")
    f.close()

try:
    f = open('simple.txt', 'r')
    # f = open('simple.txt', 'w')
    f.write("Test write to simple text!")
# except: we can use this instade
except IOError:
    print("ERROR: Could not find file or read data!")
finally:
    print('I always work no matter what!')
