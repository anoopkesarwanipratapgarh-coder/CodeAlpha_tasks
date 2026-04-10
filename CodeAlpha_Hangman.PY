import random 

#predefined word list
words=["apple", "banana","tiger", "chair","palnt"]
#computer randomly choose the word
word =random.choice(words)
#create blanck display 
display =["_"]*len(word)
#count of wrong guesses
wrong_guesses=0
while wrong_guesses<6 and "_" in display:
    print("word:"," ".join(display))

    guess = input("Enter a letter:")

    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                display[i]=guess
    else:
        wrong_guesses+=1
        print("Wrong guess!! Remaining chamces :", 6-wrong_guesses)  
#check win or loss
if "_" not in display :
    ("🎉YOU WIN! the word was:", word) 
else:
    print("YOU LOST! THE WORD WAS:", word)