import art
import random 
from replit import clear
print(art.logo)


print("Welcome to the Blackjack game!")
print("\n***Blackjack is a card comparing game between one or more players and a dealer, where each player in turn competes against the dealer.***\n\nInterested? Enter your name, and start the game. All the best!😉")

def deal_card():

  random_bots_card = 0
  random_users_card = 0
  player_name = input("\nEnter your name here: ")
  print("\nShuffling...")
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_bots_card = random.choices(cards, k = 2)
  sum_of_bots_cards = sum(random_bots_card)
  random_users_card = random.choices(cards, k = 2)
  new_random_card_bot = random.choices(cards, k = 1)

  a = sum(random_users_card)
  print(f"\nYour cards: {random_users_card}, which sums to {a}")
  if sum(random_users_card) == 21 and len(random_users_card) == 2:
    print("$Blackjack$", "You win!")
    exit
  if sum( random_bots_card) == 21 and len( random_bots_card) == 2:
    print("Bot got a $Blackjack$", "Bot wins!")
    exit
  if sum_of_bots_cards < 17:
    random_bots_card.extend(new_random_card_bot)
    sum_of_bots_cards = sum(random_bots_card)
    print("\n**Bot draw an extra card!**")

  add_card = input("""\nWant to draw another card? Type 'y' to add card or 'n' to pass the cards: """).lower()

    
    #executes on choosing "y"
  if add_card == 'y':
    new_ran_card_user = random.choices(cards, k = 1)
    random_users_card.extend(new_ran_card_user)
    sum_of_users_card = sum(random_users_card)
    print(f"\nYour cards: {random_users_card}, which sums to {sum_of_users_card}")
    
    show_ans = input("\nEnter 's' to show the cards: ").lower()

    #shows cards and evaluates the winner
    if show_ans == 's':
      print(f"\nBots cards = {random_bots_card}, Total = {sum_of_bots_cards} || {player_name} = {random_users_card}, Total = {sum_of_users_card}")
      
      #calculates the winner after choosing y
      if sum_of_bots_cards > sum_of_users_card and sum_of_bots_cards <= 21:
        #checks if bot is the winner
            print("\nBot wins!")
            cl_or_nt = input("\nEnter 'c' to clear the screen: ").lower()
            if cl_or_nt == 'c':
              clear()
            

      elif sum_of_bots_cards < sum_of_users_card and sum_of_users_card <= 21:
        #checks if player is the winner
        print("\nYou win!") 
        cl_or_nt = input("\nEnter 'c' to clear the screen: ").lower()
        if cl_or_nt == 'c':
          clear()
        

      elif sum_of_bots_cards == sum_of_users_card:
        #checks if it is a draw
        print("\nIt's a draw!")
        cl_or_nt = input("\nEnter 'c' to clear the screen: ").lower()
        if cl_or_nt == 'c':
          clear()
      
  
  #executes on choosing "n" and evaluates the winner
  if add_card == 'n':
    print(f"\nBots cards = {random_bots_card}, Total = {sum_of_bots_cards} || {player_name} = {random_users_card}, Total = {a}")
    
  #calculates the winner after choosing n
  if sum_of_bots_cards > a and sum_of_bots_cards <= 21:
    #checks if bot is the winner
    print("\nBot wins!")
    cl_or_nt = input("\nEnter 'c' to clear the screen: ").lower()
    if cl_or_nt == 'c':
      clear() #clears the screen
    
  
  
  elif sum_of_bots_cards < a and a <= 21:
    #checks if player is the winner
    print("\nYou win!")
    cl_or_nt = input("\nEnter 'c' to clear the screen: ").lower()
    if cl_or_nt == 'c':
      clear() #clears the screen
    

  elif sum_of_bots_cards == a:
    #checks if it is a draw
    print("\nIt's a draw!")
    cl_or_nt = input("\nEnter 'c' to clear the screen: ").lower()
    if cl_or_nt == 'c':
      clear() #clears the screen
    
  
  #prints invalid output
  if add_card != 'y' and add_card != 'n'and add_card != 'q':
    print("\nInvalid input. Program terminated!")
    

deal_card() #final function

play_again = 'y'
#while loop will continue to run the program until player does not choses "q" to quit the Program
while play_again == 'y':
  play_again = input("\nWant to play again? Type 'y' to play or 'q' to exit: ").lower()
  if play_again == 'y':
    deal_card()

  elif play_again == 'q':
    print("\nProgram exited successfully! Thank you... Hope to see you again!")