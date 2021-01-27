from random import choice as c
#create bag of marbles with 10 marbles: 6 green, 4 red
bag = ["green","red","green","red","green","red","green","red","green","green"]
bag_a = ["green","red","green","red","green","red","green","white","black","green"]
#decide bet before each turn
mode = input("please select mode of play. \n 1 - for standard mode \n 2 - for advanced mode")
bet = int(input("Welcome to trade game. Your current balance is 1000 gp. \n Please select how much you want to bet."))
#day starts with 1000 gp in purse
purse = 1000
rounds = 1
#draw 1 marble randomly. if drawn green win same as bet, if red lose same as bet
while purse > 500:
    if mode == "1":
        trade = c(bag)
    elif mode == "2":
        trade = c(bag_a)
    if bet != 0:
        if trade == "green":
            purse += bet
            msg = "Awesome! You won "+ str(bet) +"gp. Your current balance is "+ str(purse) +"gp."
        elif trade == "red":
            purse -= bet
            msg = "Oh, No! You lost "+ str(bet) +"gp. Your current balance is "+ str(purse) +"gp."
        elif trade == "black":
            purse += bet*10
            msg = "Super Luck! You won "+ str(bet*10) +"gp. Your current balance is "+ str(purse) +"gp."
        elif trade == "white":
            purse -= bet*5
            msg = "What a disaster! You lost "+ str(bet*5) +"gp. Your current balance is "+ str(purse) +"gp."
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