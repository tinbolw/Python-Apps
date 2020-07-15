

user_name = input("What is your characters name? ")
world_selection = input("Which world do you want to play? \n1. Hell World \n2. Grassy World \n3. Ice World \n")

def load_hell_world():
    import hellworld

def load_grassy_world():
    import grassyworld

def load_ice_world():
    import iceworld

def load_world():
    if world_selection == str("Hell World"):
        print("Loading Hell World....")
        load_hell_world()
    elif world_selection == str("Grassy World"):
        print("Loading Grassy World....")
        load_grassy_world()
    elif world_selection == str("Ice World"):
        print("Loading Ice World....")
        load_ice_world()
    else:
        print("Invalid Selection")




quit
