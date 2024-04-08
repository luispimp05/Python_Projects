#
from art import logo
import random
import os 
clear = lambda: os . system('clear')

print(logo)

# função para randomizar a saida de cartas da lista 
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
  
  
    return card    

# calcular os resultados
def calculate_score(cards):
    """ take a list of card and return the scores calculated from the cards"""
    
#check for a blackjack and return 0 instead of the actual score. 0 will represent blackjack in our game.
    #if 11 in cards and 10 in cards and len(cards) == 2
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # verificar se está junto com figura ou carta numérica :ás 
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    
    return sum(cards)

# verifica acontecimentos
def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'Draw'
    elif computer_score == 0:
        return "Lose, oppenent has blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21: 
        return "You went over. You loose"
    elif computer_score > 21:
        return "opponent went over. You win."
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
    
# reset à consola para pedir mais uma jogada
def play_another_round():
    #dar cartas ao user e ao dealer
    user_cards = []
    dealer_cards = []
    is_game_over = False

    #injetar cartas random nas listas vazias acima mencionadas
    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
        
        
    while not is_game_over:
            
        # chamar as funções 

        user_score = calculate_score(user_cards)  
        computer_score = calculate_score(dealer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {dealer_cards[0]}")

        # if th game has not ended, ask the user if thei want to draw another card if yes, then use the deal card() function to add another card to he user_cards list. If ni than the game is ended

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
            
            
        else:
                user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
                if user_should_deal == 'y':
                    user_cards.append(deal_card())
                    # print(user_cards)
                else:
                    is_game_over = True
                    
        # the score will need to be rechecked with every new card drawn and the checks in user_score and computer_score will needed to be repeated until the game ends.
        
        
        
        #dealer strategy não pedir mais cartas se tiver 17
        
    while computer_score != 0 and computer_score < 17:
        dealer_cards.append(deal_card())
        computer_score = calculate_score(dealer_cards)


    print(f"Your final hand : {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#chamadas de função dinamicas para o reset à consola e voltar a jogar novamente
while input("Do you wanna go for another round ?Type 'y' if yes type 'no' if not. ") == "y":
    clear()
    play_another_round()
