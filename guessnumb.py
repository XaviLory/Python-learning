import random
guess = int(input("Input ur number here!   "))
secret_number = random.randint(1,100)


while guess != secret_number:

    if guess > secret_number:
        print("too big! try lower!")


    elif guess < secret_number:
        print("too low! try higher!")

    guess = int(input("try again!   "))

print("You get it right!!")


