# Vigenera-Schlüssel
def vigenere_schluessel(schluessel):
    print("Schlüssel: " + schluessel)
    print("Verschiebewerte von Schlüssel: ", end="")
    verschiebung = []
    for zeichen in schluessel:
        if zeichen.isupper():
            verschiebung.append((ord(zeichen)) - 65)
        else:
            verschiebung.append((ord(zeichen)) - 97)
    for zeichen in verschiebung:
        print(zeichen, end=" ")
    print("\n")
    return verschiebung


# Vigenere-Verschlüsselung
def vigenere(verschiebung, kette):
    print("Zeichenkette: " + kette)
    print("Vigenere-Verschlüsselung: ", end="")
    verschluesselt = []
    loop = 0
    index = 1
    # Zeichen um Wert verschieben
    while loop < len(kette) - 1:
        for zeichen in kette:
            if zeichen.isupper():
                verschluesselt.append(chr((ord(zeichen) + int(verschiebung[index - 1]) - 65) % 26 + 65))
            else:
                verschluesselt.append(chr((ord(zeichen) + int(verschiebung[index - 1]) - 97) % 26 + 97))
            loop += 1
            if index == len(verschiebung):
                index = 1
            else:
                index += 1
        for zeichen in verschluesselt:
            print(zeichen, end="")
    print("\n")
    return verschluesselt


# Vigenere knacken
def vigenere_knacken(verschiebung, kette):
    print("Vigenere-Verschlüsselung decodiert: ", end="")
    decodiert = []
    loop = 0
    index = 1
    # Zeichen um Wert verschieben
    while loop < len(kette):
        for zeichen in kette:
            if zeichen.isupper():
                decodiert.append(chr((ord(zeichen) - int(verschiebung[index - 1]) - 65) % 26 + 65))
            else:
                decodiert.append(chr((ord(zeichen) - int(verschiebung[index - 1]) - 97) % 26 + 97))
            loop += 1
            if index == len(verschiebung):
                index = 1
            else:
                index += 1
        for zeichen in decodiert:
            print(zeichen, end="")
    print("\n")
    return decodiert


schluesselwort = input("Bitte geben Sie Ihr Schlüsselwort ein: ")
zeichenkette = input("Bitte geben Sie Ihre Zeichenkette ein: ")
print("\n")

verschiebewert = vigenere_schluessel(schluesselwort)

codiert = vigenere(verschiebewert, zeichenkette)

vigenere_knacken(verschiebewert, codiert)
