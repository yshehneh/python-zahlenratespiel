import random

while True:


    print ("Willkommen beim Zahlenratespiel")
    print("Wähle eine Schwierigkeit:")
    print("1 = Einfach (1-10, 3 Versuche)")
    print("2 = Mittel (1-20, 4 Versuche)")
    print("3 = Schwer (1-50, 5 Versuche)")

    auswahl = input("Deine Wahl (1, 2 oder 3): ")


    if auswahl == "1":
        max = 10
        versuche_limit = 3
        level = "(einfach)"
    elif auswahl == "2":
        max = 20
        versuche_limit = 4
        level = "(mittel)"
    elif auswahl == "3":
        max = 50
        versuche_limit = 5
        level = "(schwer)"
    else:
        print("Falsche Eingabe, ich nehme einfach mal Mittel.")
        max = 20
        versuche_limit = 4
        level = "(mittel)"


    zahl = random.randint(1, max)
    versuche = 0

    print(f"Zahlenratespiel Level{level}")

    print(f"Errate die Zahl zwischen 1 und {max}")
    print(f"Hey! Achte darauf, du hast nur {versuche_limit} Versuche.")


    while versuche < versuche_limit:
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
