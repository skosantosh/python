"""if condition: do this no matter what """

sun = "down"
if sun == "down":
    print("Good night")
print("I am here")

if sun == "up":
    print("Good Night")
print("I am Here.")

total = 100
sale_tax_rate = .065
taxable = True
sale_tax = total * sale_tax_rate
net_total = total + sale_tax
if taxable:
    output = f"""
    SubTotal : ${total:>9.2f}
    Sale Tax : ${sale_tax:>9.2f}
    Net Total: ${net_total:>9.2f}
    """
print(output)

# Heading Multiple else statements with elif
light_color = "green"
if light_color == "green":
    print("Go")
elif light_color == "red":
    print("Stop")
print("This code executes no matter what")

light_color = "red"
if light_color == "green":
    print("Go")
elif light_color == "red":
    print("Stop")
print("This code executes no matter what")

light_color = "yellow"
if light_color == "green":
    print("Go")
elif light_color == "red":
    print("Stop")
else:
    print("Process with coutation")
print("This code executes no matter what")

age = 80
if age < 21:
    eat = "milk"
elif age >= 21 and age < 80:
    eat = "beer"
else:
    eat = "prune juice"
print("Have a " + eat)

available_toppings = ['musroom', 'olives', 'pineapple', 'extra cheese',
                      'green peppers', 'pepperoni']
request_toppings = ['musroom', 'french fries', 'extra cheese']

for reqest_topping in request_toppings:
    if reqest_topping in available_toppings:
        print(f"Adding {reqest_topping}.")
    else:
        print(f"Sorry, we don't have {reqest_topping}.")
print("Finished making pizza.")
