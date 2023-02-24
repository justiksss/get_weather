from methods import get_weather, get_city, get_coord_from_city


def maker(latitude: str, longitude: str):
    dict_with_commands: dict = {1: get_weather, 2: get_city, 3: get_coord_from_city}

    command_number = int(input())

    dict_with_commands[command_number](latitude=latitude, longitude=longitude)


def main():
    latitude = input("Enter the latitude:")
    longitude = input("Enter the longitude:")

    commands_types = [
        "1)Get info by coordinates",
        "2)Get location",
        "3)Get coordinates",
    ]

    for command in commands_types:
        print(command)

    while True:
        maker(latitude=latitude, longitude=longitude)


if __name__ == "__main__":
    main()





