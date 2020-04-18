import random
import re

loadout_generated = False
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

primary_CT = ['Nova', 'XM1014', 'Negev', 'MAG-7', 'MP7', 'MP9', 'UMP-45', 'P90', 'PP-Bizon', 'SSG08', 'AWP', 'FAMAS',
              'M4A4', 'M4A1-S', 'SSG08', 'AUG', 'AWP', 'SCAR-20']
primary_T = ['Nova', 'XM1014', 'Sawed-Off', 'M249', 'Negev', 'MAC-10', 'UMP-45', 'P90', 'PP-Bizon', 'GalilAR', 'AK-47',
             'SSG08', 'SG553', 'AWP', 'G3SG1', ]
secondary_CT = ['DualBerettas', 'P250', 'Tec-9', 'DesertEagle', 'USP-S', 'P2000', 'DualBerettas', 'Five-Seven',
                'CZ75-Auto']
secondary_T = ['Glock-18', 'DualBerettas', 'P250', 'Tec-9', 'DesertEagle', 'DualBerettas', 'Five-Seven', 'CZ75-Auto']
grenades_CT = ['IncendiaryGrenade', 'DecoyGrenade', 'Flashbang', 'HighExplosiveGrenade', 'SmokeGrenade', 'Zeusx27']
grenades_T = ['Molotov', 'IncendiaryGrenade', 'DecoyGrenade', 'Flashbang', 'HighExplosiveGrenade', 'SmokeGrenade',
              'Zeusx27']

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
elif if_casual == "N":
    Casual = False
else:
    print("Invalid answer")

if not (Casual):
    grenades_CT.append("Flashbang")
    grenades_T.append("Flashbang")

if teamchecker == 1:
    wealth = float(input("How much money do you have? "))

if wealth >= 2700:
    equipment_available = True

if teamchecker == 1 and equipment_available and not (Casual):
    kevlar = input("Do you want to buy kevlar? (Y/N) ")

if teamchecker == 1 and equipment_available and not (Casual):
    helmet = input("Do you want to buy a helmet? (Y/N) ")

if equipment_available and helmet == "Y" and not (Casual):
    equipment_cost += 350
else:
    dfgdfgdfgdfg = 1

if equipment_available and kevlar == "Y" and not (Casual):
    equipment_cost += 650
else:
    kfgihdfg = 1

if Counter_Terrorist and equipment_available and not (Casual):
    defuse_kit = input("Do you want to buy a defuse kit? (Y/N) ")

if equipment_available and defuse_kit == "Y":
    equipment_cost += 200

grenades = ""

if teamchecker == 1 and equipment_available:
    grenades = input("Do you want to buy grenades? (Y/N) ")

if equipment_available and grenades == "Y":
    want_grenades = True

