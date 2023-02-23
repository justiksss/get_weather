from methods import Methods
from methods import user


class Session(Methods):
    commands_tuple: tuple = ("1)Get temperature", "2)Get location", "3)Get coordinates")
    for q in commands_tuple:
        print(q)
    number_of_command: int = int(input("Enter what to do:"))


    dict_with_commands: dict = {
        1: user.get_weather(),
        2: user.get_city(),
        3: user.get_coord_from_city()
    }
    if not isinstance(number_of_command,int):
        if not 0<number_of_command<len(dict_with_commands.keys()):
            raise AttributeError("Enter correct value")

    for i in dict_with_commands.keys():
        if number_of_command == i:
            dict_with_commands.get(i)