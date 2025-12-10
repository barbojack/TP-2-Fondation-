from classes.Member import *
from classes.Operator import Operator
from classes.Mentalist import Mentalist
from classes.Spaceship import Spaceship
from classes.Fleet import Fleet

chris = Operator("Chris", "Chevalier", "homme", 33, "armurier")
print(chris._first_name)
charif = Operator("Charif", "El Bakkali", "homme", 19, "homme de ménage")
print(charif._role)

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

# Création d'un menu en ligne de commande

def interactive_member_creation():
    print("\n--- CREATION D'UN NOUVEAU MEMBRE ---")
    first_name = input("Prénom : ")
    last_name = input("Nom de famille : ")
    gender = input("Genre : ")
    age = input("Age : ")
    while True:
        member_type = input("Type (1 pour Operateur, 2 pour Mentalist) : ").upper()
        if member_type == '1':
            role = input("Rôle de l'Operateur : ")
            new_member = Operator(first_name, last_name, gender, age, role)
            print(f"L'Opérateur {first_name} {last_name} a été créé.")
            return new_member
        elif member_type == '2':
            try:
                mana = int(input("Niveau de Mana : "))
                new_member = Mentalist(first_name, last_name, gender, age, mana)
                return new_member
            except ValueError:
                print("Erreur : Le niveau de Mana doit être un nombre entier.")
                continue
        else:
            print("Choix invalide. Veuillez entrer '1' ou '2'.")
    
def vessel_management_menu(vessel):
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
                variable_member_name = input("Entrez le nom de variable du membre à ajouter : ").lower()
                member_to_add = globals().get(variable_member_name)
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
            print("\nChoisir le Vaisseau à gérer :")
            print("1. Star Destroyer\n2. Amiral\n3. Hunter\n4. X-Wing")
            vessel_choice = input("Entrez le numéro du Vaisseau : ")
            select_vessel = vessels.get(vessel_choice)
            if select_vessel:
                vessel_management_menu(select_vessel)
            else:
                print("Numéro de Vaisseau invalide.")
        elif principal_choice == '2':
            print("\n--- VERIFICATION DE PREPARATION ---")
            print("Choisir le Vaisseau à vérifier :")
            print("1. Star Destoyer\n2. Amiral\n3. Hunter\n4. X-Wing")
            vessel_choice = input("Entrez le numéro du Vaisseau (ou 'T' pour Tous) : ").upper()
            if vessel_choice == 'T':
                print("\n--- VERIFICATION DE TOUS LES VAISSEAUX ---")
                for vessel_name, object_vessel in vessels.items():
                    object_vessel.check_preparation()
            else:
                select_vessel = vessels.get(vessel_choice)
                if select_vessel:
                    print(f"\n--- VERIFICATION DU {select_vessel._name.upper()} ---")
                    select_vessel.check_preparation()
                else:
                    print("Numéro de Vaisseau invalide.")
        elif principal_choice == '3':
            print("\n--- STATISTIQUES DES FLOTTES ---")
            sith.statistics()
            republic.statistics()
        elif principal_choice == '4':
            print("\n--- ACTIONS DES MEMBRES ---")
            yoda.gain_experience()
            obiwan.introduce_yourself()
        elif principal_choice == '5':
            print("Extinction du système. Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro entre 1 et 5.")
            
            
if __name__ == "__main__":
    main_menu()