while not(loadout_generated):
    primary_ct_price = {
        'Nova': 1200,
        'XMOneZeroOneFour': 2000,
        'Negev': 2000,
        'MAG-Seven': 1800,
        'MPSeven': 1700,
        'MPnine': 1250,
        'UMP-FourtyFive': 1200,
        'PNinety': 2350,
        'PP-Bizon': 1400,
        'SSGOhEight': 1700,
        'AWP': 4750,
        'FAMAS': 2250,
        'M4A4': 3100,
        'M4A1-S': 3100,
        'AUG': 3300,
        'SCAR-Twenty': 5000,

    }
    primary_ct_price_inverted = {1200: 'UMP-FourtyFive', 2000: 'Negev', 1800: 'MAG-Seven', 1700: 'SSGOhEight',
                                 1250: 'MPnine', 2350: 'PNinety', 1400: 'PP-Bizon', 4750: 'AWP', 2250: 'FAMAS',
                                 3100: 'M4A1-S', 3300: 'AUG', 5000: 'SCAR-Twenty'}

    primary_t_price = {
        'Nova': 1200,
        'XMOneZeroOneFour': 2000,
        'Negev': 2000,
        'Sawed-Off': 1200,
        'Mac-Ten': 1050,
        'UMP-FourtyFive': 1200,
        'PNinety': 2350,
        'PP-Bizon': 1400,
        'SSGOhEight': 1700,
        'AWP': 4750,
        'Galil': 2000,
        'AK': 2700,
        'SSGFiveFiveThree': 3000,
        'GThreeSGOne': 5000,

    }

    primary_t_price_inverted = {1200: 'UMP-FourtyFive', 2000: 'Galil', 1050: 'Mac-Ten', 2350: 'PNinety',
                                1400: 'PP-Bizon', 1700: 'SSGOhEight', 4750: 'AWP', 2700: 'AK', 3000: 'SSGFiveFiveThree',
                                5000: 'GThreeSGOne'}

    secondary_ct_price = {
        'DualBerettas': 400,
        'PTwoFifty': 300,
        'DesertEagle': 700,
        'USP-S': 200,
        'PTwoThousand': 200,
        'Five-Seven': 500,
        'CZSevenFive-Auto': 500,
        'Revolver': 600,
    }

    secondary_ct_price_inverted = {400: 'DualBerettas', 300: 'P250', 700: 'DesertEagle', 200: 'P2000', 500: 'CZ75-Auto',
                                   600: 'Revolver'}

    secondary_t_price = {
        'DualBerettas': 400,
        'PTwoFifty': 300,
        'DesertEagle': 700,
        'Glock': 200,
        'Five-Seven': 500,
        'Tec-Nine': 500,
        'Revolver': 600,

    }

    secondary_t_price_inverted = {400: 'DualBerettas', 300: 'P250', 700: 'DesertEagle', 200: 'Glock', 500: 'Tec-9',
                                  600: 'Revolver'}

    res = key, val = random.choice(list(primary_t_price.items()))

    random_primary_t = str(res)

    random_primary_t = random_primary_t.replace(',', "")

    random_primary_t = (re.sub("'", "", random_primary_t))
    random_primary_t = (re.sub(r'[a-zA-Z]', r'', random_primary_t))
    random_primary_t = (random_primary_t.replace("-", ""))
    random_primary_t = re.sub(" ", "", random_primary_t)
    random_primary_t = (random_primary_t.replace("(", ""))
    random_primary_t = random_primary_t.replace(")", "")

    res = key, val = random.choice(list(secondary_t_price.items()))

    random_secondary_t = str(res)

    random_secondary_t = random_secondary_t.replace(',', "")

    random_secondary_t = (re.sub("'", "", random_secondary_t))
    random_secondary_t = (re.sub(r'[a-zA-Z]', r'', random_secondary_t))
    random_secondary_t = (random_secondary_t.replace("-", ""))
    random_secondary_t = re.sub(" ", "", random_secondary_t)
    random_secondary_t = (random_secondary_t.replace("(", ""))
    random_secondary_t = random_secondary_t.replace(")", "")

    secondary_weapon_price = float(random_secondary_t)
    print(secondary_ct_price_inverted.get(float(random_secondary_t)))
    print(primary_ct_price_inverted.get(float(random_primary_t)))
    primary_weapon_price = float(random_primary_t)

    grenades_CT = ['IncendiaryGrenade', 'DecoyGrenade', 'Flashbang', 'HighExplosiveGrenade', 'SmokeGrenade', 'Zeusx27']
    grenade_ct_prices = {
        "Incendiary Grenade": 600,
        "Decoy Grenade": 50,
        "Grenade": 300,
        "Smoke": 200,
        "Flashbang": 200,

    }

    grenade_ct_prices_inverted = {
        600: "Incendiary Grenade",
        50: "Decoy Grenade",
        300: "Grenade",
        200: "Smoke",
        200: "Flashbang",

    }

    grenade_t_prices = {
        "Molotov": 400,
        "Decoy Grenade": 50,
        "Grenade": 300,
        "Smoke": 200,
        "Flashbang": 200,

    }

    grenade_t_prices_inverted = {
        400: "Molotov",
        50: "Decoy Grenade",
        300: "Grenade",
        200: "Smoke",
        200.1: "Flashbang",

    }

    grenadesstr = key, val = random.choice(list(grenade_ct_prices.items()))

    random_grenade_t = str(grenadesstr)

    random_grenade_t = random_grenade_t.replace(',', "")

    random_grenade_t = (re.sub("'", "", random_grenade_t))
    random_grenade_t = (re.sub(r'[a-zA-Z]', r'', random_grenade_t))
    random_grenade_t = (random_grenade_t.replace("-", ""))
    random_grenade_t = re.sub(" ", "", random_grenade_t)
    random_grenade_t = (random_grenade_t.replace("(", ""))
    random_grenade_t = random_grenade_t.replace(")", "")

    first_grenade_cost = str(random_grenade_t)
    grenade_name = (grenade_ct_prices_inverted.get(float(first_grenade_cost)))
    grenade_ct_prices_inverted.pop(float(first_grenade_cost))
    print(grenade_name)
    grenade_ct_prices.pop(str(grenade_name))
    if KeyError:
        continue

    grenadesstr = key, val = random.choice(list(grenade_ct_prices.items()))

    random_grenade_t = str(grenadesstr)

    random_grenade_t = random_grenade_t.replace(',', "")

    random_grenade_t = (re.sub("'", "", random_grenade_t))
    random_grenade_t = (re.sub(r'[a-zA-Z]', r'', random_grenade_t))
    random_grenade_t = (random_grenade_t.replace("-", ""))
    random_grenade_t = re.sub(" ", "", random_grenade_t)
    random_grenade_t = (random_grenade_t.replace("(", ""))
    random_grenade_t = random_grenade_t.replace(")", "")

    second_grenade_cost = str(random_grenade_t)
    grenade_name = (grenade_ct_prices_inverted.get(float(second_grenade_cost)))
    grenade_ct_prices_inverted.pop(float(second_grenade_cost))
    print(grenade_name)
    grenade_ct_prices.pop(str(grenade_name))
    if KeyError:
        continue

    grenadesstr = key, val = random.choice(list(grenade_ct_prices.items()))

    random_grenade_t = str(grenadesstr)

    random_grenade_t = random_grenade_t.replace(',', "")

    random_grenade_t = (re.sub("'", "", random_grenade_t))
    random_grenade_t = (re.sub(r'[a-zA-Z]', r'', random_grenade_t))
    random_grenade_t = (random_grenade_t.replace("-", ""))
    random_grenade_t = re.sub(" ", "", random_grenade_t)
    random_grenade_t = (random_grenade_t.replace("(", ""))
    random_grenade_t = random_grenade_t.replace(")", "")

    third_grenade_cost = str(random_grenade_t)
    grenade_name = (grenade_ct_prices_inverted.get(float(third_grenade_cost)))
    grenade_ct_prices_inverted.pop(float(third_grenade_cost))
    print(grenade_name)
    grenade_ct_prices.pop(str(grenade_name))
    if KeyError:
        continue

    if not(Casual):
        grenadesstr = key, val = random.choice(list(grenade_ct_prices.items()))

        random_grenade_t = str(grenadesstr)

        random_grenade_t = random_grenade_t.replace(',', "")

        random_grenade_t = (re.sub("'", "", random_grenade_t))
        random_grenade_t = (re.sub(r'[a-zA-Z]', r'', random_grenade_t))
        random_grenade_t = (random_grenade_t.replace("-", ""))
        random_grenade_t = re.sub(" ", "", random_grenade_t)
        random_grenade_t = (random_grenade_t.replace("(", ""))
        random_grenade_t = random_grenade_t.replace(")", "")

        fourth_grenade_cost = str(random_grenade_t)
        grenade_name = (grenade_ct_prices_inverted.get(float(fourth_grenade_cost)))
        grenade_ct_prices_inverted.pop(float(fourth_grenade_cost))
        print(grenade_name)
        grenade_ct_prices.pop(str(grenade_name))
        if KeyError:
            continue




    fourth_grenade_cost = 0
    float(first_grenade_cost)
    float(second_grenade_cost)
    float(third_grenade_cost)
    float(fourth_grenade_cost)

    total_grenade_cost = float(first_grenade_cost + second_grenade_cost + third_grenade_cost + fourth_grenade_cost)

    total_loadout_price = float(primary_weapon_price + secondary_weapon_price + total_grenade_cost + equipment_cost)

    if float(total_loadout_price) <= float(wealth):
        break

quit

if teamchecker == 2:
    quit












