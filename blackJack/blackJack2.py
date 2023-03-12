import random
import art
def draw():
    """returns random card from deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def play_game():
    print(art.logo)
    user_card = []
    cpu_card = []
    game_over = False
    for i in range(2):
        user_card.append(draw())
        cpu_card.append(draw())
    print(f"your opponent's first card is {cpu_card}")

    #print(user_card)
    #print(cpu_card)\
    while game_over == False:
        def calculate_score(list_of_cards):
            score = sum(list_of_cards)
            if score == 21 and len(list_of_cards) == 2:
                return 0
            if 11 in list_of_cards and sum(list_of_cards) > 21:
                list_of_cards.remove(11)
                list_of_cards.append(1)
            return score

        user_score = calculate_score(user_card)
        cpu_score = calculate_score(cpu_card)
        print(f"Your cards = {user_card} and your score is {user_score}")
        #print(f"computer's cards = {cpu_card} and computer's score is {cpu_score}")
        def compare(user_score, cpu_score):
            if user_score == cpu_score:
                return "Draw"
            elif cpu_score == 0:
                return "Computer has a Black Jack\n You lose!"
            elif user_score == 0:
                return "You win! with a Black Jack"
            elif user_score > 21:
                return "You went over!\n you lose!"
            elif cpu_score > 21:
                return "computer went over!\n You win!"
            elif user_score > cpu_score:
                return "You win!"
            elif cpu_score > user_score:
                return "You lose!"
        if user_score == 0:
            print("You got a black Jack\n You win!")
        if cpu_score == 0:
            print("computer got a Black Jack\n You lose!")
        if user_score == 0 or cpu_score == 0:
            game_over = True
        else:


            again = input("Type 'y' to get another card and 'n' to pass: ")
            if again == "y":
                user_card.append(draw())
                user_score = calculate_score(user_card)
            else:
                while cpu_score != 0 and cpu_score < 15:
                    cpu_card.append(draw())
                    cpu_score = calculate_score(cpu_card)
                   # print(cpu_card)
                    #print(cpu_score)
                game_over = True
                print(compare(user_score, cpu_score))
                print(f"your opponent's final hand is {cpu_card} and score is {cpu_score}")
play_game()
while input("Do you want to play again?: ") == "y" or "yes":
    play_game()

