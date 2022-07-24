import random
import hangman_art
import hangman_words

print(hangman_art.logo)
chosen_word =random.choice(hangman_words.words_list)

score = []
lives = 6
end_of_game = False
for _ in chosen_word:score.append("_")
while not end_of_game:
    user_guess = input("Guess a letter:").lower() 
    if user_guess in score:print(f"You already guessed {user_guess}")  
    for i in range(len(chosen_word)):
        if (user_guess == chosen_word[i]):
            score[i]=user_guess
    
    if user_guess not in chosen_word:
        lives-=1
        print(f"You guessed {user_guess}, that's not the word you lose a life")
        if lives ==0:
            print("You Lose!")
            end_of_game = True

    print(f"{' '.join(score)}")
    if "_" not in score: 
        print('You Win')
        end_of_game = True
    print(hangman_art.stages[lives])

print(f"The word is {chosen_word}")