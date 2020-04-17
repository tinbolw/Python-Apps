import random

equipment_cost = 0
equipment_available = False
want_grenades = False
Terrorist = False
Counter_Terrorist = False
weapon_price = 0
teamchecker = 0
Casual = False
kevlar = 0
helmet = 0
defuse_kit = 0
if_casual = 0
team = input("What team are you on? ")
while teamchecker == 0:
    if team == "Counter Terrorist" or team == "CT":
        Counter_Terrorist = True
        teamchecker += 1
    elif team == "Terrorists" or team == "T" or team == "Terrorist":
        Terrorist = True
        teamchecker += 1
    else:
        print("Not a valid team")
        teamchecker += 2


primary_CT = ['Nova', 'XM1014', 'Negev', 'MAG-7', 'MP7', 'MP9', 'UMP-45', 'P90', 'PP-Bizon', 'SSG08', 'AWP', 'FAMAS', 'M4A4', 'M4A1-S', 'SSG08', 'AUG', 'AWP', 'SCAR-20']
primary_T = ['Nova', 'XM1014', 'Sawed-Off', 'M249', 'Negev', 'MAC-10', 'UMP-45', 'P90', 'PP-Bizon', 'GalilAR', 'AK-47', 'SSG08', 'SG553', 'AWP', 'G3SG1',]
secondary_CT = ['DualBerettas', 'P250', 'Tec-9', 'DesertEagle', 'USP-S', 'P2000', 'DualBerettas', 'Five-Seven', 'CZ75-Auto']
secondary_T = ['Glock-18', 'DualBerettas', 'P250', 'Tec-9', 'DesertEagle', 'DualBerettas', 'Five-Seven', 'CZ75-Auto']
grenades_CT = ['IncendiaryGrenade', 'DecoyGrenade', 'Flashbang', 'HighExplosiveGrenade', 'SmokeGrenade', 'Zeusx27']
grenades_T = ['Molotov', 'IncendiaryGrenade', 'DecoyGrenade', 'Flashbang', 'HighExplosiveGrenade', 'SmokeGrenade', 'Zeusx27']

primary_ct_price = {
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
	
primary_t_price = {
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

secondary_ct_price = {
'DualBerettas': 400,
'P250': 300,
'DesertEagle': 700,
'USP-S': 200,
'P2000': 200,
'Five-Seven': 500,
'CZ75-Auto': 500,
'R8 Revolver': 600,
}

secondary_t_price = {
'DualBerettas': 400,
'P250': 300,
'DesertEagle': 700,
'Glock': 200,
'Five-Seven': 500,
'Tec-9': 500,
'R8 Revolver': 600,

}

if teamchecker == 1:
    if_casual = input("Are you playing casual? (Y/N) ")

if if_casual == "Y":
    Casual = True
elif if_casual =="N":
    Casual = False
else:
	print("Invalid answer")
	
if not(Casual):
	grenades_CT.append("Flashbang")
	grenades_T.append("Flashbang")
	

if teamchecker == 1:
    wealth = float(input("How much weapon_price do you have? "))

if wealth >= 2700:
	equipment_available = True

if teamchecker == 1 and equipment_available and not(Casual):
    kevlar = input("Do you want to buy kevlar? (Y/N) ")

if teamchecker == 1 and equipment_available and not(Casual):
    helmet = input("Do you want to buy a helmet? (Y/N) ")

if equipment_available and helmet == "Y" and not(Casual):
    equipment_cost += 350
else:
	dfgdfgdfgdfg = 1

if equipment_available and kevlar == "Y" and not(Casual):
    equipment_cost += 650
else:
	kfgihdfg = 1

if Counter_Terrorist and equipment_available and not(Casual):
    defuse_kit = input("Do you want to buy a defuse kit? (Y/N) ")

if equipment_available and defuse_kit == "Y":
    equipment_cost += 200

grenades = ""

if teamchecker == 1 and equipment_available:
    grenades = input("Do you want to buy grenades? (Y/N) ")

if equipment_available and grenades == "Y":
	want_grenades = True

	
total_price = 0
weapon_price = 0

def generate_primary(weapon, weapon_price):

def generate_secondary(weapon, weapon_price):

def random_grenades():
	random_grenade_number = random.randint(0, 5)
	first_nade = str(grenades_CT[random_grenade_number])
	print(first_nade)
	grenades_CT.remove(first_nade)
	second_nade_index = random.randint(0, 4)
	second_nade = str(grenades_CT[second_nade_index])
	print(second_nade)
	grenades_CT.remove(second_nade)
	third_nade_index = random.randint(0, 3)
	third_nade = str(grenades_CT[third_nade_index])
	print(third_nade)
	grenades_CT.remove(third_nade)
	if not (Casual):
		fourth_nade_index = random.randint(0, 2)
		fourth_nade = str(grenades_CT[fourth_nade_index])
		print(fourth_nade)
		grenades_CT.remove(fourth_nade)


	
def randomize_poor():
	print("WIP")
	
def randomize_rest():
	print("WIP")

if weapon_price == 3700

if weapon_price == 1050:
	

if weapon_price >= 7500:
	print("Here is your loadout ")
	primary_weapon_number = (random.randint(0, 17))
	random_primary_weapon = str(primary_CT[primary_weapon_number])
	print(random_primary_weapon)
	secondary_weapon_number = (random.randint(0, 8))
	random_secondary_weapon = str(secondary_CT[secondary_weapon_number])
	print(random_secondary_weapon)
elif weapon_price <= 1:
	print("wip")
else:
	kigwuhrguiwhg = 1

if weapon_price >= 7500 and want_grenades:
	random_grenade_number = random.randint(0, 5)
	first_nade = str(grenades_CT[random_grenade_number])
	print(first_nade)
	grenades_CT.remove(first_nade)
	second_nade_index = random.randint(0, 4)
	second_nade = str(grenades_CT[second_nade_index])
	print(second_nade)
	grenades_CT.remove(second_nade)
	third_nade_index = random.randint(0, 3)
	third_nade = str(grenades_CT[third_nade_index])
	print(third_nade)
	grenades_CT.remove(third_nade)
	if not(Casual):
		fourth_nade_index = random.randint(0,2)
		fourth_nade = str(grenades_CT[fourth_nade_index])
		print(fourth_nade)
		grenades_CT.remove(fourth_nade)
	
	

if teamchecker == 2:
    quit












