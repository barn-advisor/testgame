# TODO: Rework the code so it isn't spaghetti!
import globals
def runshop():
	data = globals.data
	shop = globals.shop
	unavs = 0
#	print(shop)
	print("Welcome to the store!")
	print("Items: ")
	for x in shop["weapons"]:
		if shop["weapons"][x]["available"]:
			print("Item n. " + str(x) + ": " + shop["weapons"][x]["name"])
			print("Desc: " + shop["weapons"][x]["desc"])
			if shop["weapons"][x]["healing"]:
				print("Healing: " + str(shop["weapons"][x]["dmg"]))
			else:
				print("Damage: " + str(shop["weapons"][x]["dmg"]))
			print("\n") # Crude, but works
		else:
			unavs += 1
	if unavs >= len(shop["weapons"]):
		print("All items are unavailable!")
		return
	slct = int(input("Buy which item?: "))
	try:
		if slct <= len(shop["weapons"]) and slct >= 1:
			if globals.DealAsString:
				slct = str(slct)

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
