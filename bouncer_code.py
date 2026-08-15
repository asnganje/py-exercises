age=input("How old are you: ")
if not age:
  print("You did not enter any age!")
else:
  try:
    age = int(age)
    if not isinstance(age, int):
      print("Please enter a number value")
    else:
      if age >= 18 and age <= 21:
        print("You need a wristband")
      elif age > 21:
        print("Normal entry")
      else:
        print("Sorry, you are too young!")
  except ValueError:
    print("Please enter number value only")