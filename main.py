import random
import os
from hangman_art import logo , stages
from hangman_words import word_list
while input("Do you want to play HangMan? Enter 'y' for yes or 'n' for no: ") == 'y':
    if 'y':
        os.system('cls')
    #Initialise variables
    print(logo)
    chosen_word = random.choice(word_list)
    length_word = len(chosen_word)
    lives = 6
    used_letters = []
    #print(chosen_word) - for checking if the code is working properly
    display_list = []
    #Game Loop
    for letter in chosen_word:
        display_list.append("_")
    game_end = False
    while not game_end:
        #Ask user if letter already used
        guess = (input("\nGuess a letter: ")).lower()
        #check if letters are already used
        if guess in used_letters:
            print("Letter used already.") 
            continue #no lives to be deducted
        else:
            used_letters.append(guess) #adds letter to used letter list
        #Check if letter is in word
        for i in range(length_word):
            letter = chosen_word[i]
            if letter == guess:
                display_list[i] = letter
        #If letter not in word do the below
        if guess not in chosen_word:
            print(f"\n You guessed {guess}, that is not in the word. You lost a life.")
            print(f"\n Letters guessed are {used_letters}")
            lives -= 1 #Deduct lives to update game state
            print(stages[lives])
            #Hint at the last life
            if lives == 1:
                if guess not in chosen_word:
                    remaining_letters = set(chosen_word) - set(used_letters)
                    revealed_letter = random.choice(list(remaining_letters))
                print(f"Hint: {revealed_letter}")
            if lives == 0:
                game_end = True
                print("You Loose!!\n")
                print(f"The word was {chosen_word}")
        print(f"{' '.join(display_list)}")
        #Check if the word has been guessed
        if '_' not in display_list:
            game_end = True
            print("You WIN!!!")
    used_letters.append(guess) # Add letters to used letters list

         



