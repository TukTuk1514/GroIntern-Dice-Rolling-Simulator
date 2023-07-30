import random

print("Dice Rolling Simulator\n")
def dice_value_figure(dice_value):
        if dice_value  == 1:
            print("┌─────────┐")
            print("│         │")
            print("│    ●    │")
            print("│         │")
            print("└─────────┘")

        elif dice_value == 2:
            print("┌─────────┐")
            print("│ ●       │")
            print("│         │")
            print("│       ● │")
            print("└─────────┘")

        elif dice_value == 3:
            print("┌─────────┐")
            print("│ ●       │")
            print("│    ●    │")
            print("│       ● │")
            print("└─────────┘")

        elif dice_value == 4:
            print("┌─────────┐")
            print("│ ●     ● │")
            print("│         │")
            print("│ ●     ● │")
            print("└─────────┘")

        elif dice_value == 5:
            print("┌─────────┐")
            print("│ ●     ● │")
            print("│    ●    │")
            print("│ ●     ● │")
            print("└─────────┘")

        elif dice_value == 6:
            print("┌─────────┐")
            print("│ ●     ● │")
            print("│ ●     ● │")
            print("│ ●     ● │")
            print("└─────────┘")

roll_dice=input(("Want to roll the dice (y/n): "))

if roll_dice.lower() == "y":
    again = True

    while again:
        dice_value=(random.randint(1,6))
        dice_value_figure(dice_value)
            
        another_roll = input("Want to roll the dice again (y/n): ")

        if another_roll.lower() == "y":
            continue
        else:
            break

