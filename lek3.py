print("Välkommen till räknaratorn")

operator = input("välj räknesätt (a)ddera, (s)ubtraktion, (m)ultiplikation eller (d)ivision:")

if operator == "a":
    tal1 = int(input("skriv tal: "))
    tal2 = int(input("skriv ett till tal: "))
    summa = tal1 + tal2

    print("Abra kadabra")
    print("Ditt tal är " + str(summa))



elif operator == "s":
    tal3 = int(input("skriv tal: "))
    tal4 = int(input("skriv ett till tal: "))
    differens = tal3 - tal4

    print("aaaahhhhh")
    print("Din differens är " + str(differens))


elif operator == "m":
    tal5 = int(input("skriv tal: "))
    tal6 = int(input("skriv ett till tal: "))
    produkt = tal5 * tal6

    print("wow")
    print("produkten av denna multiplikation är " + str(produkt))


elif operator == "d":
    tal7 = int(input("skriv tal: "))
    tal8 = int(input("skriv ett till tal: "))
    if tal8 == 0:
        print("sluta")
    elif operator > 0:
        tal7 = int(input("skriv tal: "))
        tal8 = int(input("skriv ett till tal: "))
        kvot = tal7 / tal8
        print("varför gör du det är mot mig")
        print("min kvotering om denna kvot är: " + str(kvot))

else: 
    
    print("WRONG")




