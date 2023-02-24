from geopy.geocoders import Nominatim
import requests

geolocator = Nominatim(user_agent="MyApp")


def get_weather(latitude: str, longitude: str):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    response = requests.get(api_url).json()

    all_time_info = response["hourly"]["time"]
    all_temperature_info = response["hourly"]["temperature_2m"]

    print("----Temperature for this time----")
    for i in all_time_info[6:24:2]:
        print(i)
    print(
        f"Max temperature:{max(all_temperature_info)}\n"
        f"Min temperature:{min(all_temperature_info)}\n"
        f"Average temperature:{sum(all_temperature_info) // 168}"
    )


def get_city(latitude: str, longitude: str):
    city = geolocator.reverse(longitude + "," + latitude)
    if city is None:
        print(f"Could not find the city from this ({latitude},{longitude}) coordinates")
    else:
        print(f"Location is:{city}")


def get_coord_from_city(latitude: str, longitude: str):
    city_input = input("Enter a city:")
    if city_input is str:
        location = geolocator.geocode(city_input)
        if location is not None:
            latitude = location.latitude
            longitude = location.longitude
            print(f"The coordinates of {city_input} are: ({latitude}, {longitude})")
        else:
            print(f"Could not find the location of {city_input}")
    else:
        raise ValueError("Enter a real city!")

