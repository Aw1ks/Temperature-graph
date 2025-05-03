import requests 
import pandas as pd
import matplotlib.pyplot as plt


def get_city_coordinates(city_name, country_code, url):
    params = {
        'where': f'country_code:"{country_code}" AND place_name:"{city_name}"', 
        'limit': 1 
    }

    response = requests.get(url, params=params) 
    response.raise_for_status()

    city_response = response.json()
    if city_response['results']:
        coordinates = city_response['results'][0].get('coordinates')
        name = city_response['results'][0].get('place_name')

        print(f'Название города: {name}')
        print(f'Координаты города: {coordinates}')
        return coordinates 
    else:
        print(f'Город {city_name} не найден в регионе {country_code}')
        return None 


def get_weather_data(coordinates, start_date, end_date, weather_url):
    params = {
        'latitude': coordinates['lat'],
        'longitude': coordinates['lon'],
        'hourly': 'temperature_2m',
        'start_date': start_date,
        'end_date': end_date,
    }

    response = requests.get(weather_url, params=params)
    response.raise_for_status()
    weather_response = response.json()

    weather = weather_response['hourly']['temperature_2m']
    time = weather_response['hourly']['time']

    return weather, time



def creating_schedule(temperature, time, city_name):
    df = pd.DataFrame({'time': time, 'temperature': temperature})
    df['time'] = pd.to_datetime(df['time'])

    plt.plot(df['time'], df['temperature'])

    plt.xlabel('Время')
    plt.ylabel('Температура (°C)')
    plt.title(f'График температуры в {city_name}')

    plt.grid(True)

    plt.show()


def main():
    url = 'https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/geonames-postal-code@public/records'
    weather_url = 'https://api.open-meteo.com/v1/forecast?'

    city_name = input(f'Введите название города в котором хотите узнать погоду (Должен начинаться с большой буквы на анголийском языке): ')
    country_code = input(f'Введите код страны (Должен быть большими буквами на английском языке "BY"): ')
    start_date = input(f'Введите дату начала периода (запишите дату в формате YYYY-MM-DD): ')
    end_date = input(f'Введите дату конца периода (запишите дату в формате YYYY-MM-DD): ')

    coordinates = get_city_coordinates(city_name, country_code, url)
    temperature, time = get_weather_data(coordinates, start_date, end_date, weather_url)
    creating_schedule(temperature, time, city_name)


if __name__ == '__main__':
    main()