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

enemies = { # Level/XP based combat is being experimented with
	1: {
		1: {
			"name": "bro you a noob",
			"desc": "you still lvl1 lomao",
			"hp": 1000,
			"dmg": 15,
			"xp": 20
		},
		2: {
			"name": "cock",
			"desc": "cock",
			"hp": 2000,
			"dmg": 20,
			"xp": 40
		}
	},
	2: {
		1: {
			"name": "death",
			"desc": "you will die",
			"hp": 9999,
			"dmg": 2147483647,
			"xp": 0
		}
	}
}

# eat my shit python
enemies_template = { # template
	1: {
		1: {
			"name": "bro you a noob",
			"desc": "you still lvl1 lomao",
			"hp": 1000,
			"dmg": 15,
			"xp": 20
		},
		2: {
			"name": "cock",
			"desc": "cock",
			"hp": 2000,
			"dmg": 20,
			"xp": 40
		}
	},
	2: {
		1: {
			"name": "death",
			"desc": "you will die",
			"hp": 9999,
			"dmg": 2147483647,
			"xp": 0
		}
	}
}

DealAsString = False
