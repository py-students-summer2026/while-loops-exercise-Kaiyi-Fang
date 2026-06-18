def get_starting_number():
    answer = input("How many bottles of beer on the wall? ")
    while answer.isnumeric() == False or int(answer) < 1:
        answer = input("How many bottles of beer on the wall?")
    return int(answer)

def sing(starting_number):
    bottles = starting_number
    keep_singing = True
    while keep_singing:
        if bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print(
                "Take it down, pass it around, "
                "no more bottles of beer on the wall!"
            )
        elif bottles == 2:
            print("2 bottles of beer on the wall, 2 bottles of beer.")
            print(
                "Take one down, pass it around, "
                "1 bottle of beer on the wall."
            )
            print()
        else:
            print(
                str(bottles)
                + " bottles of beer on the wall, "
                + str(bottles)
                + " bottles of beer."
            )
            print(
                "Take one down, pass it around, "
                + str(bottles - 1)
                + " bottles of beer on the wall."
            )
            print()
        bottles = bottles - 1
        if bottles <= 0:
            keep_singing = False