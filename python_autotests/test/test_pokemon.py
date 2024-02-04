import pytest
import requests

# Задаем значения для тестов
base_url = "https://api.pokemonbattle-stage.me:9101"
trainer_id = 2042  # ID вашего тренера

# Тест 1: Проверка, что ответ запроса GET /trainers приходит с кодом 200
def test_get_trainers_response_code():
    url = f"{base_url}/trainers?id={trainer_id}"
    response = requests.get(url)
    assert response.status_code == 200

# Тест 2: Проверка, что в ответе приходит строка с именем тренера
def get_trainer_name(trainer_id):
    url = f"{base_url}/trainers?id={trainer_id}"
    response = requests.get(url)
    trainer_data = response.json()
    if 'name' in trainer_data:
        return trainer_data['name']
    else:
        return None

# Использование функции для получения имени тренера по его id
trainer_id = 2042
trainer_name = get_trainer_name(trainer_id)
print(f"Имя тренера с id {trainer_id}: {trainer_name}")