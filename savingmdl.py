#savingmdl - saving module for testgame
#converts two dicts, data and shop (both used by testgame), into a json file
import json
def Save(data, shop):
	with open("save/data.json", "w") as sav:
		json.dump(data, sav)
	with open("save/shop.json", "w") as sav:
		json.dump(shop, sav)


