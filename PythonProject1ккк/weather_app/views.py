# weather_app/views.py
import requests
from django.shortcuts import render
from datetime import datetime

# Ваш API-ключ OpenWeatherMap
API_KEY = '86c326909ce732a85832b98b60b26452'


def index(request):
    city = 'Almaty'  # Город по умолчанию при первом запуске
    error_message = None
    current_weather = None
    forecast_data = []

    if request.method == 'POST':
        # 1. Получаем город из формы
        city = request.POST.get('city_name', '').strip()

    if city:
        # URL для текущей погоды
        current_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}&lang=ru'
        # URL для 5-дневного прогноза (каждые 3 часа)
        forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={API_KEY}&lang=ru'

        try:
            # Запрос 1: Текущая погода
            current_response = requests.get(current_url).json()
            if current_response.get('cod') == 404:
                error_message = f"Город '{city}' не найден. Попробуйте другой город в Казахстане."
                return render(request, 'weather_app/index.html', {'error_message': error_message})

            current_weather = {
                'city': current_response['name'],
                'temperature': current_response['main']['temp'],
                'description': current_response['weather'][0]['description'],
                'icon': current_response['weather'][0]['icon'],
                'humidity': current_response['main']['humidity'],
                'wind': current_response['wind']['speed'],
            }

            # Запрос 2: Прогноз на 5 дней
            forecast_response = requests.get(forecast_url).json()

            # Обработка данных прогноза
            for item in forecast_response['list']:
                # Форматируем дату и время
                dt_object = datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S')

                forecast_data.append({
                    'dt_txt': dt_object.strftime('%a, %H:%M'),  # Например: Пн, 15:00
                    'temp': item['main']['temp'],
                    'description': item['weather'][0]['description'],
                    'icon': item['weather'][0]['icon'],
                })

        except Exception as e:
            print(f"Ошибка запроса к API: {e}")
            error_message = "Не удалось получить данные о погоде. Проверьте API-ключ или подключение к интернету."

    context = {
        'current_weather': current_weather,
        'forecast_data': forecast_data,
        'error_message': error_message
    }

    return render(request, 'weather_app/index.html', context)