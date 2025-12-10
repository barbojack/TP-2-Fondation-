from classes.Member import *
from classes.Operator import Operator
from classes.Mentalist import Mentalist
from classes.Spaceship import Spaceship
from classes.Fleet import Fleet

COLONNES_MEMBRE = 4
LARGEUR_COLONNE_MEMBRE = 12
COLONNES_VAISSEAU = 3
LARGEUR_COLONNE_VAISSEAU = 15

chris = Operator("Chris", "Chevalier", "homme", 33, "armurier")
charif = Operator("Charif", "El Bakkali", "homme", 19, "homme de ménage")
khalil = Operator("Khalil", "Serdoun", "homme", "19", "technicien")
paul = Mentalist("Paul", "VAN de WALLE", "homme", 19, 10000)
yoda = Operator("Yoda", "Maître", "homme", 100, "commandant")      
anakin = Operator("Anakin", "Skywalker", "homme", 26, "pilote")
luke = Mentalist("Luke", "Skywalker", "homme", 18, 100)
obiwan = Mentalist("Obi-Wan", "Kenobi", "homme", 30, 100)
r2d2 = Operator("R2D2", "Droide", "homme", 20, "technicien")
poe = Operator("Poe", "Dameron", "homme", 30, "pilote")
leia = Operator("Leia", "Skywalker", "femme", 18, "pilote")
c3pO = Operator("C3PO", "Droide", "homme", 30, "technicien")
sidious = Mentalist("Dark", "Sidious", "homme", 50, 100)
trooper = Operator("Trooper", "Ang", "homme", 25, "technicien")

charif.act()
print(charif._role)
print(chris._first_name)
paul.act(charif)

# Création des Vaisseaux

star_destroyer = Spaceship("Star Destroyer", "Vaisseau de Combat")
hunter = Spaceship("Hunter", "Vaisseau de Combat")
amiral = Spaceship("Amiral", "Vaisseau de Commandement")
x_wing = Spaceship("X-Wing", "Vaisseau de Combat")

# sith = Fleet("Sith", [])      # On a besoin des [] car c'est une liste de vaisseaux dans la flotte

sith = Fleet ("Sith", [])
republic = Fleet("Republic", [])

# Ajout des vaisseaux dans la flotte

sith.append_spaceship(star_destroyer)
sith.append_spaceship(hunter)
republic.append_spaceship(amiral)
republic.append_spaceship(x_wing)


# Ajout de membres dans le vaisseau Star_Destroyer

star_destroyer.append_member(charif)
star_destroyer.append_member(chris)
star_destroyer.append_member(khalil)
star_destroyer.append_member(paul)
star_destroyer.append_member(anakin)

amiral.append_member(yoda)
amiral.append_member(leia)
amiral.append_member(c3pO)
amiral.append_member(obiwan)
amiral.append_member(luke)

x_wing.append_member(poe)
x_wing.append_member(r2d2)

# Ajout de membres dans le vaisseau Hunter

hunter.append_member(sidious)
hunter.append_member(trooper)
hunter.append_member(anakin)

# Vérification de la préparation du vaisseau Star Destroyer

star_destroyer.check_preparation()
hunter.check_preparation()

# Test des classes 

paul.introduce_yourself()

luke.refill_mana()
yoda.gain_experience()
khalil.gain_experience()
anakin.gain_experience()
poe.gain_experience()
anakin.gain_experience()
leia.gain_experience()
r2d2.gain_experience()


sith.statistics() 
republic.statistics()               # les mentalists ne sont pas afficher dans la répartition des rôles

amiral.remove_member("Kenobi")
star_destroyer.remove_member("Chevalier")

amiral.append_member(obiwan)
star_destroyer.append_member(chris)

amiral.display_crew()
star_destroyer.display_crew()

# Registre central des membres (pour le menu interactif)

available_members: dict[str, any] = {}
available_vessels: dict[str, Spaceship] = {}
available_fleets: dict[str, Fleet] = {}

