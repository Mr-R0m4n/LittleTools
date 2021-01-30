# Find North with position of sun and time


# Methods
# Get North
def get_north(hour, zero_point):
    print(hour)


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
        time_input = input("1Please enter the time (hh:mm)")
        time = int(time_input[:2])
        get_north(time, 0)
    elif menu == "w":
        print()
        time_input = input("2Please enter the time (hh:mm)")
        time = int(time_input[:2])
        get_north(time, 1)
    elif menu == "e":
        print("Bye until later!")
        exit()
    else:
        loop = True
        print()
        print("Invalid Entry")
