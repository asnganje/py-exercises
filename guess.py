import random
count = 0

num = random.randint(1,10)
while True:
  guess = input("Enter a number between 1-10: ")
  guess = int(guess)
  if count == 4:
    retry = input("You lost!!! Try again? (y/n)")
    if retry == "y":
      count = 0
    elif retry == "n":
      break
  if guess < num:
    print("Tool low! 🤦‍♀️")
    count+=1
  elif guess > num:
    print("Tool high! 🤦‍♀️")
    count+=1
  else:
    print("You win 🙌💪!")
    replay = input("Play again? (y/n)")
    if replay == "y":
      num = random.randint(1,10)
      count = 0
    elif replay == "n":
      break