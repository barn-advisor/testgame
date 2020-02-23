# TODO: Rework the code so it isn't spaghetti!
import globals
def runshop():
	data = globals.data
	shop = globals.shop
	print("Welcome to the store!")
	print("Items: ")
	for x in shop["weapons"]:
		print("Item n. " + str(x) + ": " + shop["weapons"][x]["name"])
		print("Desc: " + shop["weapons"][x]["desc"])
		print("Damage: " + str(shop["weapons"][x]["dmg"]))
		print("\n") # Crude, but works
	slct = int(input("Buy which item?: "))
	try:
		if slct <= len(shop["weapons"]) and slct >= 1:
			print("Item selected: " + shop["weapons"][slct]["name"])
			print("Price: " + str(shop["weapons"][slct]["price"]))
			print("Is Available: " + str(shop["weapons"][slct]["available"]))

			conf = input("Are you sure? (y/n) ")
			if conf.lower() == "y":
				print("Bought \"" + shop["weapons"][slct]["name"] + "\" for " + str(shop["weapons"][slct]["price"]))
				data["wallet"] -= shop["weapons"][slct]["price"]
				if data["bp"]["primary_wpn"] == "":
					data["bp"]["primary_wpn"] = shop["weapons"][slct]
					shop["weapons"][slct]["available"] = False
				elif data["bp"]["reserve"] == "":
					data["bp"]["reserve"] = shop["weapons"][slct]
					shop["weapons"][slct]["available"] = False
				else:
					raise Exception("Your backpack's weapon slots are full!!!")
			else:
				print("Cancelling.")
		else:
			print("Out of range.")
	except (TypeError, ValueError) as err:
		print("ERR: Type/Value Error. Did you type a value incorrectly? Halting.")
#		if throwing:
#			raise
	except:
		print("ERR: Something happened")
#		if throwing:
#			raise

