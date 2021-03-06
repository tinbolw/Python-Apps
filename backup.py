loadout_generated = False
wealth = 5000
while not (loadout_generated):
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

primary_t_price_inverted = {1200: 'UMP-FourtyFive', 2000: 'Galil', 1050: 'Mac-Ten', 2350: 'PNinety', 1400: 'PP-Bizon',
                            1700: 'SSGOhEight', 4750: 'AWP', 2700: 'AK', 3000: 'SSGFiveFiveThree', 5000: 'GThreeSGOne'}

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

float(first_grenade_cost)
float(second_grenade_cost)
float(third_grenade_cost)
float(fourth_grenade_cost)

total_grenade_cost = float(first_grenade_cost + second_grenade_cost + third_grenade_cost + fourth_grenade_cost)

total_loadout_price = float(primary_weapon_price + secondary_weapon_price + total_grenade_cost + equipment_cost)

if total_loadout_price <= wealth:
    loadout_generated = True




# backup for original


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
    if not (Casual):
        fourth_nade_index = random.randint(0, 2)
        fourth_nade = str(grenades_CT[fourth_nade_index])
        print(fourth_nade)
        grenades_CT.remove(fourth_nade)




