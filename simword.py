from random import sample
import gensim.downloader as api

print("Preparing stuff...")

corpus = api.load('text8')
wordlist = next(iter(corpus))
word = sample(wordlist,1)[0]
#print("word = ",word)

# Get word embeddings
#model = api.load('glove-twitter-25')
#model = api.load('glove-twitter-50')
#model = api.load('glove-twitter-100')
#model = api.load('glove-wiki-gigaword-100')
model = api.load('glove-wiki-gigaword-200')
similar = model.most_similar(word)

print("... Ready")
print()

nearestScore = similar[0][1]*100
print("Nearest word has similarity "+"{:6.2f}".format(nearestScore))
print()
print("To quit, enter 3 dots as your guessed word (...)")
print()

# Begin game loop
guessn = 1
more = True
while more:
    guess = input("Enter guess #"+"{:4d}".format(guessn)+" : ")
    if guess == word:
        print("Congratulations: you guessed the word!")
        more = False
    elif guess == "...":
        print("Oh well, better luck next time!")
        more = False
    else:
        score = model.similarity(guess,word)*100
        print("similarity score = "+"{:6.2f}".format(score))
        guessn += 1

    
        
