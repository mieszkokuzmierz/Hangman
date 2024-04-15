import random
print('\nHeeello!! Welcome to my HANGMAN game!\n')

words = ['Cow', 'Chicken', 'Dog', 'Bird', 'Crocodile', 'Snake']
word = random.choice(words).upper()

print('Let\'s begin! Your word to guess the word below in 10 attempts!: \n')
attempts = 10

for i in word:
    print(i.replace(i, '_ '), end= ' ')
print('\n')

guessed_letters = []

while attempts > 0:
    answer = input('Guess the letter!: ').upper()
    guessed_letters.append(answer)

    if answer in word:
        print('Good job! ' + answer + ' is in here:')
        for char in word:
            if char in guessed_letters:
                print(char, end = ' ')
            else:
                print('_ ', end = ' ')
        print()
    else:
        attempts = attempts - 1
        print('Bah! ' + '\'' + answer + '\'' + ' is not correct. You have ' + str(attempts) + ' more tries!')

    if set(word) == set(guessed_letters):
        print('Congrats! You have guessed the word: ', word)
        break
if attempts == 0:
    print('Sorry! you did not manage to guess the word in 10 tries')

