import random
# generated computer number


def generat_code():
    digits = [str(num) for num in range(10)]
    # shuffle the digits
    random.shuffle(digits)

    # grab the first three
    return digits[:3]

# Generate Clue


def generate_clues(code, user_guess):
    if user_guess == code:
        return "CODE CRACKED!"

    clues = []

    for count, value in enumerate(user_guess):
        if value == code[count]:
            clues.append("match")
        elif value in code:
            clues.append("Close")

    if clues == []:
        return ["Nope"]
    else:
        return clues


# get guess

def get_guess():
    return input("What is your guess: ")


x = get_guess()
print(type(x[0]))

# Game logic
print("Welcome code Breaker!")
secret_code = generat_code()

clue_report = []

while clue_report != "CODE CRACKED!":

    guess = get_guess()
    clue_report = generate_clues(guess, secret_code)
    print("Here is the result of your guess: ")
    for clue in clue_report:
        print(clue)
