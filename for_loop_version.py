def get_starting_number():
    while True:
        answer = input("How many bottles of beer on the wall? ")
        if answer.isnumeric():
            number = int(answer)
            if number >= 1:
                return number
            
def sing(starting_number):
    for i in range(starting_number):
        bottles = starting_number - i
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
                f"{bottles} bottles of beer on the wall, "
                f"{bottles} bottles of beer."
            )
            print(
                "Take one down, pass it around, "
                f"{bottles - 1} bottles of beer on the wall."
            )
            print()