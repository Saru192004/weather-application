import tkinter as tk
from tkinter import messagebox
import requests

# Function to get weather information
def get_weather():
    api_key = 'ddae414b908f55c437a65efabe18ba11'  # Replace with your OpenWeatherMap API key
    city = city_entry.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data['cod'] == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            result = f'Temperature: {temperature}°C\nDescription: {weather_description}'
        else:
            result = 'City not found.'
    except Exception as e:
        result = 'Error occurred: ' + str(e)
    
    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title('Weather App')

# Create and place the widgets
city_label = tk.Label(root, text='Enter city:')
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text='Get Weather', command=get_weather)
get_weather_button.pack()

result_label = tk.Label(root, text='', padx=20, pady=20)
result_label.pack()

# Run the application
root.mainloop()
