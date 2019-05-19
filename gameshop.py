# hopefully the data is global
def runshop(shop, data, throwing):
	print("Welcome to shit store")
	print("weapons:")
	for list in shop["weapons"]:
        	print("item number " + str(list))
	        # this *will* work because the values "name" and others shouldnt change
        	print("name: " + shop["weapons"][list]["name"])
	        print("desc: " + shop["weapons"][list]["desc"])
        	print("dmg: " + str(shop["weapons"][list]["dmg"]))
	slct = int(input("Buy which item?: "))
	try: #here's the possible failure spot
		#thats why there's a try-except here
		if 1 <= slct <= len(shop["weapons"]):
			print("Item selected: " + shop["weapons"][slct]["name"])
			print("Price: " + str(shop["weapons"][slct]["price"]))
			print("Is Available: " + str(shop["weapons"][slct]["available"]))
			conf = input("Are you sure? (y/n) ")
			if conf == "y":
				print("Bought \"" + shop["weapons"][slct]["name"] + "\" for " + str(shop["weapons"][slct]["price"]))
				data["wallet"] -= shop["weapons"][slct]["price"]
				if data["bp"]["primary_wpn"] == "":
					data["bp"]["primary_wpn"] = shop["weapons"][slct]["name"]
					shop["weapons"][slct]["available"] = False
				elif data["bp"]["reserve"] == "":
					data["bp"]["reserve"] = shop["weapons"][slct]["name"]
					shop["weapons"][slct]["available"] = False
				else:
					print("Your backpack's weapon slots are full!!!")
			else:
				print("Cancelling.")
		else:
			print("Out of range.")
	except (TypeError, ValueError) as err:
		print("ERR: Type/Value Error. Did you type a value incorrectly? Halting.")
		if throwing:
			raise
	except:
		print("ERR: Something happened")
		if throwing:
			raise
	finally:
		print("done")

