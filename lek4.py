#slumpgenerator
#tärning 1-6

import random
redo = True
while redo == True:
    try:
        print("Tjena till tärninggeneratorn")
        meny = input("Vill du (S)arta eller (A)vsluta ")
        if meny == "s":
            sides = int(input("hur mång sidor vill du ha på tärningen? "))

            randomNumber = random.randint(1,sides)

            print("/roll/")
            print("tärningen rullade " + str(randomNumber))
        elif meny == "a":
            redo = False
            print("Hejdå")

    except:
        print("Det där funkade inte")