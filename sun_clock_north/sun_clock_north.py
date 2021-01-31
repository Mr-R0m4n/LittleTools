# Find North with position of sun and time


# Methods
# Get North
def get_north(hour, season):
    angle = int((hour * (360/12) + season))
    north = int((angle / 2 + 180)/30)
    return north


# Main program
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
        print("When you point your hour hand to the sun at " + str(time) + " o´clock, "
        "north will be around at: " + str(get_north(time, 30)) + " o´clock")
    elif menu == "w":
        print()
        time_input = input("Please enter the time (hh:mm)")
        time = int(time_input[:2])
        print("When you point your hour hand to the sun at " + str(time) + " o´clock, "
        "north will be around at: " + str(get_north(time, 0)) + " o´clock")
    elif menu == "e":
        print("Bye until later!")
        exit()
    else:
        loop = True
        print()
        print("Invalid Entry")
