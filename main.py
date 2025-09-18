from room import Room
from character import Character
from character import Enemy
from item import Item
from info import Info

inventory = [] #should add thing to inventory
live = False
rat_quest = False
rat_killed = False
entity_killed = False
intro = True
win = False

game = Info("Sound and Silence")
game.welcome()
Info.info()
start = input(">> ")
print("You wake up on the floor with a pounding headache and no memory of how you got here.")
print("What you do know is that you don't want to be here.")
print("Find a way out.")
intro = False
live = True

kitchen = Room("Kitchen") #the room is now called 'kitchen'
dining_room = Room("Dining Room")
ballroom = Room("Ballroom")
hallway = Room("Hallway")
bedroom = Room("Bedroom")
stairwell = Room("Stairwell")
storage = Room("Storage Room")
base_stairs = Room("Basement Stairwell")
base_hall = Room("Basement Hallway")
base_hall2 = Room("Basement Hallway")
final_room = Room("???")

kitchen.set_desc("A long abandoned room that smells of rot. The light switch doesn't work.")
dining_room.set_desc("A long table stands in the center of the room. Opulent decor lines the walls.")
ballroom.set_desc("A large room with a polished wooden floor. a piano stands in the corner, collecting dust.")
hallway.set_desc("A short hallway with a painting of an important-looking man on the wall. He's almost certainly dead.")
bedroom.set_desc("A very comfortable-looking bed lies in the corner of the room, covered in a thin layer of dust.")
stairwell.set_desc("The stairs lead down into a basement. At least you think so. You can't see the bottom.")
storage.set_desc("A room lined wall to wall with shelves. Unfortunately, most of the contents are junk.")
base_stairs.set_desc("It's too dark to see where you're going...")
base_hall.set_desc("A dark hallway with no decorations.")
base_hall2.set_desc("A dark hallway with no decorations.")
final_room.set_desc("There's a hatch on the ceiling. Somehow, you can tell it leads out of here.")

kitchen.link_room(dining_room, "south")
dining_room.link_room(kitchen, "north")
dining_room.link_room(ballroom, "west")
ballroom.link_room(dining_room, "east")
ballroom.link_room(hallway, "west")
hallway.link_room(ballroom,'east')
hallway.link_room(bedroom, "north")
hallway.link_room(stairwell, "west")
hallway.link_room(storage, "south")
stairwell.link_room(hallway, "east")
stairwell.link_room(base_stairs, "west")
base_stairs.link_room(stairwell, "east") #also goes to base_hall by west, but that has to be unlocked w/ lantern
storage.link_room(hallway, "north")
bedroom.link_room(hallway, "south")

base_hall.link_room(base_hall2, "west")
base_hall2.link_room(base_hall, "east")
base_hall2.link_room(final_room, "west")
final_room.link_room(base_hall2, "east")

ballroom.lock()
storage.lock()

current_room = kitchen

dave = Enemy("Zombie", 'A rotting corpse on shaky legs. It wears the scraps of what may once have been noble clothing.' )
dave.set_conversation("It makes a vague gurgling noise.")
dave.set_weakness("knife")

rat = Character("Rat", "A suspiciously large rat. A glimmer of intellingence sparkles in its eyes.")
rat.set_conversation("'Ever since the people disappeared, I've been left hungry. If you can find me something to eat, I'll make it worth your while.'")

entity = Character("???", "Something vaguely person-shaped, hunched over in the corner of the room, and bound to the wall by an iron chain. It has no discernable characteristics.")
entity.set_conversation("'Light...'")

knife = Item('knife', "A common kitchen knife. It's still sharp.")
key = Item('key',"A steel key.")
lantern = Item('lantern', 'A brass lantern. It still has some fuel in it.')
hatch_key = Item('hatch key', "A brass key.")
paperclip = Item("paperclip" , 'A common office supply, occasionally used as a lockpick.')

dining_room.set_char(dave)
dining_room.set_item(key)
key.hide()

bedroom.set_char(rat)

kitchen.set_item(knife)
knife.show()

storage.set_item(lantern)
lantern.show()

bedroom.set_item(paperclip)
paperclip.hide()

final_room.set_char(entity)
final_room.set_item(hatch_key)
hatch_key.hide()

