# Find North with position of sun and time


# Methods
# Get North
def get_north(hour, zero_point):
    angle = int(360 / 12 * hour)
    north = (360 - (zero_point * 30) - angle) / 2
    print(north)


# Main Program
# Menu

print("********************************************")
print("  Find North with position of sun and time")
print("********************************************")
print()
print("s = Summertime")
print("w = Wintertime")
print("e = Exit")
print()
loop = True
while loop:
    menu = input("Please choose: ").lower()

    if menu == "s":
        print()
        time_input = input("Please enter the time (hh:mm)")
        time = int(time_input[:2])
        get_north(time, 0)
    elif menu == "w":
        print()
        time_input = input("Please enter the time (hh:mm)")
        time = int(time_input[:2])
        get_north(time, 1)
    elif menu == "e":
        print("Bye until later!")
        exit()
    else:
        loop = True
        print()
        print("Invalid Entry")
