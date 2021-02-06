"""****************************************************
Cäsar-Verschlüsselung mit verschiebung um Zeichen Index
****************************************************"""


# Funktion zur Cäsar-Verschlüsselung
def caesar(zeichenkette):
    print("Cäsar-Verschlüsselung um Zeichen Index")
    # Eingabe des Verschiebewertes
    verschiebung = int(input("Bitte geben Sie den Verschiebewert ein: "))
    print("\n")
    print("Codiert: ", end="")
    # Index zur Erhöhung des Verschiebewertes
    index = 1
    # Jedes Zeichen um den Verschiebewert und jeweiligen Index in der Zeichenkette verschieben
    for zeichen in zeichenkette:
        # Falls es ein Großbuchstabe ist
        if zeichen.isupper():
            print(chr((ord(zeichen) + (verschiebung + len(zeichenkette[:index])) - 65) % 26 + 65), end=" ")
        else:
            print(chr((ord(zeichen) + (verschiebung + len(zeichenkette[:index])) - 97) % 26 + 97), end=" ")
        # Erhöhung des Verschiebewertes
        index += 1


eingabe = input("Bitte geben Sie die zu verschlüsselnde Zeichenkette ein: ")
print("\n")
caesar(eingabe)
