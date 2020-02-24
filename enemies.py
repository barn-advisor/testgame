# TODO: Add an XP system!
# Version: FUNCTIONAL (to an extent)
from random import randint
import globals
enemies = { # XP based combat is impossible at the moment
	1: {
		"name": "bro you a noob",
		"desc": "you still lvl1 lomao",
		"hp": 1000,
		"dmg": 45
	}
}

def fight():
	use_reserve = False
	healing = ""
	data = globals.data

	# no guarantee these checks will work
	if data["bp"]["primary_wpn"] == "" and data["bp"]["reserve"] == "" or data["bp"]["primary_wpn"]["name"] == "" and data["bp"]["reserve"]["name"] == "":
		print("You have no weapons!")
		print(data["bp"])
		return
	if data["bp"]["primary_wpn"] == "":
		if data["bp"]["reserve"]["healing"]:
			print("You only have a healing weapon! (And you skipped the primary weapon! HOW)")
			return
		use_reserve = True
	elif data["bp"]["primary_wpn"] != "":
		if data["bp"]["primary_wpn"]["healing"] and data["bp"]["reserve"] == "":
			raise Exception("what")
	elif data["bp"]["reserve"] != "":
		if data["bp"]["reserve"]["healing"]:
			healing = data["bp"]["reserve"]


	enemy = enemies[randint(1, len(enemies))]

	# Turn-based combat
	while enemy["hp"] > 0 or data["hp"] > 0:
		data["hp"] -= enemy["dmg"]
		print("Enemy's turn: You received " + str(enemy["dmg"]) + " DMG")
		print("You now have: " + str(data["hp"]) + " HP")
		if data["hp"] <= 0:
			print("dead lol")
			raise
		if use_reserve:
			enemy["hp"] -= data["bp"]["reserve"]["dmg"]
			print("Your turn: You dealt " + data["bp"]["reserve"]["dmg"] + " DMG")
			print("Now he has: " + str(enemy["hp"]) + " HP")
		else:
			enemy["hp"] -= data["bp"]["primary_wpn"]["dmg"]
			print("Your turn: You dealt " + str(data["bp"]["primary_wpn"]["dmg"]) + " DMG")
			print("Now he has: " + str(enemy["hp"]) + " HP")
		if data["hp"] <= 25 and healing != "":
			data["hp"] += healing["dmg"]
			print("You gave yourself +" + str(healing["dmg"]) + " HP, now you have " + str(data["hp"]) + " HP")

		if enemy["hp"] <= 0:
			print("You won!")
			break

