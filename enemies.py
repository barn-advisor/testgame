# TODO: Add an XP system!
from random import randint
import globals

def fight():
	use_reserve = False
	healing = ""
	data = globals.data
	enemies = globals.enemies
	# no guarantee these checks will work
	if data["bp"]["primary_wpn"] == "" and data["bp"]["reserve"] == "":
		print("You have no weapons!")
		return
	elif data["bp"]["primary_wpn"] != "":
		if data["bp"]["primary_wpn"]["healing"] and data["bp"]["reserve"] == "":
			print("You only have a healing item!")
			return
		elif data["bp"]["primary_wpn"]["healing"]:
			healing = data["bp"]["primary_wpn"]
		elif data["bp"]["reserve"]["healing"]:
			healing = data["bp"]["reserve"]
	enemy_level_index = 0
	if data["lvl"] <= len(enemies):
		enemy_level_index = randint(1, data["lvl"])
	else:
		enemy_level_index = randint(1, len(enemies))

	enemy = enemies[enemy_level_index][randint(1, len(enemies[enemy_level_index]))]
	print("Enemy: " + enemy["name"])
	print("Enemy description: " + enemy["desc"])
	print("HP | DMG | XP: \n" + str(enemy["hp"]) + " | " + str(enemy["dmg"]) + " | " + str(enemy["xp"]))
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
			data["exp"] += enemy["xp"]
			break
	del enemy
	del enemies
	globals.enemies = globals.resetenemies()
	return
