"""****************************************************
Cäsar-Verschlüsselung mit verschiebung um Zeichen Index
****************************************************"""


# Funktion zur Cäsar-Verschlüsselung
def caesar(kette):
    print("Cäsar-Verschlüsselung")
    # Index zur Erhöhung des Verschiebewertes
    index = 1
    # Jedes Zeichen um den jeweiligen Index verschieben
    for zeichen in kette:
        # Falls es ein Großbuchstabe ist
        if zeichen.isupper():
            print(chr((ord(zeichen) + len(kette[:index]) - 65) % 26 + 65), end=" ")
        else:
            print(chr((ord(zeichen) + len(kette[:index]) - 97) % 26 + 97), end=" ")
        # Erhöhung des Verschiebewertes
        index += 1
