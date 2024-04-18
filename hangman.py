import random

print('\nHeeello!! Welcome to my HANGMAN game!\n')

words = ['Cow', 'Chicken', 'Dog', 'Bird', 'Crocodile', 'Snake'] #maybe one day to use some existing word database somewhere :)
word = random.choice(words).upper()

print('Let\'s begin! Your word to guess the word below in 10 attempts!: \n')

attempts = 10
guessed_letters = []

display_word = ['_'] * len(word) # in previous version i used for loop, but think that approach is much more readable. Any pro programmers willing to discuss and broaden my horizons? :))
print(' '.join(display_word) + '\n')

while attempts > 0:
    guess = input('Guess the letter!: ').upper()
    

    if guess in guessed_letters:
        print('You already guessed that letter! Try again.') # making sure no duplicates arrive! Think that was an issue and created a bug in previous version
        continue # I still have trouble using break/continue operators and tend to forget how useful they are. If i wouldn't use continue here it will just add that letter anyway because of what's stated below lol

    guessed_letters.append(guess)


    if guess in word:
        print('Good job! ' + guess + ' is in here:')
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
        print(' '.join(display_word))
        print()
    else:
        attempts -= 1
        print('Bah! ' + '\'' + guess + '\'' + ' is not correct. You have ' + str(attempts) + ' more tries!')

    if '_' not in display_word:
        print('Congrats! You have guessed the word: ', word)
        break
else:
    print('Sorry! you did not manage to guess the word in 10 tries')

