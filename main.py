from config import Settings



while True:
    list_with_command = ('1)Start', '2)Get info', '3)Get city by coordinates', '4)Get coordinates by city')

    for i in list_with_command:
        print(i)

    class Base(Settings):

        command_number = int(input("Enter what to do:"))+1

        def get_command(self):
            pass

