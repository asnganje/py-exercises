print(".....rock......")
print(".....paper.....")
print(".....scissors..")

player1 = input("Player 1 make your move:")
player2 = input("Player 2 make your move:")

print("SHOOT!")
winner = None

if (player1 == "rock" or player1 == "scissors" or player1 == "paper") and (player1 == "rock" or player1 == "scissors" or player1 == "paper"):
  if player1 == player2:
    winner = None
    print(f"IT'S A TIE, No WINNER 🙌 in {player1} vs {player2}")
  elif player1 == "rock" and player2 == "paper":
      winner = player2
      print(f"Player 2 Wins 🙌 in {player1} vs {player2}")
  elif player1 == "rock" and player2 == "scissors":
      winner = player1
      print(f"Player 1 Wins 🙌 in {player1} vs {player2}")  
  elif player1 == "scissors" and player2 == "rock":
      winner = player2
      print(f"Player 2 Wins 🙌 in {player1} vs {player2}")
  elif player1 == "scissors" and player2 == "paper":
      winner = player1
      print(f"Player 1 Wins 🙌 in {player1} vs {player2}")
  elif player1 == "paper" and player2 == "rock":
        winner = player1
        print(f"Player 1 Wins 🙌 in {player1} vs {player2}")
  elif player1 == "paper" and player2 == "scissors":
      winner = player2
      print(f"Player 2 Wins 🙌 in {player1} vs {player2}")
else:
  print("No winner! \nDid not choose correct option, try again!")