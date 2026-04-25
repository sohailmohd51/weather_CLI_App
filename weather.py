# Import required modules
import requests
import json
import csv

while True :
	

	api_key = "YOUR_API_KEY"

	city = input('Enter City Name : ')
	if city == "exit":
		print("App Quit !")
		break

	url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

	response  = requests.get(url)

	data = response.json()

	#print (json.dumps(data, indent=4))
	
	if data["cod"] != 200:
		print ('City Not Found.')
		exit()

	city = data["name"]
	lat_Long = data["coord"]
	temprature = data["main"]["temp"]
	weather_Condition = data["weather"][0]["description"]
	feels_like = data["main"]["feels_like"]
	min_temp = data["main"]["temp_min"]
	max_temp = data["main"]["temp_max"]
	humidity = data["main"]["humidity"]
	visibility = data["visibility"]
	wind_speed = data["wind"]["speed"]
	country = data["sys"]["country"]

	row = [city, lat_Long, temprature, weather_Condition, feels_like, min_temp, max_temp, humidity, wind_speed, country]
	
	print("\n--- Weather Report ---")
	print(f'City Name : {city}')
	print(f'Coordinates : {lat_Long}')
	print(f'Temprature : {temprature} °C')
	print(f'Weather Condition : {weather_Condition}')
	print(f'Feels like : {feels_like} °C')
	print(f'Min-Temp : {min_temp} °C')
	print(f'Max-Temp : {max_temp} °C')
	print(f'Humidity : {humidity} %')
	print(f'Visibility : {visibility} meters')
	print(f'Wind-Speed : {wind_speed}, m/s')
	print(f'Country : {country}')

	# Saving City Data in to the csv file
	with open("weather-data.csv", "a", newline="") as file:
		writer = csv.writer(file)
		writer.writerow(row)
	
	
	






