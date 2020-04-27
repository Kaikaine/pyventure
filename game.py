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
        return

    def view_items(self):
        print(self.items)
        return

    def move_room(self):
        command = input("Please choose from one of these commands. 'N' 'S' 'E' 'W': ")
        if command.lower() == "n":
            Room(self.location).area.move_north
        elif command.lower() == "e":
            self.location = self.location.move_east()
        elif command.lower == "s":
            Room.area.move_south
        elif command.lower() == "w":
            Room.area.move_west
        elif command.lower == "q":
            pass
        else:
            print("I did not recognize that command \n")


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

    def move_north(self):
        Player.location = self.north
        return

    def move_east(self):
        print(f"Player moved to: {self.east} \n")
        return self.east

    def move_south(self):
        Player.location = self.south
        return

    def move_west(self):
        Player.location = self.west
        return

    def __str__(self):
        return self.name


print(f"Hello {player_name} and welcome to my game")
new_player = Player(["flashlight"], Outside("Outside", "Tower entrance", None, "car", None, ["key"]), player_name)
print(new_player.location)
new_player.move_room()
new_player.current_location()