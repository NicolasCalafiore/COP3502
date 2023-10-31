## Nicolas Calafiore
## UFID:73404209
## COP 3502C
## psuedo-random blackjack game

import p1_random as p1 # import the module (do this on the first line of code)
rng = p1.P1Random()
isPlayerTurn = True;
playerCards = []
menuSelection = 1
gameNumber = 1
winCount = 0
tieCount = 0
lostCount = 0


def PrintStatistics(winCount, lostCount, tieCount, gameNumber): ## Function to print glboal statistics
    print(f"Number of Player wins: {winCount}")
    print(f"Number of Dealer wins: {lostCount}")
    print(f"Number of tie games: {tieCount}")
    print(f"Total # of games played is: {gameNumber}")
    print(f"Percentage of player wins: {(winCount/gameNumber)*100}%\n")

def OutputGameResult(dealerHand, tieCount, winCount, lostCount): ## Registers and returns game result. Outputs result.
    playerHandTotal = getPlayerHandTotal()

    print(f"Dealer's hand: {dealerHand}")
    print(f"Your hand is: {playerHandTotal}\n")


    if dealerHand == 21 and playerHandTotal == 21:
        print("It's a tie! No one wins!\n")
        tieCount += 1

    if dealerHand == playerHandTotal:
        print("It's a tie! No one wins!\n")
        tieCount += 1

    elif dealerHand <= 21 and dealerHand > playerHandTotal:
        print("Dealer wins!\n")
        lostCount += 1
    else:
        print("You win!\n")
        winCount += 1


    return tieCount, winCount, lostCount


def OutputPulledCard(card): ## Outputs the card previously dealt. Autoamtically outputs correct face card respective of their number
    cardStr = ""
    if card == 1: cardStr = "ACE"
    elif card == 11: cardStr = "JACK"
    elif card == 12: cardStr = "QUEEN"
    elif card == 13: cardStr = "KING"
    else:
        cardStr = str(card)
    print(f"Your card is a {cardStr}!")

def ResetGame(gameNumber): ## Clears player cards array to prepare for new round. Increments gameNumber
    gameNumber += 1
    playerCards.clear()
    return gameNumber

def GetMenuSelection(): ## Displays generic menu
    print("1.  Get another card")
    print("2.  Hold hand")
    print("3.  Print Statistics")
    print("4.  Exit\n")
    return int(input("Choose an option: "))

def OutputHandTotal(): ## Outputs the players total hand
    handTotal = getPlayerHandTotal()
    print(f"Your hand is: {handTotal}\n")

def PullCardFromDeck(): ## Retrives psuedo-random number and assigns it a value of 10 if equal to 11 or more. Adds to player cards list
    cardInt = rng.next_int(13) + 1;
    OutputPulledCard(cardInt)
    if cardInt > 10: cardInt = 10
    playerCards.append((cardInt))
    return cardInt

def SimulateDealerRound(): ## psuedo-random number 16 to 26
    dealerHand = rng.next_int(11) + 16
    return dealerHand

def getPlayerHandTotal(): ## Returns all values of player cards within player card list
    handTotal = 0
    for i in playerCards:
        handTotal += i
    return handTotal

def EvaluatePlayerHandTotal(): ## returns a response indicitive of a bust, jackpot, or safe hold
    handTotal = getPlayerHandTotal()
    if(handTotal < 21):
        return 0
    if(handTotal == 21):
        return 1
    if(handTotal > 21):
        return -1

while menuSelection != 4: ## While player does select exit
    print(f"START GAME #{gameNumber}\n")
    pulledCard = PullCardFromDeck()
    OutputHandTotal()
    handEvaluation = EvaluatePlayerHandTotal()


    while isPlayerTurn:
        menuSelection = GetMenuSelection() ## Displays menu
        print("")
        if (menuSelection == 1): ## Player chooses to hit
            pulledCard = PullCardFromDeck() ## Generates new card
            OutputHandTotal() ## Displays new card
            handEvaluation = EvaluatePlayerHandTotal() ## Returns int indicitive of bust, blackjack, or safe hold


            if handEvaluation == 1: ## Blackjack
                print("BLACKJACK! You win!\n")
                gameNumber = ResetGame(gameNumber)
                menuSelection = 5;
                winCount += 1
                break ## Exit round loop
            if handEvaluation == -1: ## Bust
                print("You exceeded 21! You lose.\n")
                gameNumber = ResetGame(gameNumber)
                menuSelection = 5;
                lostCount += 1
                break ## Exits round loop

        if(menuSelection == 2): ## Hold
            isPlayerTurn = False
            break ## Exit round loop

        if(menuSelection == 4): ## Exit
            isPlayerTurn = False
            break ## Exit rounds loop

        if(menuSelection == 3):
            PrintStatistics(winCount, lostCount, tieCount, gameNumber - 1) ## Displays statistics

        if(menuSelection < 1 or menuSelection > 4): ## Invalid input
            print("Invalid input!\nPlease enter an integer value between 1 and 4.\n")


    if(menuSelection != 4 and menuSelection != 5): ## If player did not select exit, busted, or blackjacked
        dealerHand = SimulateDealerRound()
        tieCount, winCount, lostCount = OutputGameResult(dealerHand, tieCount, winCount, lostCount)
        gameNumber = ResetGame(gameNumber)
        isPlayerTurn = True;