for variable_name, object in list(globals().items()):
    if isinstance(object, (Operator, Mentalist)):
        available_members[variable_name.lower()] = object
    elif isinstance(object, Spaceship):
        available_vessels[variable_name.lower()] = object
    elif isinstance(object, Fleet):
        available_fleets[variable_name.lower()] = object


def afficher_en_colonnes(items: list[str], colonnes: int, largeur_colonne: int):
    for i, name in enumerate(items):
        print(f"{name.ljust(largeur_colonne)}", end="")
        if (i + 1) % colonnes == 0:
            print()
    if len(items) % colonnes != 0:
        print()

# Création d'une nouvelle flotte et l'ajoute au registre des flottes

def interactive_fleet_creation():
    print("\n--- CREATION D'UNE NOUVELLE FLOTTE ---")
    fleet_name_lower = input("Nom de la flotte : ").lower
    if fleet_name_lower in available_fleets:
        print("Ce nom de flotte est déjà utilisé.")
        return None
    real_fleet_name = input("Confirmez le nom de la flotte : ")
    try:
        new_fleet = Fleet(str(real_fleet_name), [])
        available_fleets[fleet_name_lower] = new_fleet
        print(f"Flotte '{new_fleet}' créée et enregistrée.")
        return new_fleet
    except Exception as e:
        print(f"Erreur lors de la création de la flotte : {e}")
        return None
    
# Création d'un nouveau vaisseau et l'ajoute au registre des vaisseaux

def interactive_vessel_creation():
    print("\n--- CREATION D'UN NOUVEAU VAISSEAU ---")
    vessel_name = input("Nom du Vaisseau : ").lower()
    if vessel_name in available_vessels:
        print("Ce nom de Vaisseau est déjà utilisé.")
        return None
    vessel_type = input("Type de Vaisseau : ")
    try:
        new_spaceship = Spaceship(vessel_name.capitalize(), vessel_type)
        available_vessels[vessel_name] = new_spaceship
        print(f"Vaisseau '{new_spaceship._name}' créée et enregistré.")
        if available_fleets:
            print("\nVoulez-vous intégrer ce vaisseau à une flotte existante ? ")
            fleets_names = [str(key) for key in available_fleets.keys()]
            print("Flottes disponibles :", ", ".join(fleets_names))
            fleet_choice = input("Votre choix : ").upper()
            if fleet_choice == '0':
                target_fleet_name = input("Nom de la flotte cible : ").lower()
                target_fleet = available_fleets.get(target_fleet_name)
                if target_fleet:
                    target_fleet.append_spaceship(new_spaceship)
                    print(f"Vaisseau '{new_spaceship._name}' ajouté à la flotte '{target_fleet_name}'.")
                else:
                    print("Flotte introuvable. Le Vaisseau n'a pas été ajouté à une flotte.")
        return new_spaceship
    except Exception as e:
        print(f"Erreur lors de la création du Vaisseau : {e}")
        return None


# Création d'un menu en ligne de commande

def interactive_member_creation():
    print("\n--- CREATION D'UN NOUVEAU MEMBRE ---")
    variable_name = input("Pseudo unique pour ce membre : ").lower
    if variable_name in available_members:
        print("Ce pseudo est déjà utilisé. Veuillez en choisir un autre.")
        return None
    first_name = input("Prénom : ")
    last_name = input("Nom de famille : ")
    gender = input("Genre : ")
    age = input("Age : ")
    while True:
        member_type = input("Type (1 pour Operateur, 2 pour Mentalist) : ").upper()
        if member_type == '1':
            role = input("Rôle de l'Operateur : ")
            new_member = Operator(first_name, last_name, gender, age, role)
            available_members[variable_name] = new_member
            print(f"L'Opérateur {first_name} {last_name} a été créé et enregistré sous '{variable_name}'.")
            return new_member
        elif member_type == '2':
            try:
                mana = int(input("Niveau de Mana : "))
                new_member = Mentalist(first_name, last_name, gender, age, mana)
                available_members[variable_name] = new_member
                print(f"Mentalist {first_name} {last_name} créé et enregistré sous '{variable_name}'.")
                return new_member
            except ValueError:
                print("Erreur : Le niveau de Mana doit être un nombre entier.")
                continue
        else:
            print("Choix invalide. Veuillez entrer '1' ou '2'.")

        
    
