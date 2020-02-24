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
			"healing": False,
			"dmg": 400,
			"price": 5,
			"available": True
		},
		2: {
			"name": "bitch gun",
			"desc": "heal test",
			"healing": True, # turns dmg into heal
			"dmg": 50,
			"price": 1,
			"available": True
		}
	}
}

enemies = { # XP based combat is impossible at the moment
	1: {
		"name": "bro you a noob",
		"desc": "you still lvl1 lomao",	
		"hp": 1000,
		"dmg": 45
	}
}

enemies_template = {
	1: {
		"name": "bro you a noob",
		"desc": "you still lvl1 lomao",
		"hp": 1000,
		"dmg": 45
	}
}

DealAsString = False
