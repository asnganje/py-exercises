print("How many kilometers did you run today? \n")
user_input = input()
print("Ok you said" + " " + user_input + "kms")
const = 0.60923
result = float(user_input)*const
print(f"Your {user_input}kms run is around {round(result, 2)}miles")