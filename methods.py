from geopy.geocoders import Nominatim
from config import Settings
import requests
import json
geolocator = Nominatim(user_agent="MyApp")

class Methods(Settings):
    def get_weather(self):
        link_to_get_json_from_api: str = f'https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.latitude}&hourly=temperature_2m'
        response = requests.get(link_to_get_json_from_api).text # dict with all wheater >>> json.loads(response)
        all_time_info: list = json.loads(response).get('hourly').get("time")
        all_temperature_info: list = json.loads(response).get('hourly').get("temperature_2m")

        # time_temperature_pair: list = list(zip(all_temperature_info,all_time_info)) list with pair in tuple time/temp (len 168)

        print(f"Max temperature:{max(all_temperature_info)}\nMin temperature:{min(all_temperature_info)}\nAverage temparature:{sum(all_temperature_info) // 168}")
        print("----Time is----")
        for i in all_time_info[6:24:2]:
            print(i)
    def get_city(self):   # get city from coordinates (coordinates init in settings)
        city = geolocator.reverse(self.longitude+","+self.latitude) # city from coord
        if city == None :
            print(f"Could not find the city from this ({self.latitude},{self.longitude}) coordinates")
        else:
            print(f"Location is:{city}")
    def get_coord_from_city(self):  # get coordinates of city (city get in function)
        city_input: str = input("Enter a city:")
        if isinstance(city_input,str):
            location = geolocator.geocode(city_input)
            if location is not None:
                latitude = location.latitude
                longitude = location.longitude
                print(f"The coordinates of {city_input} are: ({latitude}, {longitude})")
            else:
                print(f"Could not find the location of {city_input}")



user = Methods()