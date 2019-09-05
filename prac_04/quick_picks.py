import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    quick_picks = int(input("How many quick picks? "))
    while quick_picks < 0:
        print("Invalid number, must be greater than 0")
        quick_picks = int(input("How many quick picks? "))

    for i in range(quick_picks):
        quick_pick_list = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick_list:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick_list.append(number)
        quick_pick_list.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick_list))


main()
