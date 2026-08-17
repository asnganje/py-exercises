cat = {
    "name": "blue",
    "age": 3.5,
    "isCute": True
}

# cat2 = dict(name="ozil", age = 0.5)

# print(cat2["name"])

# for k,v in cat2.items():
#   print(k,v)
# print("name" in cat2)

# d = cat.copy()
# print(d is cat)

# new_user = {}.fromkeys(["name", "age", "email", "profile"], "unknown")
# print(new_user.get("love"))
cat = {
    "name": "blue",
    "age": 3.5,
    "isCute": True
}

# cat.pop("age")
# cat.popitem()
# print(cat)
# sec = {"married":"no"}
# sec.update(cat)

# print(cat)
# print(sec)

play_list = {
    "title": "patagonia bus",
    "author": "colt",
    "songs": [
        {
            "title": "song1",
            "artist": ["kitty", "djKatt"],
            "duration": 2.05
        },
        {
            "title": "song2",
            "artist": ["blue"],
            "duration": 3.05
        },
        {
            "title": "meoww",
            "artist": ["garfied"],
            "duration": 2.01
        }
    ]
}

t = 0

# for song in play_list["songs"]:
#   t+=song["duration"]
t = sum(song["duration"] for song in play_list["songs"])
# print(t)

nums = {
  "first":1,
  "second":2,
  "third":3
}

squared = {key:value**2 for key,value in nums.items()}
# print(squared)
nums = [1,2,3,4]
s = {num:num**2 for num in nums}
# print(s)
str1="abc"
str2="123"
s = {str1[i]:str2[i] for i in range(0,len(str1))}
# print(s)
instructor = {"name":"colt", "city":"london", "color":"purple"}

yell = {(k.upper() if k == "color" else k):v.upper() for k,v in instructor.items()}
# print(yell)
nums = [1,2,3,4,5]
w= {num: ("even" if num%2==0 else "odd") for num in range(1,100) }
# print(w)

# answer = {}.fromkeys(["a","e","i","o","u"], 0)
answer = {m:chr(m) for m in range(65,91)}
print(answer)