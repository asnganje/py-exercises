s = set({1,2,3})
s={1,23,1}
# for num in s:
#   print(num)

names = ["abdul", "ozil", "nasra", "zaitun", "omar", "asya", "nafisa", "abdul", "nafisa", "asya", "omar"]
s.add(20)
s.discard(23)
t = s.copy()
t.clear()
# print(t)
math={"ozil", "sele"}
scie={"auf", "zaynab", "sele"}

# z= math | scie
z = math & scie
# print(z)

d= {x:x**3 for x in range(0,5)}
# print(d)
st = {char.upper() for char in "abdulll"}
# print(st)

def are_all_vowels(str):
  return len({char for char in str if char in "aeiou"}) == 5

print(are_all_vowels("sequioa"))