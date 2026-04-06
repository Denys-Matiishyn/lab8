import requests

# перевірка buyers
response2 = requests.get("http://127.0.0.1:5000/buyers")
print("Buyers:", response2.status_code)

# Перевіряємо тільки buyers
assert response2.status_code == 200
print("Усе працює ідеально!")