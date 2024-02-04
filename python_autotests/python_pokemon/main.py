import requests
import random
import string

# Заменяем значение на предоставленный вам токен
trainer_token = "2afff038cfca7c5b738492946e5e2172"

# URL для API
base_url = "https://api.pokemonbattle-stage.me:9101"

# Генерация случайного имени покемона
def generate_random_name(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Создание покемона
create_pokemon_url = f"{base_url}/pokemons"
create_pokemon_payload = {
    "name": generate_random_name(),  # Генерируем случайное имя покемона
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
create_pokemon_headers = {
    "Content-Type": "application/json",
    "trainer_token": trainer_token
}

try:
    response = requests.post(create_pokemon_url, json=create_pokemon_payload, headers=create_pokemon_headers)
    created_pokemon_id = response.json()["id"]  # Сохраняем идентификатор созданного покемона
    print("Response from creating Pokemon:")
    print(response.json())  # Выводим ответ в формате JSON
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
except requests.exceptions.RequestException as e:
    print(f"Request Exception: {e}")

# Поймать покемона в покебол
catch_pokemon_url = f"{base_url}/trainers/add_pokeball"
catch_pokemon_payload = {
    "pokemon_id": created_pokemon_id  # Используем идентификатор созданного покемона
}
catch_pokemon_headers = {
    "Content-Type": "application/json",
    "trainer_token": trainer_token
}

try:
    response = requests.post(catch_pokemon_url, json=catch_pokemon_payload, headers=catch_pokemon_headers)
    print("\nResponse from catching Pokemon in Pokeball:")
    print(response.json())  # Выводим ответ в формате JSON
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
except requests.exceptions.RequestException as e:
    print(f"Request Exception: {e}")
