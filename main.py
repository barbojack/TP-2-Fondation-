from classes.Member import *
from classes.Operator import Operator
from classes.Mentalist import Mentalist
from classes.Spaceship import Spaceship
from classes.Fleet import Fleet
from typing import Dict, Any, List # Importations ajoutées pour la clarté

# ========== CREATION DES MEMBRES ==========
chris = Operator("Chris", "Chevalier", "homme", 33, "armurier")
charif = Operator("Charif", "El Bakkali", "homme", 19, "homme de ménage")
khalil = Operator("Khalil", "Serdoun", "homme", 19, "technicien")
paul = Mentalist("Paul", "VAN de WALLE", "homme", 19, 10000)
yoda = Operator("Maître", "Yoda", "homme", 100, "commandant")      
anakin = Operator("Anakin", "Skywalker", "homme", 26, "pilote")
luke = Mentalist("Luke", "Skywalker", "homme", 18, 100)
obiwan = Mentalist("Obi-Wan", "Kenobi", "homme", 30, 100)
r2d2 = Operator("R2D2", "", "droide", 20, "technicien")
poe = Operator("Poe", "Dameron", "homme", 30, "pilote")
leia = Operator("Leia", "Skywalker", "femme", 18, "pilote")
c3po = Operator("C3PO", "", "droide", 30, "technicien")
sidious = Mentalist("Dark", "Sidious", "homme", 50, 100)
trooper = Operator("Trooper", "Ang", "homme", 25, "technicien")

# ========== CREATION DES VAISSEAUX ==========
star_destroyer = Spaceship("Star Destroyer", "Vaisseau de Combat")
hunter = Spaceship("Hunter", "Vaisseau de Combat")
amiral = Spaceship("Amiral", "Vaisseau de Commandement")
x_wing = Spaceship("X-Wing", "Vaisseau de Combat")

# ========== CREATION DES FLOTTES ==========
sith = Fleet("Sith", [])
republic = Fleet("Republic", [])

# ========== AJOUT DES VAISSEAUX AUX FLOTTES ==========
sith.append_spaceship(star_destroyer)
sith.append_spaceship(hunter)
republic.append_spaceship(amiral)
republic.append_spaceship(x_wing)

# ========== AJOUT DES MEMBRES AUX VAISSEAUX ==========
# Star Destroyer
star_destroyer.append_member(charif)
star_destroyer.append_member(chris)
star_destroyer.append_member(khalil)
star_destroyer.append_member(paul)
star_destroyer.append_member(anakin)

# Amiral
amiral.append_member(yoda)
amiral.append_member(leia)
amiral.append_member(c3po)
amiral.append_member(obiwan)
amiral.append_member(luke)

# X-Wing
x_wing.append_member(poe)
x_wing.append_member(r2d2)

# Hunter
hunter.append_member(sidious)
hunter.append_member(trooper)

# ========== TESTS INITIAUX ==========
print("\n=== TESTS DES FONCTIONNALITES ===")
charif.act()
paul.introduce_yourself()
luke.refill_mana()
khalil.gain_experience()

# Vérifications
star_destroyer.check_preparation()
hunter.check_preparation()

# Statistiques
sith.statistics()
republic.statistics()

# ========== REGISTRES GLOBAUX ==========
# Dictionnaires pour stocker tous les objets créés
MEMBERS_DICT: Dict[str, Any] = {}
VESSELS_DICT: Dict[str, Spaceship] = {}
FLEETS_DICT: Dict[str, Fleet] = {}

# Remplir automatiquement les dictionnaires
for name, obj in list(globals().items()):
    if isinstance(obj, (Operator, Mentalist)):
        MEMBERS_DICT[name.lower()] = obj
    elif isinstance(obj, Spaceship):
        VESSELS_DICT[name.lower()] = obj
    elif isinstance(obj, Fleet):
        FLEETS_DICT[name.lower()] = obj

# ========== FONCTIONS UTILITAIRES (UTILITY FUNCTIONS) ==========

