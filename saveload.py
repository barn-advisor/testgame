#savingmdl - saving module for testgame
#converts two dicts, data and shop (both used by testgame), into a json file
import json
import globals
import os
def Save():
	if not os.path.exists("save"):
		os.makedirs("save")

	with open("./save/data.json", "w+") as sav:
		json.dump(globals.data, sav)
	with open("./save/shop.json", "w+") as sav:
		json.dump(globals.shop, sav)
	print("Saved!")

def Load():
	with open("./save/data.json", 'r') as f:
		globals.data = json.load(f)
	with open("./save/shop.json", 'r') as f:
		globals.shop = json.load(f)
	print("Loaded!")
#	print(globals.data)
