import requests
from django.shortcuts import render

def home(request):
    weather_data = None
    error = None

    if 'city' in request.GET:  # Check if a city is provided
        city = request.GET['city']
        api_key = 'b1206708e5c8f9b06abb7f6b5b51427f'  
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response = requests.get(api_url)
            data = response.json()

            if response.status_code == 200:  
                kelvin_temp = data['main']['temp']
                celsius_temp = kelvin_temp - 273.15
                fahrenheit_temp = (celsius_temp * 9/5) + 32
                

                weather_data = {
                    'city': data['name'],
                    'temperature': {
                        'celsius': round(celsius_temp, 2),
                        'fahrenheit': round(fahrenheit_temp, 2),
                    },
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                }
            else:
                error = data.get('message', 'City not found.')

        except Exception as e:
            error = str(e)

    return render(request, 'weather.html', {'weather_data': weather_data, 'error': error})