def display_list_in_columns(items: List[str], num_columns: int = 4, column_width: int = 12):
    """Affiche une liste d'éléments en plusieurs colonnes."""
    for i, item in enumerate(items):
        print(f"{item.ljust(column_width)}", end="")
        if (i + 1) % num_columns == 0:
            print()  # Retour à la ligne
    if len(items) % num_columns != 0:
        print()  # Dernière ligne si incomplète
        
def create_member():
    """Crée un nouveau membre (Operator ou Mentalist)."""
    print("\n--- CREATION D'UN NOUVEAU MEMBRE ---")
    
    pseudo = input("Pseudo unique (ou 'r' pour retour) : ").lower()
    if pseudo == 'r':
        return None
        
    if pseudo in MEMBERS_DICT:
        print("Ce pseudo existe déjà !")
        return None
        
    prenom = input("Prénom : ")
    nom = input("Nom : ")
    genre = input("Genre : ")
    age = input("Âge : ")
    
    print("\nType de membre :")
    print("1. Opérateur")
    print("2. Mentaliste")
    choix = input("Votre choix (1 ou 2) : ")
    
    if choix == '1':
        role = input("Rôle (pilote, technicien, etc.) : ")
        new_member = Operator(prenom, nom, genre, age, role)
        MEMBERS_DICT[pseudo] = new_member
        print(f"Opérateur {prenom} {nom} créé !")
        return new_member
            
    elif choix == '2':
        try:
            mana = int(input("Niveau de mana : "))
            new_member = Mentalist(prenom, nom, genre, age, mana)
            MEMBERS_DICT[pseudo] = new_member
            print(f"Mentaliste {prenom} {nom} créé !")
            return new_member
        except ValueError:
            print("Le mana doit être un nombre !")
            return None
    else:
        print("Choix invalide !")
        return None

def create_spaceship():
    """Crée un nouveau vaisseau."""
    print("\n--- CREATION D'UN NOUVEAU VAISSEAU ---")
    
    name = input("Nom du vaisseau (ou 'r' pour retour) : ")
    if name.lower() == 'r':
        return None
        
    name_key = name.lower().replace(" ", "_")
    
    if name_key in VESSELS_DICT:
        print("Ce nom existe déjà !")
        return None
        
    vessel_type = input("Type (Combat, Commandement, etc.) : ")
    
    new_vessel = Spaceship(name, vessel_type)
    VESSELS_DICT[name_key] = new_vessel
    print(f"✓ Vaisseau '{name}' créé !")
    
    return new_vessel

def delete_spaceship():
    """Supprime un vaisseau existant."""
    print("\n--- SUPPRESSION D'UN VAISSEAU ---")
    
    if not VESSELS_DICT:
        print("Aucun vaisseau disponible !")
        input("Appuyez sur Entrée pour continuer...")
        return
        
    print("Vaisseaux disponibles :")
    vessels_list = list(VESSELS_DICT.keys())
    for i, name in enumerate(vessels_list, 1):
        print(f"{i}. {name.capitalize()}")
    print("R. Retour au menu principal")
    
    choice = input(f"Choisir le vaisseau à supprimer (1-{len(vessels_list)}) ou R : ").upper()
    
    if choice == 'R':
        return
        
    try:
        index = int(choice) - 1
        if 0 <= index < len(vessels_list):
            vessel_key = vessels_list[index]
            vessel = VESSELS_DICT[vessel_key]
                        
            # Retirer le vaisseau de toutes les flottes
            for fleet in FLEETS_DICT.values():
                if vessel in fleet._spaceships:
                    fleet._spaceships.remove(vessel)
                        
            del VESSELS_DICT[vessel_key]
            print(f"Vaisseau '{vessel._name}' supprimé !")
            input("Appuyez sur Entrée pour continuer...")
        else:
            print("Numéro invalide !")
            input("Appuyez sur Entrée pour continuer...")
    except ValueError:
        print("Saisie invalide !")
        input("Appuyez sur Entrée pour continuer...")

