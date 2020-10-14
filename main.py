class Player:

    def __init__(self, player_name, room):
        self.player_name = player_name
        self.room = room

    def enter_room(self, room):
        self.room = room

    def get_room(self):
        return self.room


class Room:

    def __init__(self, room_name):
        self.room_name = room_name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def print_room_options(self):
        print("(0) Verlassen")
        for i in range(len(self.rooms)):
            print("({}) Raum {}".format(str(i + 1), self.rooms[i].room_name))

    def room_prompt(self, player):
        self.print_room_options()
        while True:
            try:
                room_number = int(input("In welchen Raum möchtest du gehen?: ")) - 1

                if room_number == -1:
                    break

                player.enter_room(self.rooms[room_number])
                print("Du bist jetzt im Raum {}!".format(self.rooms[room_number].room_name))
                player.get_room().room_prompt(player)
            except IndexError:
                print("Das ist kein valider Raum!")
            except ValueError:
                print("Das ist kein valider Raum!")


entry_room = Room("Eingang")
basement = Room("Keller")
attic = Room("Dach")

entry_room.add_room(basement)
entry_room.add_room(attic)

basement.add_room(entry_room)

attic.add_room(entry_room)

print("Willkommen zu Rooms!")
name = input("Gib deinen Spielernamen ein: ")
player = Player(name, entry_room)
entry_room.room_prompt(player)