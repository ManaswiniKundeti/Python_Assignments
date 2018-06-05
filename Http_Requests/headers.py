import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"})
                              #headers={"Accept": "text/plain" to print the text data
                              #print(response.text)
#response.text is a string object and we cannot treat it like key:value pairs
# to get only the joke detail, we use response.json() as it gives a dictionary.so, it is easy to access the jokeas a key!
data = response.json() #.json() converts the response data to Python

print(data["joke"])
print(f"status: {data['status']}")



 