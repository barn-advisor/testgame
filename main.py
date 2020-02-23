import gameshop
import saveload
import enemies
import globals
from os import path

def rshp():
	gameshop.runshop()

# this function and the load function is highly experimental
def save():
	saveload.Save()

def load():
	saveload.Load()

def fite():
	enemies.fight()

def quit():
	exit()

opt = {
	1: rshp,
	2: fite,
	3: save,
	4: load,
	5: quit
}
# Initial player setup
if not path.exists("save"):
	print("It seems that you haven't set up your character yet.")
	globals.data["name"] = str(input("Enter your player's name: "))
	save()
else:
	load()
	print("Welcome back, " + str(globals.data["name"]))

print(len(opt))

while True:
	print("Options:")
	print("1. Run shop")
	print("2. Fight!")
	print("3. Save game")
	print("4. Load game")
	print("5. Quit (don't forget to save!)")
	option = int(input("Your choice: "))
	if option <= len(opt) and option > 0:
		opt[option]()
	else:
		print("Out of range.")