def create_fleet():
    """Crée une nouvelle flotte."""
    print("\n--- CREATION D'UNE NOUVELLE FLOTTE ---")
    
    name = input("Nom de la flotte (ou 'r' pour retour) : ")
    if name.lower() == 'r':
        return None
        
    name_key = name.lower()
    
    if name_key in FLEETS_DICT:
        print("Ce nom existe déjà !")
        return None
        
    new_fleet = Fleet(name, [])
    FLEETS_DICT[name_key] = new_fleet
    print(f"✓ Flotte '{name}' créée !")
    input("Appuyez sur Entrée pour continuer...")
    return new_fleet

def delete_fleet():
    """Supprime une flotte existante."""
    print("\n--- SUPPRESSION D'UNE FLOTTE ---")
    
    if not FLEETS_DICT:
        print("Aucune flotte disponible !")
        input("Appuyez sur Entrée pour continuer...")
        return
        
    print("Flottes disponibles :")
    fleets_list = list(FLEETS_DICT.keys())
    for i, name in enumerate(fleets_list, 1):
        print(f"{i}. {name.capitalize()}")
    print("R. Retour au menu principal")
    
    choice = input(f"Choisir la flotte à supprimer (1-{len(fleets_list)}) ou R : ").upper()
    
    if choice == 'R':
        return
        
    try:
        index = int(choice) - 1
        if 0 <= index < len(fleets_list):
            fleet_key = fleets_list[index]
            fleet = FLEETS_DICT[fleet_key]
                        
            # Confirmer la suppression
            confirmation = input(f"Supprimer '{fleet._name}' et ses {len(fleet._spaceships)} vaisseaux ? (o/n) : ").lower()
            if confirmation == 'o':
                del FLEETS_DICT[fleet_key]
                print(f"✓ Flotte '{fleet._name}' supprimée !")
            else:
                print("Suppression annulée.")
            input("Appuyez sur Entrée pour continuer...")
        else:
            print("Numéro invalide !")
            input("Appuyez sur Entrée pour continuer...")
    except ValueError:
        print("Saisie invalide !")
        input("Appuyez sur Entrée pour continuer...")

def add_vessel_to_fleet():
    """Ajoute un vaisseau existant à une flotte."""
    print("\n--- AJOUTER UN VAISSEAU A UNE FLOTTE ---")
    
    if not VESSELS_DICT:
        print("Aucun vaisseau disponible !")
        input("Appuyez sur Entrée pour continuer...")
        return
        
    if not FLEETS_DICT:
        print("Aucune flotte disponible !")
        input("Appuyez sur Entrée pour continuer...")
        return
        
    # Choisir le vaisseau
    print("\nVaisseaux disponibles :")
    vessels_list = list(VESSELS_DICT.keys())
    for i, name in enumerate(vessels_list, 1):
        print(f"{i}. {name.capitalize()}")
    print("R. Retour au menu principal")
    
    choice_v = input(f"Choisir le vaisseau (1-{len(vessels_list)}) ou R : ").upper()
    
    if choice_v == 'R':
        return
        
    try:
        index_v = int(choice_v) - 1
        if not (0 <= index_v < len(vessels_list)):
            print("Numéro invalide !")
            input("Appuyez sur Entrée pour continuer...")
            return
            
        vessel = VESSELS_DICT[vessels_list[index_v]]
                
        # Choisir la flotte
        print("\nFlottes disponibles :")
        fleets_list = list(FLEETS_DICT.keys())
        for i, name in enumerate(fleets_list, 1):
            fleet = FLEETS_DICT[name]
            print(f"{i}. {name.capitalize()} ({len(fleet._spaceships)}/15 vaisseaux)")
        print("R. Retour au menu principal")
        
        choice_f = input(f"Choisir la flotte (1-{len(fleets_list)}) ou R : ").upper()
        
        if choice_f == 'R':
            return
            
        index_f = int(choice_f) - 1
        if not (0 <= index_f < len(fleets_list)):
            print("Numéro invalide !")
            input("Appuyez sur Entrée pour continuer...")
            return
            
        fleet = FLEETS_DICT[fleets_list[index_f]]
                
        # Vérifier si le vaisseau est déjà dans cette flotte
        if vessel in fleet._spaceships:
            print(f"Le vaisseau '{vessel._name}' est déjà dans la flotte '{fleet._name}' !")
            input("Appuyez sur Entrée pour continuer...")
            return
            
        # Ajouter le vaisseau
        fleet.append_spaceship(vessel)
        print(f"✓ Vaisseau '{vessel._name}' ajouté à la flotte '{fleet._name}' !")
        input("Appuyez sur Entrée pour continuer...")
        
    except ValueError:
        print("❌ Saisie invalide !")
        input("Appuyez sur Entrée pour continuer...")

