import random
print('\nHeeello!! Welcome to my HANGMAN game!\n')

words = ['Cow', 'Chicken', 'Dog', 'Bird', 'Crocodile', 'Snake']
word = random.choice(words)
print(word)

print('Let\'s begin! Your word to guess the word below in 10 attempts!: \n')
attempts = 10

for i in word:
    print(i.replace(i, '_ '), end= ' ')
print('\n')

while attempts > 0:

    answer = input('Come on and guess the first letter: ').upper()

    if answer in word:
        print('Great! Indeed ' + answer + ' is in here!') 
    else:
        print('Kupsztal... ' + '\'' + answer + '\'' ' is not correct. you have '+ str(attempts - 1)+ ' tries!')
    attempts = attempts - 1

#Ok I'm a beginner programmer so 

# for i in word: # Now we make a for loop to iterate through randomly selected word so that user can see how many letters does the word have
#     print(i.replace(i, '_ '), end = '  ')

# print('\n')

# attempts = 10

