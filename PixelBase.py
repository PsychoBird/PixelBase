from PIL import Image, ImageDraw
import json

typeDraw = input("Draw wall outline or full base (outline/full): ")

baseSkeleton = Image.new('RGB', (500, 500), color='#19633A')
base = ImageDraw.Draw(baseSkeleton)
base.rectangle([(30, 30), (470, 470)], fill='#90EE90')

with open('json.txt', 'r') as myfile:
        jsonload = myfile.read()
        jsonload = json.loads(jsonload)

def spaceLoad(id, x, y):
    info = {
        1000010: [1, "#207CBA"], # Wall
        1000001: [4, "#08345B"], # TownHall
        1000014: [3, "#28343D"], # Clan Castle
        1000008: [3, "#686C6F"], # Cannon
        1000009: [3, "#1A8C50"], # Archer Tower
        1000011: [3, "#D714EE"], # Wizard Tower
        1000012: [3, "#E9BF02"], # Air Defense
        1000013: [3, "#C38729"], # Mortar
        1000021: [3, "#9FA925"], # X-Bow
        1000027: [2, "#F41503"], # Inferno Tower
        1000028: [2, "#90362E"], # Air Sweeper
        1000031: [4, "#FFFFFF"], # Eagle Artillery
        1000032: [3, "#22ADC3"], # Bomb Tower
        1000022: [3, "#F24B1B"], # Barbarian King
        1000025: [3, "#AF58C3"], # Archer Queen
        1000030: [3, "#C9BAB6"], # Grand Warden
        1000015: [2, "#632D1F"], # Builder Hut
        1000002: [3, "#910046"], # Elixir Collector
        1000003: [3, "#FF007B"], # Elixir Storage
        1000004: [3, "#868F1D"], # Gold Collector
        1000005: [3, "#ECFF0B"], # Gold Storage
        1000023: [3, "#351919"], # Dark Elixir Collector
        1000024: [3, "#000000"], # Dark Elixir Storage
        1000000: [4, "#E1C47F"], # Army Camp
        1000006: [3, "#AA7800"], # Barracks
        1000007: [3, "#15D0C8"], # Laboratory
        1000020: [3, "#7F910B"], # Spell Factory
        1000026: [3, "#845F5E"], # Dark Barracks
        1000029: [3, "#4C110F"], # Dark Spell Factory
        1000059: [4, "#A50600"], # Siege Workshop
        1000067: [3, "#204CBE"], # Scattershot
        1000066: [3, "#7E91C2"], # Royal Champion
        1000064: [2, "#93503F"], # Master Builder
        1000019: [2, "#A9AD97"], # Hidden Tesla
    }
    addBuilding(info[id][0], x, y, info[id][1])


def addBuilding(space, x, y, bColor):
    base.rectangle([(x*10, y*10), (x+space)*10, (y+space)*10], fill=bColor)
    baseSkeleton.save("PixelBase" + typeDraw.capitalize() + ".png")

i=0
for data in jsonload:
    id = jsonload[i]["data"]
    x = jsonload[i]["x"]
    y = jsonload[i]["y"]
    i=i+1
    if typeDraw == "full":
        spaceLoad(id, x, y)
    if typeDraw == "outline" and id == 1000010:
        spaceLoad(id, x, y)

baseSkeleton.show()




