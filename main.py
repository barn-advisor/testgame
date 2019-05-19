# "game" that doesn't work
# it's just me fuckin around with dictionaries
# this is the main module, here is where all the data is initialized and where the "game" actually begins
import gameshop
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
#yeha this probably isnt working
shop = {
	"weapons": {
		1: {
			"name": "eat my ass",
			"desc": "this is the fucking",
			"dmg": 1000,
			"price": 5,
			"available": True
		}
	}
}

gameshop.runshop(shop, data, False) #believe it or not THIS ACTUALLY FUCKING WORKS HAHAHAHAHA
				#IT ACTUALLY FUCKING EDITS THE DATA DICTIONARY :DDD
				#YEE HAW BITCH