def vessel_management_menu(vessel: Spaceship):
    available_vessels = {
        '1': star_destroyer,
        '2': amiral,
        '3': hunter,
        '4': x_wing
    }
    while True:
        print(f"\n--- GESTION DE L'EQUIPAGE : {vessel._name} ({len(vessel._crew)}/10) ---")
        print("1. Afficher l'équipage")
        print("2. Ajouter un membre")
        print("3. Retirer un membre")
        print("4. Retour au Menu Principal")
        choice = input("Votre choix : ").upper()
        if choice == '1':
            vessel.display_crew()
        elif choice == '2':
            print("\nSouhaitez-vous :")
            print("1. Créer un nouveau membre")
            print("2. Ajouter un membre existant")
            add_choice = input("Votre choix : ")
            member_to_add = None
            if add_choice == '1':
                member_to_add = interactive_member_creation()
            elif add_choice == '2': 
                print("Membres disponibles :", ", ".join(available_members.keys()))
                variable_member_name = input("Entrez le pseudo du membre à ajouter : ").lower()
                member_to_add = available_members.get(variable_member_name)
                member_to_add = available_members.get(variable_member_name)
                if not (member_to_add and isinstance(member_to_add, (Operator, Mentalist))):
                    print(f"Erreur : L'objet membre '{variable_member_name}' est introuvable ou n'est pas un membre valide.")
                    member_to_add = None
            if member_to_add:
                vessel.append_member(member_to_add)
        elif choice == '3':
            lastname = input("Entrez le nom de famille du membre à retirer : ")
            vessel.remove_member(lastname)
        elif choice == '4':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
            
def display_menu():
    print("\n-----------------MENU PRINCIPAL-----------------")
    print("1. Gérer un Vaisseau")
    print("2. Vérifier la Préparation de l'équipage afin de décoller")
    print("3. Afficher les statistiques des Flottes")
    print("4. Tester les actions de Membres")
    print("5. Quitter")
    print("--------------------------------------------------")
            
