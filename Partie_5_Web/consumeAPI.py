import requests
import json

url = "http://127.0.0.1:8000/api/GetPizzas"

response = requests.get(url)
# print(response.text)

pizzas = json.loads(response.text)
print(pizzas)
print(len(pizzas))

for pizzaModel in pizzas:
    pizza = pizzaModel['fields']
    print(pizza['nom'])