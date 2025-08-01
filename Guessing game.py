from random import randint

for x in range(1,91):
    guessnumber = int(input("Please Enter your guess number between 1 to 5: "))
    randomnumber = randint(1,5)
    if guessnumber == randomnumber:
        print("YOU HAVE WON BOSS 🌹🌹")
    else:
        print("APNI HERE GESEN ABR TRY KOREN😁🤣")
        print("Random number was : ", randomnumber)
