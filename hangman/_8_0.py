import random

def hangman(word):
    wrong = 0
    stages = ["",
              "_ _ _ _ _ _ _ _ _ _",
              "|        |         ",
              "|        |         ",
              "|        O         ",
              "|       /|\        ",
              "|       / \        ",
              "|                  "
               ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
            print((" ".join(board)))
        else:
            wrong += 1
            print((" ".join(board)))
            e = wrong + 1
            print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You Win!")
            print((" ".join(board)))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You Lose! It was {}".format(word))


words = ["bible", "british", "apple", "cpu", "computer", "games", "lockes", "jaime", "prescott"]

words = random.choice(words)

hangman(words)


