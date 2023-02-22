from dataclasses import dataclass
import requests
import json
@dataclass
class Settings:

    def __init__(self, latitude, longitude):

        self.latitude: float = latitude
        self.longitude: float = longitude


    def get_data(self):

        link_to_get_json_from_api: str = f'https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}&hourly=temperature_2m'
        response = requests.get(link_to_get_json_from_api).text
        dictionary_with_info = json.loads(response)
        all_time : list = dictionary_with_info.get('hourly').get("time")
        all_temperature: list = dictionary_with_info.get('hourly').get("temperature_2m")
        list_time_temperature: list = list(zip(all_temperature,all_time))
        for i in list_time_temperature:
            print(i)





def main():
    user = Settings(float(input('Enter the latitude:')), float(input('Enter the latitude:')))
