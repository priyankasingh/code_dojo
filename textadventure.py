class Room:
    def __init__(self, accessibility, description):
        self.accessibility = accessibility
        self.description = description

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class TextAdventure:
    def __init__(self):
        self.map_size = 5;
        self.x = 0
        self.y = 0
        self.money = 0
        
        self.inventory = None
        self.limit = 1
        
        self.rooms = [[Room(True, "the wilderness") for x in range(self.map_size)] for x in range(self.map_size)]
        
        self.rooms[0][0] = Room(True, "The spawn point, a mysterious magic permeates the air")
        self.rooms[0][1] = Room(True, "Slimy rat hole, filled with skulls and bones of rhodents")
        self.rooms[0][2] = Room(True, "Praise the lord of evil, a cat house")
        self.rooms[0][3] = Room(True, "Hear the beautiful music of Lady Iris from her golden harp")
        self.rooms[0][4] = Room(False, "")
        self.rooms[1][0] = Room(True, "Existensial room that tells you how empty your soul is.")
        self.rooms[1][1] = Room(False, "")
        self.rooms[1][2] = Room(False, "")
        self.rooms[1][3] = Room(True, "A dark empty room, light a match to see around")
        self.rooms[1][4] = Room(True, "A brave soldier died here, so feel free to grab his stuff")
        self.rooms[2][0] = Room(False, "")
        self.rooms[2][1] = Room(False, "")
        self.rooms[2][2] = Room(True, "The rainbow room without a rainbow with a trap door. Do you have a key?")
        self.rooms[2][3] = Room(True, "Boredom lounge, nothing ever happens here")
        self.rooms[2][4] = Room(True, "Rest room, you actually rest here and have a breather")
        self.rooms[3][0] = Room(True, "A ginger bread house")
        self.rooms[3][1] = Room(True, "A Library")
        self.rooms[3][2] = Room(True, "A dungeon where a dragon plays a piano")
        self.rooms[3][3] = Room(False, "")
        self.rooms[3][4] = Room(False, "")
        self.rooms[4][0] = Room(True, "Kitchen")
        self.rooms[4][1] = Room(False, "")
        self.rooms[4][2] = Room(True, "An abandoned movie theatre")
        self.rooms[4][3] = Room(True,"Cemetary")
        self.rooms[4][4] = Room(True, "Antique shop")
        
        
        
        
        self.item = [[None for x in range(self.map_size)] for x in range(self.map_size)]
        self.item[0][0] = Item("Key", 100)
        self.item[0][1] = Item("Mouse Trap", -50)
        self.item[0][2] = Item("Cat", -100)
        self.item[0][3] = Item("Harp", 150)
        self.item[1][4] = Item("Helmet", 50)
        self.item[2][2] = Item("Piano", -10)
        self.item[4][0] = Item("Matches", 50)
        self.item[4][4] = Item("Net", 10)
        
    def run(self):
        print self.rooms[self.x][self.y].description
        while(True):
            command = raw_input("What is your command?\n")
            
            if self.inventory != None and self.inventory.name == "Key" and self.x == 2 and self.y == 2:
                print "You have brought the key to the drawer, you open it. Inside is a myserious orb. It explodes. The end."
                exit()
            else:
                self.interpret(command)

    def interpret(self, command):
        command = command.lower().strip()
        
        if command == "go north":
            new_position = self.y + 1
            if (new_position>=self.map_size):
                new_position %= self.map_size

            if self.rooms[self.x][new_position].accessibility:
                self.y = new_position
                print "You move north into " + self.rooms[self.x][self.y].description
            else:
                print "You find yourself obstructed, there is something in the way"
        elif command == "go south":
            new_position = self.y - 1
            if (new_position<0):
                new_position += self.map_size
                
            if self.rooms[self.x][new_position].accessibility:
                self.y = new_position
                print "You move south into " + self.rooms[self.x][self.y].description
            else:
                print "You find yourself obstructed, there is something in the way"
        elif command == "go east":
            new_position = self.x + 1
            if (new_position>=self.map_size):
                new_position %= self.map_size
                
            if self.rooms[new_position][self.y].accessibility:
                self.x = new_position
                print "You move east into " + self.rooms[self.x][self.y].description
            else:
                print "You find yourself obstructed, there is something in the way"
        elif command == "go west":
            new_position = self.x - 1
            if (new_position<0):
                new_position += self.map_size
                
            if self.rooms[new_position][self.y].accessibility:
                self.x = new_position
                print "You move west into " + self.rooms[self.x][self.y].description
            else:
                print "You find yourself obstructed, there is something in the way"
        elif command == "pickup":
            if self.item[self.x][self.y] != None:
                if self.inventory == None :
                    self.inventory = self.item[self.x][self.y]
                    self.item[self.x][self.y] = None
                    print "You pick up " + self.inventory.name
                else:
                    print "Your hands are full, you cannot pick the item up"
            else:
                print "You find nothing, tumbleweed wonders by"
        elif command == "leave":
            print "Goodbye .. don't go!"  
            exit()
        elif command == "look":
            if self.item[self.x][self.y] != None:
                print "You see " + self.item[self.x][self.y].name
            else:
                print "Nothing is around"
        elif command == "dance":
            print "You jump up and down but quickly you are out of breath. Looking around no one saw you humilate yourself"
        elif command == "list":
            if self.inventory != None:
                print "You have a " + self.inventory[0].name
            else:
                print "You aren't carrying anything!"
        elif command == "drop":
            if self.inventory != None:
                if self.item[self.x][self.y] == None:
                    self.item[self.x][self.y] = self.inventory
                    self.inventory = None
                    print "You drop the item onto the floor"
                else :
                    print "You can't drop the item in this room, it's full!"
            else:
                print "You aren't carrying anything!"
        elif command == "where":
            print "You are in Room " + str(self.x) + "" + str(self.y)
        else :
            print "Can't do "+ command + ". You can go north, go south, go east, go west, pickup, and leave (but don't!)."
        

adventure = TextAdventure()
adventure.run()