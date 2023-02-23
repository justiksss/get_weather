from methods import Methods
user = Methods()


class Session(Methods):

    while True:
        commands_tuple: tuple = ("1)Get info by coordinates", "2)Get location", "3)Get coordinates","4)Set new coordiantes")
        for i in commands_tuple:
            print(i)
        @staticmethod
        def main(number_of_command):
            dict_with_commands: dict = {
                1: user.get_weather,
                2: user.get_city,
                3: user.get_coord_from_city,
                4: user.set_coordinates
            }
            dict_with_commands.get(number_of_command)()


        main(int(input("Enter what to do:")))





