import requests
url = "https://api.kanye.rest/"

response = requests.get(url)

print(response.json()["quote"])



import requests
url = "https://api.kanye.rest/"

response = requests.get(url)
final_response = response.json()["quote"]
print(final_response)
