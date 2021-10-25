import random
# generated computer number


# Get guess
def get_guess():
    return list(input("What is your guess: "))


x = get_guess()
# print(type(x[0]))


# Generate code
def generat_code():
    digits = [str(num) for num in range(10)]

    # Shuffle the digits
    random.shuffle(digits)

    # Grab the first three
    return digits[:3]


# Generate Clues
def generate_clues(code, user_guess):
    if user_guess == code:
        return "CODE CRACKED!"

    clues = []

    for idn, num in enumerate(user_guess):
        if num == code[idn]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")

    if clues == []:
        return ["Nope"]
    else:
        return clues

# Game Logic


print("Welcome code Breaker!")

secret_code = generat_code()
clue_report = []

while clue_report != "CODE CRACKED!":

    guess = get_guess()
    clue_report = generate_clues(secret_code, guess)
    print("Here is the result of your guess: ")
    print(f"Computer Generate {secret_code}")
    for clue in clue_report:
        print(clue)

# Rum Game Logic
