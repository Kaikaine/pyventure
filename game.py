player_name = input("Hello, what is your name?: ")


class Player:
    def __init__(self, items, location, name):
        self.items = items
        self.location = location
        self.name = name

    def __str__(self):
        return self.name

    def current_location(self):
        print(f"My current location is: {self.location} \n")

    def view_items(self):
        print(self.items)


class Room:
    def __init__(self, area):
        self.area = area


class Outside:
    def __init__(self, name, north, south, east, west, items):
        self.name = name
        self.items = items
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def move_north(self, north):
        pass


print(f"Hello {player_name} and welcome to my game")