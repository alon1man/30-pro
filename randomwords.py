import random
def artrandomword():
    
    art_dict = {
    "Canvas": 1, "Paint": 2, "Brush": 3, "Sketch": 4, "Statue": 5,
    "Color": 6, "Pencil": 7, "Museum": 8, "Gallery": 9, "Artist": 10,
    "Mural": 11, "Easel": 12, "Pastel": 13, "Frame": 14, "Design": 15,
    "Shadow": 16, "Light": 17, "Value": 18, "Hue": 19, "Tone": 20,
    "Style": 21, "Modern": 22, "Abstract": 23, "Oil": 24, "Acrylic": 25,
    "Clay": 26, "Bronze": 27, "Stone": 28, "Wood": 29, "Ink": 30,
    "Paper": 31, "Charcoal": 32, "Etching": 33, "Glaze": 34, "Pottery": 35,
    "Form": 36, "Shape": 37, "Line": 38, "Texture": 39, "Space": 40,
    "Mosaic": 41, "Enamel": 42, "Crayon": 43, "Gouache": 44, "Varnish": 45,
    "Print": 46, "Stencil": 47, "Palette": 48, "Studio": 49, "Visual": 50
    }
    return random.choice(list(art_dict.keys()))
def scaryrandomword():
    global scary_dict
    scary_dict = {
        "Ghost": 1, "Shadow": 2, "Phantom": 3, "Specter": 4, "Haunt": 5,
        "Zombie": 6, "Vampire": 7, "Monster": 8, "Demon": 9, "Goblin": 10,
        "Ghoulish": 11, "Spooky": 12, "Creepy": 13, "Eerie": 14, "Chilling": 15,
        "Macabre": 16, "Morbid": 17, "Sinister": 18, "Ominous": 19, "Grim": 20,
        "Skeleton": 21, "Skull": 22, "Bones": 23, "Coffin": 24, "Grave": 25,
        "Cemetery": 26, "Crypt": 27, "Tomb": 28, "Vault": 29, "Mausoleum": 30,
        "Cobweb": 31, "Spider": 32, "Bat": 33, "Wolf": 34, "Crow": 35,
        "Scream": 36, "Shriek": 37, "Howl": 38, "Groan": 39, "Whisper": 40,
        "Nightmare": 41, "Terror": 42, "Horror": 43, "Panic": 44, "Dread": 45,
        "Curse": 46, "Witch": 47, "Wizard": 48, "Potion": 49, "Spell": 50
    }
    return random.choice(list(scary_dict.keys()))
def toysrandomword():
    global toy_dict
    global toy_lengths_matched
    toy_dict = {
    "Robot": 1, "Doll": 2, "Puzzle": 3, "Blocks": 4, "Train": 5,
    "Ball": 6, "Yoyo": 7, "Kite": 8, "Marble": 9, "Slime": 10,
    "Lego": 11, "Crayons": 12, "Truck": 13, "Car": 14, "Plane": 15,
    "Bear": 16, "Plush": 17, "Action": 18, "Figure": 19, "Trike": 20,
    "Slinky": 21, "Frisbee": 22, "Hoop": 23, "Cards": 24, "Dice": 25,
    "Chess": 26, "Clay": 27, "Whistle": 28, "Top": 29, "Balloon": 30,
    "Rattle": 31, "Bubbles": 32, "Drum": 33, "Rocket": 34, "Slide": 35,
    "Swing": 36, "Skates": 37, "Board": 38, "Game": 39, "Puppet": 40,
    "Mask": 41, "Cape": 42, "Sword": 43, "Shield": 44, "Wand": 45,
    "Soldier": 46, "Dino": 47, "GoKart": 48, "Scooter": 49, "Radio": 50
    }
    
    toy_lengths_matched = {
    "Trike": 1, "Bear": 2,  "Action": 3,   "Marble": 4,   "Plane": 5,
    "Yoyo": 6, "Kite": 7, "Ball": 8,  "Blocks": 9,  "Puppet": 10,
    "Drum": 11, "Cymbal": 12, "Train": 13, "Toy": 14, "Robot": 15,
    "Slime": 16, "Rocket": 17, "Puzzle": 18, "Crayon": 19, "Truck": 20,
    "Shield": 21, "Soldier": 22, "Dice": 23,"Flute": 24, "Hoop": 25,
  "Cards": 26, "Mask": 27, "Scooter": 28,"Sub": 29,"Frisbee": 30,
    "Slinky": 31,"Soldier": 32,"Xylo": 33,"GoKart": 34,"Sword": 35,
    "Radio": 36,"Skate": 37,"Blade": 38,"Dino": 39,"Glider": 40,
    "Game": 41,"Clay": 42,"Trunk": 43,"Helmet": 44,"YoYo": 45,
    "Bubbles": 46,"Plush": 47,"Skates": 48,"Whistle": 49,"Crown": 50
}
    return random.choice(list(toy_dict.keys()))


def encryptionforone_time_pad():
    encryption_dict = {
        "one_time_pad": 1,
        
    }
    return random.choice(list(encryption_dict.keys()))

def encryptionstring():
    encryption_dict = {
        "vigenere": 1,
        
    }
    return random.choice(list(encryption_dict.keys()))
def encryptionnum():
    encryption_dict = {
        "azby": 1,
        "caesar": 2,
        
    }
    return random.choice(list(encryption_dict.keys()))
def keyrandom():
    return random.randint(0, 26)
def stringkeyrandom():
    return random.choice(list(scary_dict.keys()))
def keyforone_time_pad(toy_name):
    number = toy_dict.get(toy_name)
    if number is None:
        number = len(toy_name)
    candidates = [toy for toy, value in toy_lengths_matched.items() if value == number]
    if candidates:
        return random.choice(candidates)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return "".join(random.choice(alphabet) for _ in range(number))
    
    
   