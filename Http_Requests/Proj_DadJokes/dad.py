import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("DAD-JOKE 300")
color_header = colored(header,color = "magenta")
print(color_header)
user_input = input("What you you like to search for??")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
	url,
	headers={"Accept": "application/json"},
	params = {"term":user_input}
	).json()

num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1 :
	print(f"I found {num_jokes} jokes about {user_input} . Here is one :")
	print(choice(results)["joke"])
elif num_jokes == 1:
	print(res["results"][0]["joke"])
	print("There is one joke")
else:
	print("There are no jokes")
# print(res)