import random

siege = 0
verloren = 0

while True:


    print ("""
====================================
        ZAHLENRATESPIEL
====================================

Wähle eine Schwierigkeit:

[1] Einfach  (1–10,  3 Versuche)
[2] Mittel   (1–20,  4 Versuche)
[3] Schwer   (1–50,  5 Versuche)

====================================   """)




   

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
    gewonen = False


    print (f"""
           
------------------------------------
Zahlenratespiel Level{level}

Errate die Zahl zwischen 1 und {max}
Hey! Achte darauf, du hast nur {versuche_limit} Versuche

Viel Spaß...
------------------------------------""")

    


    while versuche < versuche_limit:
        try:
            eingabe = int(input("Gib deine Schätzung ein: "))
        except:
            print("Bitte gib eine Zahl ein!")
            continue

        versuche += 1

        if eingabe == zahl:
            print("Richtig! Du hast gewonnen.")
            siege += 1
            gewonen = True
            break
        elif eingabe < zahl:
            print("Zu klein, versuch nochmal")
        else:
            print("Zu gross, versuch nochmal")

    if not gewonen:

        print("Leider, du hast verloren. Die Zahl war:", zahl)
        verloren += 1


    statistik = input("Willst du deine Ergebnisse sehen? (ja/nein): ").strip().lower()
    if statistik == "ja":
        spiele = siege + verloren
        if spiele > 0:
            quote = (siege / spiele) * 100
        else:
            quote = 0

        

        print (f"""
    ========== Deine Ergebnisse ==========
    Gewonnen   : {siege}
    Verloren   : {verloren}
    Gewinnquote: {quote:.2f}%
    =======================================""")
           



    nochmal = input("Willst du nochmal spielen? (ja/nein) ").strip().lower()

    if nochmal != "ja":
        print("Ok, wie du willst..Bye")
        break


    
    




