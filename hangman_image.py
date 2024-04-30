
def draw_hangman(incorrect):
    if incorrect == 0:
        print("\n+----+")
        print("|    '")
        print("|    ")
        print("|    ")
        print("|     ")
        print("---    ")

    elif incorrect == 1:
        print("\n+----+")
        print("|    '")
        print("|    O")
        print("|    ")
        print("|     ")
        print("---    ")

    elif incorrect == 2:
        print("\n+----+")
        print("|    '")
        print("|    O")
        print("|    |")
        print("|     ")
        print("---    ")

    elif incorrect == 3:
        print("\n+----+")
        print("|    '")
        print("|    O")
        print("|   /|")
        print("|     ")
        print("---    ")

    elif incorrect == 4:
        print("\n+----+")
        print("|    '")
        print("|    O")
        print("|   /|\\")
        print("|     ")
        print("---    ")

    elif incorrect == 5:
        print("\n+----+")
        print("|    '")
        print("|    O")
        print("|   /|\\")
        print("|   ^^^ ")
        print("---    ")

    elif incorrect == 6:
        print("\n+----+")
        print("|    '")
        print("|    O")
        print("|   /|\\")
        print("|   ^^^ ")
        print("|  ^^^^^ ")
        print("---    ")


draw_hangman(incorrect=6)

