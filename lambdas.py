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
# print(peeps)
aas = list(filter(lambda n:n[0].lower() == "a", people))
# print(aas)

users = [
  {"username":"jeff", "tweets":["I love", "I hate"],
  "username":"joel", "tweets":["Yooh"],
  "username":"bob", "tweets":[]
  }
]

inactive_users = list(filter(lambda user: user["tweets"], users))
# print(inactive_users)
instructors = ["abdul", "auf", "mikes"]
m=list(map(lambda name: f"Your instructor is {name}",
    filter(lambda value: len(value) < 5, instructors )))
# print(m)