def manage_vessel_crew(vessel: Spaceship):
    """Menu de gestion de l'équipage d'un vaisseau."""
    while True:
        print(f"\n--- EQUIPAGE : {vessel._name} ({len(vessel._crew)}/10) ---")
        print("1. Afficher l'équipage")
        print("2. Ajouter un membre")
        print("3. Retirer un membre")
        print("4. Retour")
        
        choice = input("Votre choix : ")
        
        if choice == '1':
            vessel.display_crew()
            
        elif choice == '2':
            print("\n1. Créer un nouveau membre")
            print("2. Ajouter un membre existant")
            sub_choice = input("Votre choix : ")
            
            member = None
            if sub_choice == '1':
                member = create_member()
            elif sub_choice == '2':
                print("Membres disponibles :", ", ".join(MEMBERS_DICT.keys()))
                pseudo = input("Pseudo du membre : ").lower()
                member = MEMBERS_DICT.get(pseudo)
                if not member:
                    print("Membre introuvable !")
                        
            if member:
                vessel.append_member(member)
                        
        elif choice == '3':
            name = input("Nom de famille du membre à retirer : ")
            vessel.remove_member(name)
            
        elif choice == '4':
            break
        else:
            print("Choix invalide !")

# ========== MENU PRINCIPAL FUNCTIONS ==========

def display_main_menu():
    """Affiche le menu principal."""
    print("\n" + "="*50)
    print("         GESTION DE FLOTTES SPATIALES")
    print("="*50)
    print("1. Créer un vaisseau")
    print("2. Supprimer un vaisseau")
    print("3. Créer une flotte")
    print("4. Supprimer une flotte")
    print("5. Ajouter un vaisseau à une flotte")
    print("6. Gérer l'équipage d'un vaisseau")
    print("7. Vérifier la préparation au décollage")
    print("8. Afficher les statistiques des flottes")
    print("9. Actions des membres")
    print("10. Quitter")
    print("="*50)

def menu_manage_vessels():
    """Menu pour gérer l'équipage d'un vaisseau."""
    if not VESSELS_DICT:
        print("Aucun vaisseau disponible !")
        input("Appuyez sur Entrée pour continuer...")
        return
        
    print("\nVaisseaux disponibles :")
    vessels_list = list(VESSELS_DICT.keys())
    for i, name in enumerate(vessels_list, 1):
        print(f"{i}. {name.capitalize()}")
    print("R. Retour au menu principal")
    
    choice = input(f"Choisir (1-{len(vessels_list)}) ou R : ").upper()
    
    if choice == 'R':
        return
        
    try:
        index = int(choice) - 1
        if 0 <= index < len(vessels_list):
            vessel = VESSELS_DICT[vessels_list[index]]
            manage_vessel_crew(vessel)
        else:
            print("Numéro invalide !")
            input("Appuyez sur Entrée pour continuer...")
    except ValueError:
        print("Saisie invalide !")
        input("Appuyez sur Entrée pour continuer...")

