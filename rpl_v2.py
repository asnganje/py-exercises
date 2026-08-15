print(".....rock......")
print(".....paper.....")
print(".....scissors..")

player1 = input("Player 1 make your move:")
print("******NO CHEATING******* \n"*20)
player2 = input("Player 2 make your move:")

print("SHOOT!")
winner = None

if (player1 == "rock" or player1 == "scissors" or player1 == "paper") and (player1 == "rock" or player1 == "scissors" or player1 == "paper"):
    if player1 == player2:
        winner = None
        print(f"IT'S A TIE, No WINNER 🙌 in {player1} vs {player2}")
    elif player1 == "rock":
        if player2 == "scissors":
            print(f"Player 1 Wins 🙌 in {player1} vs {player2}")
        if player2 == "paper":
            print(f"Player 2 Wins 🙌 in {player1} vs {player2}")
    elif player1 == "paper":
        if player2 == "rock":
            print(f"Player 1 Wins 🙌 in {player1} vs {player2}")
        elif player2 == "scissors":
            print(f"Player 2 Wins 🙌 in {player1} vs {player2}")
    elif player1 == "scissors":
        if player2 == "paper":
          print(f"Player 1 Wins 🙌 in {player1} vs {player2}")
        if player2 == "rock":
          print(f"Player 2 Wins 🙌 in {player1} vs {player2}")
else:
    print("No winner! \nDid not choose correct option, try again!")
