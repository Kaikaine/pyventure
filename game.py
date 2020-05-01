

class Player:
    def __init__(self, inventory, location, name):
        self.inventory = inventory
        self.location = location
        self.name = name
        self.back = None

    def __str__(self):
        return self.name

    def current_location(self):
        print(f"My current location is: {self.location} \n")
        return

    def view_items(self):
        print(self.inventory)
        return

    def search_ground(self):
        print(f"You searched the ground and found these lying around: {self.location.items}")

    def move_room(self):
        command = input("Please choose from one of these commands. "
                        "\n 'N' to go north "
                        "\n 'S' to go south "
                        "\n 'E' to go east "
                        "\n 'W' to go west"
                        "\n 'B' to go to the previous location"
                        "\n 'Q' to quit: ")
        if command.lower() == "n":
            if self.location.north is None:
                print("You cannot go that way")
                return
            self.back = self.location
            self.location = self.location.move_north()
        elif command.lower() == "e":
            if self.location.east is None:
                print("You cannot go that way")
                return
            self.back = self.location
            self.location = self.location.move_east()
        elif command.lower == "s":
            if self.location.south is None:
                print("You cannot go that way")
                return
            self.back = self.location
            self.location = self.location.move_south()
        elif command.lower() == "w":
            if self.location.west is None:
                print("You cannot go that way")
                return
            self.back = self.location
            self.location = self.location.move_west()
        elif command.lower() == 'b':
            if self.back is None:
                print("You have not moved yet")
                return
            temp = self.location
            self.location = self.back
            self.back = temp
        elif command.lower == "q":
            print("Thanks for playing, press enter to exit: ")
        else:
            print("I did not recognize that command \n")


class Room:
    def __init__(self, name, north, south, east, west, items):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.items = items

    def __str__(self):
        return self.name

    def move_north(self):
        print(f"Player moved to: {self.north} \n")
        return self.north

    def move_east(self):
        print(f"Player moved to: {self.east} \n")
        return self.east

    def move_south(self):
        print(f"Player moved to: {self.south} \n")
        return self.south

    def move_west(self):
        print(f"Player moved to: {self.west} \n")
        return self.west


player_name = input("Hello, what is your name?: ")
print(f"Hello {player_name} and welcome to my game")
new_player = Player(["flashlight"], Room("Outside", "Tower entrance", None, "car", None, ["key"]), player_name)
print(f"You are currently: {new_player.current_location()}")
new_player.search_ground()
new_player.move_room()
new_player.current_location()
