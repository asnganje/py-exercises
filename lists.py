# demo = [1,2,3,4,5]
# len = len(demo)
# print(type(len))
# print(len)
import random

# tasks = list(range(1,5))
# check = 1 in tasks
# print(check)

# for num in tasks:
#   print(num)

# i=0
# len = len(tasks)
# while i < len:
#   print(tasks[i])
#   i+=1

tasks = list(range(1,5))
tasks.append(6)
tasks.extend([7])
tasks.insert(4,2)
print(tasks)
print(tasks[1::2])
print(tasks)
# print(tasks.count(2))
# tasks.reverse()
# tasks.sort()
# print(tasks)
# print(tasks.index(2))

# words = ["Coding", "is", "fun"]

# s=" ".join(words)
# print(s)
