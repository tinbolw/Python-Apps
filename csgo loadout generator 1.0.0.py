Terrorist = False
CounterTerrorist = False
team = None
money = None

def getData():
	global team
	global money
	team = input("What team are you on?\n")
	money = input("How much money do you have?\n")
	print(team)
	if team == "T" or "t" or "Terrorist" or "terrorist":
		Terrorist = True
		print("terrorist")
	elif team == "CT" or "ct" or "Ct" or "cT" or "Counter Terrorist" or "counter terrorist" or "Counter-Terrorist" or "counter-terrorist":
		CounterTerrorist = True
		print("counterterrorist")
	else:
		print("Invalid Selection")
		getData()



primaryCTPrices = {
'Nova': 1200,
'XM1014': 2000,
'Negev': 2000,
'MAG-7': 1800,
'MP7': 1700,
'MP9': 1250,
'UMP-45': 1200,
'P90': 2350,
'PP-Bizon': 1400,
'SSG08': 1700,
'AWP': 4750,
'FAMAS': 2250,
'M4A4': 3100,
'M4A1-S': 3100,
'AUG': 3300,
'SCAR-20': 5000,

}
	
primaryTPrices = {
'Nova': 1200,
'XM1014': 2000,
'Negev': 2000,
'Sawed-Off': 1200,
'Mac-10': 1050,
'UMP-45': 1200,
'P90': 2350,
'PP-Bizon': 1400,
'SSG08': 1700,
'AWP': 4750,
'Galil': 2000,
'AK-47': 2700,
'SSG 553': 3000,
'G3SG1': 5000,

}

secondaryCTPrices = {
'DualBerettas': 400,
'P250': 300,
'DesertEagle': 700,
'USP-S': 200,
'P2000': 200,
'Five-Seven': 500,
'CZ75-Auto': 500,
'R8 Revolver': 600,
}

secondaryTPrices = {
'DualBerettas': 400,
'P250': 300,
'DesertEagle': 700,
'Glock': 200,
'Five-Seven': 500,
'Tec-9': 500,
'R8 Revolver': 600,

}

getData()