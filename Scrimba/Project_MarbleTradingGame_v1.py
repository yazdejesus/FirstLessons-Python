from random import choice as c
#create bag of marbles with 10 marbles: 6 green, 4 red
bag = ["green","red","green","red","green","red","green","red","green","green"]
#decide bet before each turn
bet = int(input("Welcome to trade game. Your current balance is 1000  gp. \n Please select how much you want to bet."))
#day starts with 1000 gp in purse
purse = 1000
rounds = 1
#draw 1 marble randomly. if drawn green win same as bet, if red lose same as bet
while purse > 500:
    trade = c(bag)
    if bet != 0:
        if trade == "green":
            purse += bet
            msg = "Awesome! You won "+ str(bet) +"gp. Your current balance is "+ str(purse) +"gp."
        elif trade == "red":
            purse -= bet
            msg = "Oh, No! You lost "+ str(bet) +"gp. Your current balance is "+ str(purse) +"gp."
        bet = int(input(f"{msg} \n Select how much you want to bet or press 0 to exit game \n Rounds played {rounds}"))
        rounds += 1
    else:
        print("You chose to end the game")
        break

if purse <= 500:
    print(f"Thanks for playing, but you ran out of money, come back later. \n Final balance {purse}. \n Rounds played {rounds-1}")
else:
    print(f"Thanks for playing. You are a very lucky guy and managed to not run out of money. \n Final balance {purse}. \n Rounds played {rounds-1}")
#marbles are replaced after each round, which means the bag will always have 10
#number of rounds is variable, but game ends when purse has less than 500 gp
#print results on screen to let trader know how things are going
#advanced mode replace 1 green with 1black marble +10x score and 1 red with 1white marble -5x score