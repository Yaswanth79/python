import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    # Check if the response contains an error message
    if data.get('cod') != 200:
        print(f"Error: {data.get('message')}")
        return
    
    # If no error, print the weather details
    main = data.get('main', {})
    weather = data.get('weather', [{}])[0]
    
    print(f"Weather in {city}:")
    print(f"Temperature: {main.get('temp')}°C")
    print(f"Weather: {weather.get('description', 'No description available').capitalize()}")

if __name__ == "__main__":
    api_key = "your_api_key_here"  # Replace with your actual API key
    city = input("Enter city: ")
    get_weather(api_key, city)
