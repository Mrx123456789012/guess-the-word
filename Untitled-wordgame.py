import random
words=["father","science","enterprsise","money","superman","batman","python"]
word=random.choice(words)
jumble=(''.join(random.sample(word,len(word))))
#print(jumble)
print(f"The jumble word is {jumble}")
guess = input("write your guess:")
if guess == word:
    print("correct answer")
else:
    print(f"Incorrect: The word is {word}")


