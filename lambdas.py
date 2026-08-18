# def sq(num):
#   return num**2
# print(sq(3))
# s=lambda num: num**2
# print(s(5))

nums = [2,4,6,7]
doubles = list(map(lambda n:n*2, nums))
# for num in doubles:
#   print(num)
# print(doubles)
people= ["Abdul", "Ozil", "Auf"]
peeps = list(map(lambda name: name.upper(), people))
print(peeps)