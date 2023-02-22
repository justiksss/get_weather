from dataclasses import dataclass



@dataclass
class Settings:

    def __init__(self):

        self.latitude: str = input('Enter the latitude:')
        self.longitude: str = input('Enter the longitude:')


