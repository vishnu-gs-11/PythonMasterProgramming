import random 
def hang_men():
    word_list = ["pugger","littelepugger","tiger","superman","thor","pokemon","avengers","savewater","global","planet"]
    word = random.choice(word_list)
    valid_letters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guess_made = ''
    
    while len(word) > 0:
        main = ""
        
        for letter in word:
            if letter in guess_made:
                main += letter
            else:
                main += "_" + " "

        if main == word:
            print(main)
            print("You're correct !...")
            break

        print("Guess the word ...", main)
        guess = input()

        if guess in valid_letters:
            guess_made += guess
        else:
            print("Enter a valid character :")
            guess = input()

        if guess not in word:
            turns -= 1 
            if turns == 9:
                    print("9 turns left")
                    print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break

name = input("Enter your name : ")
print("Welcome ! " + name + " ! ...." )
print("Let's start our hangmen game try to guess the word in less than 10 attempts")

hang_men()
print()