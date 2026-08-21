from termcolor import colored
import pyfiglet
import requests
from random import randint

url = "https://icanhazdadjoke.com/search"


def joker():
    topic = "DadJoke2026"
    topic = pyfiglet.figlet_format(topic)
    print(colored(topic, "cyan"))
    term = input("Let me tell you a joke! Give me a topic: \n")
    res = requests.get(url, headers={
        "Accept": "application/json"}, params={"term": f"{term}"})
    data = res.json()
    numJokes = len(data["results"])
    if numJokes:
        resT = randint(0, numJokes-1)
        print(f"I have got {len(data["results"])} jokes about {term}. Here is one: \n")
        return data["results"][resT]["joke"]
    else:
        return f"Sorry, I dont have any joke about {term}. Please try again!"
print(joker())
