class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.desc = None
        self.linked_rooms = {} #*there's no one here... yet.
        self.char = None
        self.locked = False
        self.item = None

    def set_desc(self,room_desc):
        self.desc = room_desc

    def get_desc(self):
        return self.desc
    
    def set_char(self, room_char):
        self.char = room_char

    def set_item(self, room_item):
        self.item = room_item
    
    def get_char(self):
        return self.char
    
    def get_item(self): #test later
        if self.item is not None:
            return self.item
        else:
            pass

    def get_details(self):
        self.get_char
        self.get_desc

    def link_room(self, room_to_link, direction):
        "add the room_to_link into the dictionary under the key direction"
        self.linked_rooms[direction] = room_to_link

    def move(self,direction):
        "find the room in the direction, go there."
        if direction in self.linked_rooms:
            if self.linked_rooms[direction].locked:
                print('But the door was locked.')
                return self
            else:
                return self.linked_rooms[direction]
        else:
            print("But there was no room in that direction.")
            return self

    def describe(self):
        print(self.name)
        print("..........")
        print(self.desc)
        for direction in self.linked_rooms:
            print(f"The {self.linked_rooms[direction].name} is {direction}.")
    
    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False
        



 


if __name__ == "__main__":
    #this code will only run if room.py is run
    #good for testing
    kitchen = Room("Kitchen") #the room is now called 'kitchen'
    dining_room = Room("Dining Room")
    ballroom = Room("Ballroom")

    kitchen.set_desc("A dark, dank room that smells of rot.")

    print(kitchen.name)
    print("...............")
    print(kitchen.get_desc())

    kitchen.link_room(dining_room, "south")
    print(kitchen.linked_rooms)
