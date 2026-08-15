import random

random_num = random.randint(0,2)

options = ["rock", "paper", "scissors"]

print(".....rock......")
print(".....paper.....")
print(".....scissors..")

count = 0
human_score=0
computer_score=0
computer_player = options[random_num]

while True:
  player1 = input("Please make your move or press quit/q to stop:")
  player1 = player1.lower().strip()
  print("SHOOT!")
  if player1 == "quit" or player1 == "q":
    print("No WINNER, GAME did not complete!")
    break
  if (player1 == "rock" or player1 == "scissors" or player1 == "paper"):
      if count == 3:
          if human_score > computer_score:
              res = input(f"Yeaaah...Human being Wins 🙌 --> {human_score} - {computer_score}, try again? (y/n)")
              if res == "y":
                count = 0
                continue
              else:
                break
          elif computer_score > human_score:
            res1 = input(f"Yeaaah...Computer Wins 🙌 --> {computer_score} - {human_score} try again? (y/n)")
            if res1 == "y":
              count = 0
              continue
            else:
              break
          else:
            output = input(f"IT'S A TIE, No WINNER 😇  {human_score} - {computer_score}, try again? (y/n)")
            if output == "y":
              count = 0
              continue
            else:
              break
      else:
        if player1 == computer_player:
            print(f"IT'S A TIE, No WINNER 🙌 in {player1} vs {computer_player}")
            count += 1
        elif computer_player == "rock":
            if player1 == "scissors":
                print(f"Computer Wins 🙌 in {player1} vs {computer_player}")
                count += 1
                computer_score +=1
                random_num = random.randint(0,2)
                computer_player = options[random_num]
            if player1 == "paper":
                print(f"Human player Wins 🙌 in {player1} vs {computer_player}")
                count += 1
                human_score += 1
                random_num = random.randint(0,2)
                computer_player = options[random_num]
        elif computer_player == "paper":
            if player1 == "rock":
                print(f"Computer wins 🙌 in {player1} vs {computer_player}")
                count+=1
                computer_score +=1 
                random_num = random.randint(0,2)
                computer_player = options[random_num]
            elif player1 == "scissors":
                print(f"Human player Wins 🙌 in {player1} vs {computer_player}")
                count+=1
                human_score += 1
                random_num = random.randint(0,2)
                computer_player = options[random_num]
        elif computer_player == "scissors":
            if player1 == "paper":
              print(f"Computer Wins 🙌 in {player1} vs {computer_player}")
              count += 1
              computer_score +=1
              random_num = random.randint(0,2)
              computer_player = options[random_num]
            if player1 == "rock":
              print(f"Human player Wins 🙌 in {player1} vs {computer_player}")
              count += 1
              human_score += 1
              random_num = random.randint(0,2)
              computer_player = options[random_num]
  else:
      res = input("No winner! \nDid not choose correct option, try again? (y/n)")
      if res == "y":
          continue
      else: 
          break
          
