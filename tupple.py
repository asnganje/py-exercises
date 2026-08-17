# x = (1,2,3,4)
# print(x[0])

locations = {
  (35.4545, 18.0823): "Shirazi",
  (23.2345, 29.3004): "Bodo",
  (45.3940, 18.3223): "Funzi"
}

# print(locations[(45.3940, 18.3223)])
student = {
  "name":"suleiman",
  "bro":"auf",
  "father":"nganje",
  "mama":"asya"
}

# print(student.items())
# for loc in locations:
  # print(loc)

months = ("jan", "feb", "march", "april", "may", "june", "july", "aug", "sep", "october", "november", "december", "suleiman")
i = len(months)-1
while i >= 0:
  # print(months[i])
  i-=1

nums = (1,2,3,3,3,4,5,6,7,8,9)
print(nums.index(3))
