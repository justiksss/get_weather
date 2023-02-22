from geopy.geocoders import Nominatim
from config import Settings
import requests
import json
geolocator = Nominatim(user_agent="MyApp")

class Methods(Settings):
    def get_wheater(self):
        link_to_get_json_from_api: str = f'https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.latitude}&hourly=temperature_2m'
        response = requests.get(link_to_get_json_from_api).text # dict with all wheater >>> json.loads(response)
        all_time_info: list = json.loads(response).get('hourly').get("time")
        all_temperature_info: list = json.loads(response).get('hourly').get("temperature_2m")
        time_temperature_pair: list = list(zip(all_temperature_info,all_time_info))# list with pair in tuple time/temp (len 168)
        print(time_temperature_pair)
    def get_city(self):
        city = geolocator.reverse(self.longitude+","+self.latitude) # city from coord
        print(city)
    def get_coord_from_city(self):
        pass


user = Methods()
user.get_city()
user.get_wheater()