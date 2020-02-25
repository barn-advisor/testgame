import gameshop
import saveload
import enemies
import globals
from os import path

def rshp():
	gameshop.runshop()

def save():
	saveload.Save()

def load():
	saveload.Load()

def fite():
	enemies.fight()

def quit():
	exit()

def up_level():
	if globals.data["exp"] >= 100:
		globals.data["lvl"] += (globals.data["exp"] // 100)
		globals.data["exp"] = 0
		print("Leveled up! Your level is now: " + str(globals.data["lvl"]))
	else:
		print("Not enough XP to level up! You need 100 XP")

opt = {
	1: rshp,
	2: fite,
	3: save,
	4: load,
	5: up_level,
	6: quit
}
# Initial player setup
if not path.exists("save"):
	print("It seems that you haven't set up your character yet.")
	globals.data["name"] = str(input("Enter your player's name: "))
	save()
else:
	load()
	print("Welcome back, " + str(globals.data["name"]))

while True:
	print("Options:")
	print("1. Go to shop")
	print("2. Fight!")
	print("3. Save game")
	print("4. Load game")
	print("5. Level up! (You have " + str(globals.data["exp"]) + " XP)")
	print("6. Quit (don't forget to save!)")
	option = int(input("Your choice: "))
	if option <= len(opt) and option > 0:
		opt[option]()
	else:
		print("Out of range.")