def menu_verification():
    """Vérification de la préparation des vaisseaux."""
    print("\n--- VERIFICATION DE PREPARATION ---")
    
    if not VESSELS_DICT:
        print("Aucun vaisseau disponible !")
        input("Appuyez sur Entrée pour continuer...")
        return
        
    vessels_list = list(VESSELS_DICT.keys())
    print("Vaisseaux disponibles :")
    for i, name in enumerate(vessels_list, 1):
        print(f"{i}. {name.capitalize()}")
    print("T. Tous les vaisseaux")
    print("R. Retour au menu principal")
    
    choice = input(f"Choisir (1-{len(vessels_list)}), T pour tous, ou R : ").upper()
    
    if choice == 'R':
        return
        
    if choice == 'T':
        print("\n--- VERIFICATION DE TOUS LES VAISSEAUX ---")
        for vessel in VESSELS_DICT.values():
            vessel.check_preparation()
        input("\nAppuyez sur Entrée pour continuer...")
    else:
        try:
            index = int(choice) - 1
            if 0 <= index < len(vessels_list):
                vessel = VESSELS_DICT[vessels_list[index]]
                print(f"\n--- {vessel._name.upper()} ---")
                vessel.check_preparation()
                input("\nAppuyez sur Entrée pour continuer...")
            else:
                print("Numéro invalide !")
                input("Appuyez sur Entrée pour continuer...")
        except ValueError:
            print("Saisie invalide !")
            input("Appuyez sur Entrée pour continuer...")

def menu_statistics():
    """Afficher les statistiques des flottes."""
    print("\n--- STATISTIQUES DES FLOTTES ---")
    
    if not FLEETS_DICT:
        print("❌ Aucune flotte disponible !")
        input("Appuyez sur Entrée pour continuer...")
        return
        
    for fleet in FLEETS_DICT.values():
        fleet.statistics()
        input("\nAppuyez sur Entrée pour continuer...")

def menu_member_actions():
    """Menu des actions des membres."""
    while True:
        print("\n--- ACTIONS DES MEMBRES ---")
        
        if not MEMBERS_DICT:
            print("❌ Aucun membre disponible !")
            return
                
        print("Membres disponibles :")
        display_list_in_columns(list(MEMBERS_DICT.keys()))
                
        print("\n1. Présentation d'un membre")
        print("2. Gagner de l'expérience (Opérateur)")
        print("3. Retour")
        
        choice = input("Votre choix : ")
        
        if choice == '3':
            break
            
        if choice in ['1', '2']:
            pseudo = input("Pseudo du membre : ").lower()
            member = MEMBERS_DICT.get(pseudo)
                        
            if not member:
                print("Membre introuvable !")
                continue
                        
            if choice == '1':
                if hasattr(member, 'introduce_yourself'):
                    member.introduce_yourself()
                else:
                    print(f"{member._first_name} ne peut pas se présenter.")
                                
            elif choice == '2':
                if isinstance(member, Operator):
                    member.gain_experience()
                else:
                    print(f"{member._first_name} n'est pas un Opérateur !")
        else:
            print("Choix invalide !")

def main_program_loop():
    """Boucle principale du programme."""
    while True:
        display_main_menu()
        choice = input("Votre choix : ")
        
        if choice == '1':
            create_spaceship()
        elif choice == '2':
            delete_spaceship()
        elif choice == '3':
            create_fleet()
        elif choice == '4':
            delete_fleet()
        elif choice == '5':
            add_vessel_to_fleet()
        elif choice == '6':
            menu_manage_vessels()
        elif choice == '7':
            menu_verification()
        elif choice == '8':
            menu_statistics()
        elif choice == '9':
            menu_member_actions()
        elif choice == '10':
            print("\nAu revoir !")
            break
        else:
            print("Choix invalide ! Entrez un numéro entre 1 et 10.")

# ========== LANCEMENT DU PROGRAMME ==========
if __name__ == "__main__":
    main_program_loop()