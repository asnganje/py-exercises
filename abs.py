# print(abs(-12))
# print(round(12.76))
nums = [123, 3,6]
# print([num for num in nums if len(str(num)) == max(len(str(n)) for n in nums)].pop())
# print(max(abs(num) for num in nums))
# print(list(zip([1,2,3], [4,5,6])))

mid=[80,91,78]
end=[98,89,53]
studs=['dan', 'ang', 'kate']

results = {st:max(m,e) for st,m,e in zip(studs, mid,end)}
# print(results)
scores = zip(studs, (map( lambda pair: (pair[0]+pair[1])/2, zip(mid,end))))
# print(dict(scores))
str1 = "abdul"
str2="ozil"
# print("".join("".join(x) for x in zip(str1,str2)))
a=[1,2,3,4,5]
print(list(map(lambda k:k**3, filter(lambda val:val %2 == 0, a))))
