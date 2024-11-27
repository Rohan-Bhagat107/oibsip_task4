import requests

city_name=input("Enter your city name: ")
API_key="893c5086208412ae5ceb8aefbb562ec9"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    print("Current Temperature: ",data["main"]["temp"])
    print("Current Weather: ",data["weather"][0]["description"])
    print("Humidity : ",data["main"]["humidity"])
    