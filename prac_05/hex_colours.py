COLOUR_CODES = {"RED": "ff0000", "ORANGE": "ffa500",
               "YELLOW": "ffff00", "GREEN": "00ff00",
               "BLUE": "0000ff", "PURPLE": "a020f0",
               "PINK": "ffc0cb", "BLACK": "000000",
                "WHITE": "ffffff", "GREY": "bebebe"}
# print(STATE_NAMES)

colour = input("Enter Colour: ").upper()
while colour != "":
    if colour in COLOUR_CODES:
        print(colour, "is", COLOUR_CODES[colour])
    else:
        print("Invalid Colour")
    colour = input("Enter Colour: ")
