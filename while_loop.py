import random
counter = 65
number_print = 0
while counter < 91:
    print(str(counter) + "=" + chr(counter))
    counter += 1
print("All Done")

print("Number that aren't evnely divisible by 5.")
san = 0
while san < 10:
    number = random.randint(1, 999)
    if int(number/5) == number/5:
        break
    number_print = number_print + number
    print(number)
    san += 1
print(f"Totla  {number_print}")
print("Loop is Done.")
