import random

print("Witaj w swiecie wisielca, podaj swoj nick: ")
pseudonim = input()
def Wisielec():
    wrong = 0
    stages = ["",
              "           \n"
              "_________  \n",
              "|     |    \n",
              "|     0    \n",
              "|    /|\   \n",
              "|    / \   \n",
              "           \n"
              ]
    file=open("word.txt","r")
    spell=file.read().splitlines()
    tab=random.choice(spell)

    rleters = list(tab)
    board = ["__"] * len(tab)
    win = False
    print("Gra w Wisielca")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Odgadnij Litere: "
        char = input(msg)
        if char in rleters:
            cind = rleters.index(char)
            board[cind] = char
            rleters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print((" ".join(stages[0: e])))
        if "__" not in board:
            print(pseudonim + " Wygrałes!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print(pseudonim+" Przegrałes ! Miałes odgadnac: {}.".format(tab))

Wisielec()
