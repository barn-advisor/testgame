import gameshop
import saveload
import enemies
import globals
# These dicts are meant as placeholders.

datab = {
	"name": "",
	"exp": 0,
	"hp": 100,
	"lvl": 1,
	"bp": {
		"slot1": "",
		"slot2": "",
		"slot3": "",
		"primary_wpn": "",
		"reserve": ""
	},
	"wallet": 6
}
shopb = {
	"weapons": {
		1: {
			"name": "eat my ass",
			"desc": "this is the fucking",
			"dmg": 400,
			"price": 5,
			"available": True
		}
	}
}

def rshp():
	gameshop.runshop()

# this function and the load function is highly experimental
def save():
	saveload.Save()

def load():
	saveload.Load()

def fite():
	enemies.fight()

opt = {
	1: rshp,
	2: fite,
	3: save,
	4: load
}
while True:
	print("Options:")
	print("1. Run shop")
	print("2. Fight!")
	print("3. Save game")
	print("4. Load game")
	option = int(input("Your choice: "))
	opt[option]()
