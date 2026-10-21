import requests
import os
import google.generativeai as genia

def get_weather(city: str = 'Kyiv'):
    url = f'https://wttr.in/{city}?format=j1'

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()

            current_temp = data['current_condition'][0]['temp_C']
            wind_speed = data['current_condition'][0]['windspeedKmph']
            humidity = data['current_condition'][0]['humidity']

            weather_text = {
                'city': city,
                'current_temp': current_temp,
                'wind_speed': wind_speed,
                'humidity': humidity,
                'code': 200
            }

            return weather_text
        else:
            return {
                    'error': "Не вдалося отримати дані про погоду",
                    'code': 404
            }


    except requests.exceptions.RequestException:
        return {
                'error': "Помилка з'єднання з інтернетом або сервером",
                'code': 404
        }


def ask_gemini(promt: str):
    api_key = os.getenv('GEMINI_API_KEY')

    if not api_key:
        return 'Помилка GEMINI ключ не знайдено'

    genia.configure(api_key=api_key)
    model = genia.GenerativeModel('gemini-3.8-flash')

    try:
        reponse = model.generate_content(promt)
        return reponse.text
    except Exception as e:
        return f'Помилка при запиті до GEMINI: {e}'


def weather_gemini(data: str):
    api_key = os.getenv('GEMINI_API_KEY')

    if not api_key:
        return 'Помилка GEMINI ключ не знайдено'

    genia.configure(api_key=api_key)
    model = genia.GenerativeModel('gemini-3.8-flash')

    try:
        reponse = model.generate_content(f'Привіт ти помічник який рекомендує '
                                         f'як одягтися або що взяти на вулицю. '
                                         f'Твоя задача порекомендувати щось якщо погода ось така {data}')
        return reponse.text
    except Exception as e:
        return f'Помилка при запиті до GEMINI: {e}'
