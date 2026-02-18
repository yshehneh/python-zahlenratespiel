import random

while True:

    zahl = random.randint(1, 10)
    versuche = 0

    print("Zahlenratespiel")
    print("Errate eine Zahl zwischen 1 und 10")
    print("Hey! Achte darauf, du hast nur 3 Versuche.")

    while versuche < 3:
        try:
            eingabe = int(input("Deine Zahl: "))
        except:
            print("Bitte gib eine Zahl ein!")
            continue

        versuche += 1

        if eingabe == zahl:
            print("Richtig! Du hast gewonnen.")
            break
        elif eingabe < zahl:
            print("Zu klein, versuch nochmal")
        else:
            print("Zu groß, versuch nochmal")

    else:
        print("Leider, du hast verloren. Die Zahl war:", zahl)


    nochmal = input("Willst du nochmal spielen? (ja/nein) ").strip().lower()

    if nochmal != "ja":
        print("Ok, wie du willst..")
        break
