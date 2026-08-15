# li = range(0,8, 2)

# print(list(li))

# print("....ROOM CLEANLINESS....! \n")
# nums = input("How many times do I have to tell you? ")
# nums = int(nums)
# for time in range(nums):
#   print(f" TIME {time}: CLEAN UP YOUR ROOM! \n")

# nums = range(1, 21)

# for num in nums:
#     if num == 4 or num == 13:
#         state = "unlucky"
#     elif num % 2 == 0:
#         state = "even"
#     else:
#         state = "odd"
#     print(f"{num} is {state}")

# msg=input("What is your secret word? ")
# while msg != "Abdul":
#   msg = input("Try again!:")
# print(f"Wow! Congratulations {msg}!")

# num = 1

# while num <= 10:
#   print(num)
#   num +=1
# num = 1
# while num < 10:
#   print("😆" * num)
#   num+=1

# for n in range(3):
#   nums = range(1,10)
#   for num in nums:
#     print("😀" * num)

# response = ""
# print("How is it going?")
# while response != "stop copying me":
#   response=input(f"{response} \n")
# print("UGH!, FINE YOU WIN!")

# print("....EXIT CODE....")
# while True:
#   command = input("Type \"Exit\", to Exit \n")
#   if command == "Exit":
#     print("Bye... see you, Tomorrow!")
#     break

# for x in range(10):
#   print(x)
#   if x == 5:
#     break

times = input("How many times should I tell? \n")
times = int(times)

for time in range(1,times):
  print("CLEAN UP YOUR ROOM!")
  if time >= 5:
    print("Do you even listen anymore!")
    break