import gameshop
import savingmdl as sv
import enemies
data = {
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
shop = {
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
	gameshop.runshop(shop, data, False)

# this function is in the works
# def save():
# 	sv.Save(data, shop)

def fite():
	enemies.fight(data)

opt = {
	1: rshp,
	2: fite
}
while True:
	print("Options:")
	print("1. Run shop")
	print("2. Fight!")

	option = int(input("Your choice: "))
	opt[option]()
