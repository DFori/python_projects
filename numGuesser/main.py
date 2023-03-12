import random
numbers = []
for i in range(1, 101):
    numbers.append(i)
import art
print(art.logo)
print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100")
#this is where the difficulty affects the lives
lives = ()
difficulty = input("Type 'easy' or ' hard': ")
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
else:
    print("invalid input")
#generate a random number and store it in a variable
secret_num = random.choice(numbers)
while lives != 0:
    guess = int(input("Make a Guess: "))
    if guess!= secret_num:
        lives -= 1
    if guess > secret_num:
        print("Too high")
    if guess < secret_num:
        print("Too low")
    if guess == secret_num:
        print(f"You got it the number is {guess}")
        print(f"You have {lives} lives left")
        print("You win!")
        break
    if lives == 0:
        print("You have run out of lives\n You lose!")