def main_menu():
    vessels = {
        '1': star_destroyer,
        '2': amiral,
        '3': hunter,
        '4': x_wing
    }
    while True:
        display_menu()
        principal_choice = input("Entrez votre choix : ")
        if principal_choice == '1':
            print("\n--- GESTION DES VAISSEAUX ET FLOTTES ---")
            print("1. Gérer l'équipage d'un vaisseau")
            print("2. Créer un nouveau vaisseau et l'intégrer à une flotte")
            print("3. Créer une nouvelle flotte")
            print("4. Retour")
            global_management_option = input("Votre choix : ").upper()
            if global_management_option == '4':
                continue
            if global_management_option == '3':
                interactive_fleet_creation()
                continue
            if global_management_option == '2':
                interactive_vessel_creation()
                continue
            if global_management_option == '1':
                if not available_vessels:
                    print("Aucun Vaisseau disponible. Créez-en un d'abord.")
                    continue
                print("\nChoisir le vaisseau à gérer :")
                vessels_keys = list(available_vessels.keys())
                for i, name in enumerate(vessels_keys):
                    print(f"{i+1}. {name.capitalize().ljust(LARGEUR_COLONNE_VAISSEAU)}", end="")
                    if(i + 1) % COLONNES_VAISSEAU == 0:
                        print()
                if len(vessels_keys) % COLONNES_VAISSEAU != 0:
                    print()
                vessel_choice = input(f"Entrez le numéro (1-{len(vessels_keys)}) : ")
                try:
                    index_vessel = int(vessel_choice) - 1
                    if 0 <= index_vessel < len(vessels_keys):
                        ship_name_select = vessels_keys[index_vessel]
                        select_vessel = available_vessels[ship_name_select]
                        vessel_management_menu(select_vessel)
                    else:
                        print("Numéro de vaisseau invalide.")
                except ValueError:
                    print("Saisie invalide.")
            else:
                print("Choix invalide. Veuillez réessayer.")
        elif principal_choice == '2':
            print("\n--- VERIFICATION DE PREPARATION ---")
            print("Choisir le Vaisseau à vérifier :")
            vessels_keys = list(available_vessels.keys())
            for i, name in enumerate(vessels_keys):
                print(f"{i+1}. {name.capitalize().ljust(LARGEUR_COLONNE_VAISSEAU)}", end="")
                if (i + 1) % COLONNES_VAISSEAU == 0:
                    print()
            if len(vessels_keys) % COLONNES_VAISSEAU != 0:
                print()
            vessel_choice = input(f"Entrez le numéro (1-{len(vessels_keys)}) (ou 'T' pour Tous) : ").upper()
            if vessel_choice == 'T':
                print("\n--- VERIFICATION DE TOUS LES VAISSEAUX ---")
                for object_vessel in available_vessels.values():
                    object_vessel.check_preparation()
            else:
                try:
                    index_vessel = int(vessel_choice) - 1
                    if 0 <= index_vessel < len(vessels_keys):
                        ship_name_select = vessels_keys[index_vessel]
                        vaisseau_selectionne = available_vessels[ship_name_select]
                        print(f"\n--- VÉRIFICATION DU {vaisseau_selectionne._name.upper()} ---")
                        select_vessel.check_preparation()
                    else:
                        print("Numéro de vaisseau invalide.")
                except ValueError:
                    print("Saisie invalide.")
        elif principal_choice == '3':
            print("\n--- STATISTIQUES DES FLOTTES ---")
            if not available_fleets:
                print("Aucune flotte disponible.")
                continue    
            for fleet in available_fleets.values():
                fleet.statistics()
        elif principal_choice == '4':
            while True:
                print("\n--- ACTIONS DES MEMBRES ---")
                members_keys = list(available_members.keys())
                colonnes = 4
                print("Membres disponibles :")
                for i, name in enumerate(members_keys):
                    print(f"{name.ljust(12)}", end="")
                    if (i + 1) % colonnes == 0:
                        print()
                if len(members_keys) % colonnes != 0:
                    print()
                print("1. Demander à un membre de se présenter")
                print("2. Faire gagner de l'expérience à un Opérateur")
                print("3. Retour au Menu Principal")
                action_choice = input("Votre choix : ").upper()
                if action_choice == '3':
                    break
                if action_choice in ['1', '2']:
                    variable_member_name = input("Entrez le pseudo du membre : ").lower()
                    object_member = available_members.get(variable_member_name)
                    if not object_member or not isinstance(object_member, (Operator, Mentalist)):
                        print(f"Erreur : L'objet membre '{variable_member_name}' est introuvable ou n'est pas un membre valide.")
                        continue
                    if action_choice == '1':
                        try:
                            object_member.introduce_yourself()
                        except AttributeError:
                            print(f"{object_member._first_name} ne possède pas de présentation.")
                    elif action_choice == '2':
                        if isinstance(object_member, Operator):
                            try:
                                object_member.gain_experience()
                            except AttributeError:
                                print(f"{object_member._first_name} est un Opérateur, mais ne possède d'expérience.")
                        else: 
                            print(f"Erreur : {object_member._first_name} {object_member._last_name} n'est pas un Opérateur et ne peut donc pas gagner d'expérience.")
                else:
                    print("Choix invalide. Veuillez réessayer.")
            

        elif principal_choice == '5':
            print("Extinction du système. Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro entre 1 et 5.")
            
            
if __name__ == "__main__":
    main_menu()