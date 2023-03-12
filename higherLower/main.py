import random

import game_data
import art
#generate random item from dictionary
person = random.choice(game_data.data)
a = person["name"]+" "+ person["description"]+" "+person["country"]
print(art.logo)
print(a)
#main game mechanics
game_over = True
score = 0
while game_over:
    person2 = random.choice(game_data.data)
    b = person2["name"] + " " + person2["description"] + " " + person2["country"]
    print(art.vs)
    print(b)
    c = ()
    c = b
    player_ans = input("Who has more followers? 'a' or 'b': ")
    if player_ans == "a":
        if person["follower_count"] > person2["follower_count"]:
            print("You got it!")
            print(c)
            score += 1
        else:
            print("You Lose!")
            game_over = False
    if player_ans == "b":
        if person2["follower_count"] > person["follower_count"]:
            print("You got it!")
            print(" ")
            print(c)
            score += 1
        else:
            print("You Lose!")
            game_over = False

print(score)
