# TODO: Add an XP system!
# Version: FUNCTIONAL (to an extent)
from random import randint
import globals
enemies = { # XP based combat is impossible at the moment
	1: {
		"name": "bro you a noob",
		"desc": "you still lvl1 lomao",
		"hp": 1000,
		"dmg": 50
	}
}

def fight():
	use_reserve = False
	data = globals.data
	if data["bp"]["primary_wpn"] == "" and data["bp"]["reserve"] == "" or data["bp"]["primary_wpn"]["name"] == "" and data["bp"]["reserve"]["name"] == "":
		print("You have no weapons!")
		print(data["bp"])
		return
	elif data["bp"]["primary_wpn"] == "":
		use_reserve = True

	enemy = enemies[randint(1, len(enemies))]
	# Turn-based combat
	while enemy["hp"] > 0 or data["hp"] > 0:
		data["hp"] -= enemy["dmg"]
		print("Enemy's turn: You received " + str(enemy["dmg"]) + " DMG")
		print("You now have: " + str(data["hp"]) + " HP")
		if use_reserve:
			enemy["hp"] -= data["bp"]["reserve"]["dmg"]
			print("Your turn: You dealt " + data["bp"]["reserve"]["dmg"] + " DMG")
			print("Now he has: " + str(enemy["hp"]) + " HP")
		else:
			enemy["hp"] -= data["bp"]["primary_wpn"]["dmg"]
			print("Your turn: You dealt " + str(data["bp"]["primary_wpn"]["dmg"]) + " DMG")
			print("Now he has: " + str(enemy["hp"]) + " HP")
		if enemy["hp"] <= 0:
			print("You won!")
			break
		elif data["hp"] <= 0:
			print("fuck")
			raise

