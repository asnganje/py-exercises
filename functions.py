# import random


# def coin_flip():
#   rand = random.randint(0,1)
#   if rand < 0.5:
#     return "HEAD"
#   return "TAIL"
# res = coin_flip()
# print(res)

# def sum_odd(nums):
#   total = 0
#   for num in nums:
#     if num % 2 != 0:
#       total += num
#   return total

# res = sum_odd([1,2,3,4,5,6,7])
# print(res)

# def speak(animal="dog"):
#     sounds = {
#         "pig":"oink",
#         "duck":"quack",
#         "cat":"meow",
#         "dog":"woof"
#     }
#     if animal in sounds:
#         return sounds[animal]
#     return "?"
# res = speak("spider")
# print(res)

total = 0

def increment():
  global total
  total +=1
  return total

s = increment()
# print(s)

print("akbsajs".count("z"))