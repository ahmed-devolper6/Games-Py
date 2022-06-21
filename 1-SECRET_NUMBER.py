Secret_number = 20
print("i have One Secret number it bigger than 10 smaller than 30...")
print("print X to exit form The game: ")
while True:
    
    Guessing_number = input("Guess the number: ")
    if Guessing_number == "x":
        print("Tanks")
        break
    try:    
        Guessing_number = int(Guessing_number)
        if Guessing_number != Secret_number:
            if Guessing_number > Secret_number:
                print(f"you git close but the number is smaller than {Guessing_number}")
            elif Guessing_number < Secret_number:
                print(f"you git close but the number is bigger than {Guessing_number}")
        if Guessing_number == Secret_number:
            print("Congrats!")
            break
    except:
        print("Type i number plesse! ")
        continue
