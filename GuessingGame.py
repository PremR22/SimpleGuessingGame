secret_word = "prix"
user_word = ""
guess_count = 1
guess_limit = 3
guess_available = True
hint = "1"
hint_count = 1
hint_available = 2
hint1 = "It is a four letter word"
hint2 = "first letter is 'p' and last letter is 'x' "

print("Welcome to the Guessing Game!!! \n\nYou have 3 chances and 2 hints. \nMind you it wont be easy. Good Luck guessing the word! Bwahaha!!!")
print("----------------------------------------------------------------------")
while user_word != secret_word and guess_available:
    if guess_count <= guess_limit:
        print("                                         (Enter 1 to get a hint) \n")
        user_word = input("Enter your guess: ")
        if user_word == hint:
            if hint_count < hint_available:
                print(hint1)
                print("One hint remaining!")
                print("----------------------------------------------------------------------")
                guess_count -= 1
                hint_count += 1
            elif hint_count == hint_available:
                print(hint2)
                print("No more hints remaining")
                print("----------------------------------------------------------------------")
                guess_count -= 1
                hint_count += 1
            else:
                print("No hints remaining!")
                print("----------------------------------------------------------------------")
        elif user_word == secret_word:
            print("You won the game!")
            break
        else:
            print("Wrong Guess! Try Again")
            print("----------------------------------------------------------------------")
        guess_count += 1
        if guess_count == 1:
            print("All chances remaining! Bruh try first")
        elif guess_count == 2:
            print("2 chances remaining! Think harder")
        else:
            print("Last chance! Use everything you got.")
    else:
        guess_available = False
        print("You are out of Guesses! \nGame Over!")


