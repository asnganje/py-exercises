# nums = [1,2,3]
# d = [x*10 for x in nums]
# print(d)

# name = "nasra"
# updated = [char.upper() for char in name]
# print(updated)
# friends = ["ashley", "matt", "michael"]

# fris = [friend[0].upper()+friend[1:] for friend in friends]
# fris = [friend.capitalize() for friend in friends]
# print(fris)

# range = [num*10 for num in range(1,5)]
# # print(range)
# b = [bool(val) for val in [0,1,""]]
# print(b) 

nums = [1,2,3,4,5,6]
# strs = [str(num) for num in nums]
# print(strs)
# even = [num for num in nums if num%2==0]
# odd = [n for n in nums if n %2 != 0]
# comb = [n*5 if n%2 != 0 else n/2 for n in nums]
# print(comb)

# words = ["Elie", "Tim", "Matt"]
# answer2 = [val[::-1].lower() for val in words]
# print(answer2)

# 

# nestedL = [[1,2,3], [4,5,6], [7,8,9]]

# [[print(val) for val in l] for l in nestedL]

# b = [[num for num in range(1,4)] for val in range(1,4)]
# print(b)

# c = [["x" if num % 2 != 0 else "o" for num in range(1,4)] for val in range(1,4)]
# print(c)
d = [["*" for num in range(1,4)] for val in range(1,5)]
print(d)