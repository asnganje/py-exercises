import random

random_num = random.randint(0,2)

options = ["rock", "paper", "scissors"]

print(".....rock......")
print(".....paper.....")
print(".....scissors..")

computer_player = options[random_num]

player1 = input("Please make your move:")
player1 = player1.lower().strip()

print("SHOOT!")

if (player1 == "rock" or player1 == "scissors" or player1 == "paper"):
    if player1 == computer_player:
        print(f"IT'S A TIE, No WINNER 🙌 in {player1} vs {computer_player}")
    elif computer_player == "rock":
        if player1 == "scissors":
            print(f"Computer Wins 🙌 in {player1} vs {computer_player}")
        if player1 == "paper":
            print(f"Human player Wins 🙌 in {player1} vs {computer_player}")
    elif computer_player == "paper":
        if player1 == "rock":
            print(f"Computer wins 🙌 in {player1} vs {computer_player}")
        elif player1 == "scissors":
            print(f"Human player Wins 🙌 in {player1} vs {computer_player}")
    elif computer_player == "scissors":
        if player1 == "paper":
          print(f"Computer Wins 🙌 in {player1} vs {computer_player}")
        if player1 == "rock":
          print(f"Human player Wins 🙌 in {player1} vs {computer_player}")
else:
    print("No winner! \nDid not choose correct option, try again!")
