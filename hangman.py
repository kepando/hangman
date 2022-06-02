import os
import random

words_list = ["weigh","smart","pound","fleck","light"]

def hangman(word):
    wrong = 0
    stages = ["",
            "_______      ",
            "|        ",
            "|    |   ",
            "|    O   ",
            "|   /|\  ",
            "|   / \  ",
            "|       "
            ]
    rletters = list(word)
    board = ["__"] * len(word)
    guesses = list()
    win = False
    print("\nWelcome to Hangman\n")

    while wrong < len(stages) - 1:
        print("\n\n")
        print(" ".join(guesses))
        msg = "Guess a letter: "
        char = input(msg)
        guesses.append(char)

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
            os.system("clear")
        else:
            wrong += 1
            os.system("clear")
        
        print((" ".join(board)))
        
        e = wrong + 1
        print("\n".join(stages[0:e]))
        
        if "__" not in board:
            print("\nYou win!")
            print("The word was: ")
            print(" ".join(board))
            print("\n")
            win = True
            break
    if not win:
        print("\nYou lost! The word was \"{}\".\n".format(word))

# if we want Player 1 to pick a word
#secret = input("Please enter a word: ")
#os.system("clear")
#hangman(secret)
  
# if we want the word chosen from words_list above
os.system("clear")
secret = words_list[random.randint(0,len(words_list))]
hangman(secret)
