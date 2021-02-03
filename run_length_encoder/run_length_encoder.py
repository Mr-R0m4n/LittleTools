message = input()


def lauflaengencodierung(data):
    liste = []
    ergebnis = ""
    counter = 1
    i = 1

    for char in data:
        liste.append(char)

    while i != len(liste):
        if liste[0] == liste[i]:
            counter = counter + 1
        else:
            ergebnis = ergebnis + str(counter) + liste[0]
            counter = 1
        liste[0] = liste[i]
        i = i + 1
    letze_ziffer = str(counter) + liste[0]

    print(ergebnis + letze_ziffer)


lauflaengencodierung(message)