while live == True:
    "eternity"
    print(" ")
    current_room.describe()

    inhabitant = current_room.get_char()
    if inhabitant:
        inhabitant.describe()

    item = current_room.get_item()
    if item and item.visible == True:
        print(f"There is a {current_room.item.name} here.")

    command = input(">> ")

    if current_room == final_room:
        base_hall2.lock()

    if command in ("north", 'south', 'east', 'west'):
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant:
            inhabitant.talk()
            if current_room == bedroom:
                rat_quest = True
                kitchen.set_desc("A long abandoned room that smells of rot. One of the cupboards is ajar.")

        else:
            print("But no-one was there.")

    elif command == 'fight':
        if inhabitant:
            print('What do you fight with?')
            combat_item = input('>> ')
            inhabitant.fight(combat_item) 
            if combat_item in inventory:
                if True:
                 print(f"You fend off {current_room.char.name} with the {combat_item}.")
                 current_room.set_char(None)
                 current_room.item.visible = True
                elif False:
                   print(f"{current_room.char.name} was unaffected.")
                   print("You were slain.")
                   live = False                
                else:
                    print("But no-one was there.")
            elif combat_item not in inventory:
                print("But you don't have that.")
                print("You were slain.")
                live = False 

    
    elif command == "take":
        if current_room.item.visible == True:
            inventory.append(current_room.item.name) 
            current_room.item.describe()
            current_room.item.hide()
        else:
            print("But there was nothing to take.")

    elif command == "inventory":
        print(f"INVENTORY: /n {inventory}")    

    elif command == "key" and "key" in inventory:
        if current_room == dining_room:
            print("You twist the key in the doorknob. It comes unlocked with a faint 'click'.")
            ballroom.unlock()
        elif current_room == hallway or current_room == final_room:
            print("Try as you might, the key doesn't twist. Seems like it takes a different key.")

    elif command == "paperclip" and "paperclip" in inventory and current_room == hallway:
        print("You jiggle the paperclip around in the lock until it comes open with a satisfying 'click'.")
        storage.unlock()

    elif command == "check" and rat_quest == True and current_room == kitchen or command == "cupboard" and rat_quest == True and current_room == kitchen:
        print("You reach into the cupboard and pull out a bag of dried cranberries.")
        inventory.append('cranberries')

    elif command == "cranberries" and current_room == bedroom and "cranberries" in inventory:
        print("you take a handful of berries out of the bag and put them on the floor. The rat looks up at you. 'Here's your payment.' it says, before pushing a paperclip in your direction and scurrying away.")
        print("...")
        print("You feel scammed.")
        rat_quest = False
        bedroom.set_char(None)
        paperclip.show()
        inventory.remove('cranberries')

    elif command == "lantern" and "lantern" in inventory:
        if current_room == base_stairs:
            print("You turn on the lantern, and now can see the room around you.")
            base_stairs.set_desc("The bottom of the stairwell. There's a couple of fake flowers here.")
            base_stairs.link_room(base_hall, "west")
            base_hall.link_room(base_stairs, "east")

        elif current_room == final_room:
            print("You give the light to the creature, who pulls it towards itself slowly.")
            print("Now that it holds the light, you can make out something like a face. Something about it seems familiar.")
            print("It lets out a strange noise, almost like a woman saying 'Thank you', then fades away.")

            inventory.remove("lantern")
            current_room.set_char(None)
            hatch_key.show()

    elif command == "knife" and 'knife' in inventory:
        if current_room == bedroom:
            print("Without warning, you shove the knife into the rat's head. It squeals, and promptly collapses, dead.")

            current_room.set_char(None)
            paperclip.show()
            rat_quest = False
            rat_killed = True

        elif current_room == final_room:
            print("You stab the creature once, twice, three times.")
            print("It collapses onto the floor, and melts into a puddle of colourless liquid.")
            print("For some reason, you feel like something has been lost.")

            current_room.set_char(None)
            hatch_key.show()
            entity_killed = True

    elif command == "hatch key" and 'hatch key' in inventory:
        print("You twist the key in the lock, and it clicks open.")
        print("beyond the hatch is a ladder, which you climb up for what feels like an hour." )
        print("As you'd hoped, you eventually emerge into open air. You breathe in as you step out, free.")
        if rat_killed == True and entity_killed == True:
            print("...")
            print("...")
            print("You should wash the blood off your hands.")
        live = False
        win = True
            
    else:
        print("But nothing happened.")
   
if live == False and intro == False:
    print("Thank you for playing,")
    if win == True:
        print("and congratulations on winning!")
    print('you may now close the program.')