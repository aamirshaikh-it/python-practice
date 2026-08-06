import requests
from config import api_key

while True:
    
    city = input("Enter a City Name. (or 'q' to quit): ").lower()
    try:
        if city == "quit" or city == "q":
            break
        else:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
            response = requests.get(url)
            data = response.json()

            temp_kelvin = data['main']['temp']
            temp_celsius = temp_kelvin - 273.15 
            description = data["weather"][0]["description"]

            print(f"Temperature: {round(temp_celsius, 1)}°C")
            print(f"Conditions: {description}")
    except KeyError:
        print("City not found. Please check the spelling and try again.")