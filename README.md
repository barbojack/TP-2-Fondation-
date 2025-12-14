# TP-2-Fondation-

Modifier le type
print("3. Modifier les deux")
print("4. Annuler")
sub_choice = input("Votre choix : ")
    
    if sub_choice == "4":
        return
    
    new_name = None
    new_type = None
    
    # Demander le nouveau nom si nécessaire
    if sub_choice in ["1", "3"]:
        new_name = input(f"Nouveau nom (actuel: {vessel._name}) : ").strip()
        if not new_name:
            print("Le nom ne peut pas être vide !")
            input("Appuyez sur Entrée pour continuer...")
            return
    
    # Demander le nouveau type si nécessaire
    if sub_choice in ["2", "3"]:
        new_type = input(f"Nouveau type (actuel: {vessel._shipType}) : ").strip()
        if not new_type:
            print("Le type ne peut pas être vide !")
            input("Appuyez sur Entrée pour continuer...")
            return
    
    # ========== APPLIQUER LES MODIFICATIONS ==========
    
    # Modifier le nom
    if new_name:
        old_name = vessel._name
        vessel._name = new_name
        
        # Mettre à jour la clé dans le dictionnaire
        new_key = new_name.lower().replace(" ", "_")
        # Vérifier que la nouvelle clé n'existe pas déjà
        if new_key != vessel_key and new_key not in VESSELS_DICT:
            VESSELS_DICT[new_key] = vessel  # Ajouter avec la nouvelle clé
            del VESSELS_DICT[vessel_key]     # Supprimer l'ancienne clé
            print(f"Nom modifié : '{old_name}' → '{new_name}'")
        elif new_key in VESSELS_DICT:
            print(f"Un vaisseau avec ce nom existe déjà !")
            vessel._name = old_name  # Annuler la modification
            input("Appuyez sur Entrée pour continuer...")
            return
    
    # Modifier le type
    if new_type:
        old_type = vessel._shipType
        vessel._shipType = new_type
        print(f"Type modifié : '{old_type}' → '{new_type}'")
    
    print(f"\nVaisseau modifié avec succès !")
    input("Appuyez sur Entrée pour continuer...")
    
except ValueError:
    print("Saisie invalide !")
    input("Appuyez sur Entrée pour continuer...")

    def create_fleet():
# Crée une nouvelle flotte vide.
print("\n--- CREATION D'UNE NOUVELLE FLOTTE ---")
name = input("Nom de la flotte (ou 'r' pour retour) : ")
if name.lower() == "r":
    return None

name_key = name.lower()

# Vérifier que le nom n'existe pas déjà
if name_key in FLEETS_DICT:
    print("Ce nom existe déjà !")
    return None

# Créer la flotte avec une liste vide de vaisseaux
new_fleet = Fleet(name, [])
FLEETS_DICT[name_key] = new_fleet
print(f"Flotte '{name}' créée !")
input("Appuyez sur Entrée pour continuer...")
return new_fleet

def delete_fleet():
# Supprime une flotte existante.
Note : Les vaisseaux ne sont pas supprimés, seulement retirés de la flotte.
"""
print("\n--- SUPPRESSION D'UNE FLOTTE ---")

if not FLEETS_DICT:
    print("Aucune flotte disponible !")
    input("Appuyez sur Entrée pour continuer...")
    return

# Afficher toutes les flottes
print("Flottes disponibles :")
fleets_list = list(FLEETS_DICT.keys())
for i, name in enumerate(fleets_list, 1):
    print(f"{i}. {name.capitalize()}")
print("R. Retour au menu principal")

choice = input(f"Choisir la flotte à supprimer (1-{len(fleets_list)}) ou R : ").upper()

if choice == "R":
    return

try:
    index = int(choice) - 1
    if 0 <= index < len(fleets_list):
        fleet_key = fleets_list[index]
        fleet = FLEETS_DICT[fleet_key]
        
        # Demander confirmation en affichant le nombre de vaisseaux
        confirmation = input(
            f"Supprimer '{fleet._name}' et ses {len(fleet._spaceships)} vaisseaux ? (o/n) : "
        ).lower()
        
        if confirmation == "o":
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

def modify_fleet():
# Modifie le nom d'une flotte existante.
print("\n--- MODIFICATION D'UNE FLOTTE ---")
if not FLEETS_DICT:
    print("Aucune flotte disponible !")
    input("Appuyez sur Entrée pour continuer...")
    return

# Afficher toutes les flottes avec leur nombre de vaisseaux
print("Flottes disponibles :")
fleets_list = list(FLEETS_DICT.keys())
for i, name in enumerate(fleets_list, 1):
    fleet = FLEETS_DICT[name]
    print(f"{i}. {fleet._name} ({len(fleet._spaceships)} vaisseaux)")
print("R. Retour au menu principal")

choice = input(f"Choisir la flotte à modifier (1-{len(fleets_list)}) ou R : ").upper()

if choice == "R":
    return

try:
    index = int(choice) - 1
    if not (0 <= index < len(fleets_list)):
        print("Numéro invalide !")
        input("Appuyez sur Entrée pour continuer...")
        return
    
    fleet_key = fleets_list[index]
    fleet = FLEETS_DICT[fleet_key]
    
    # Demander le nouveau nom
    print(f"\n--- Modification de '{fleet._name}' ---")
    new_name = input(f"Nouveau nom (actuel: {fleet._name}) : ").strip()
    
    if not new_name:
        print("Le nom ne peut pas être vide !")
        input("Appuyez sur Entrée pour continuer...")
        return
    
    # Appliquer la modification
    old_name = fleet._name
    fleet._name = new_name
    
    # Mettre à jour la clé dans le dictionnaire
    new_key = new_name.lower()
    if new_key != fleet_key and new_key not in FLEETS_DICT:
        FLEETS_DICT[new_key] = fleet
        del FLEETS_DICT[fleet_key]
        print(f"Nom modifié : '{old_name}' → '{new_name}'")
    elif new_key in FLEETS_DICT:
        print(f"Une flotte avec ce nom existe déjà !")
        fleet._name = old_name  # Annuler
        input("Appuyez sur Entrée pour continuer...")
        return
    
    print(f"\nFlotte modifiée avec succès !")
    input("Appuyez sur Entrée pour continuer...")
    
except ValueError:
    print("Saisie invalide !")
    input("Appuyez sur Entrée pour continuer...")

def add_vessel_to_fleet():
# Ajoute un vaisseau existant à une flotte existante.
Processus en 2 étapes :
1. Choisir le vaisseau à ajouter
2. Choisir la flotte de destination
"""
print("\n--- AJOUTER UN VAISSEAU A UNE FLOTTE ---")

# Vérifier qu'il y a des vaisseaux
if not VESSELS_DICT:
    print("Aucun vaisseau disponible !")
    input("Appuyez sur Entrée pour continuer...")
    return

# Vérifier qu'il y a des flottes
if not FLEETS_DICT:
    print("Aucune flotte disponible !")
    input("Appuyez sur Entrée pour continuer...")
    return

# ========== ÉTAPE 1 : CHOISIR LE VAISSEAU ==========
print("\nVaisseaux disponibles :")
vessels_list = list(VESSELS_DICT.keys())
for i, name in enumerate(vessels_list, 1):
    print(f"{i}. {name.capitalize()}")
print("R. Retour au menu principal")

choice_v = input(f"Choisir le vaisseau (1-{len(vessels_list)}) ou R : ").upper()

if choice_v == "R":
    return

try:
    index_v = int(choice_v) - 1
    if not (0 <= index_v < len(vessels_list)):
        print("Numéro invalide !")
        input("Appuyez sur Entrée pour continuer...")
        return
    
    vessel = VESSELS_DICT[vessels_list[index_v]]
    
    # ========== ÉTAPE 2 : CHOISIR LA FLOTTE ==========
    print("\nFlottes disponibles :")
    fleets_list = list(FLEETS_DICT.keys())
    for i, name in enumerate(fleets_list, 1):
        fleet = FLEETS_DICT[name]
        # Afficher le nombre de vaisseaux actuel / maximum
        print(f"{i}. {name.capitalize()} ({len(fleet._spaceships)}/15 vaisseaux)")
    print("R. Retour au menu principal")
    
    choice_f = input(f"Choisir la flotte (1-{len(fleets_list)}) ou R : ").upper()
    
    if choice_f == "R":
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
    
    # Ajouter le vaisseau à la flotte
    fleet.append_spaceship(vessel)
    print(f"Vaisseau '{vessel._name}' ajouté à la flotte '{fleet._name}' !")
    input("Appuyez sur Entrée pour continuer...")
    
except ValueError:
    print("Saisie invalide !")
    input("Appuyez sur Entrée pour continuer...")

def manage_vessel_crew(vessel: Spaceship):
# Menu de gestion de l'équipage d'un vaisseau.
Permet de :
- Afficher l'équipage complet
- Ajouter des membres (nouveaux ou existants)
- Retirer des membres
"""
while True:
    # Afficher l'en-tête avec le nombre de membres actuel / maximum
    print(f"\n--- EQUIPAGE : {vessel._name} ({len(vessel._crew)}/10) ---")
    print("1. Afficher l'équipage")
    print("2. Ajouter un membre")
    print("3. Retirer un membre")
    print("4. Retour")
    
    choice = input("Votre choix : ")
    
    if choice == "1":
        # Appeler la méthode display_crew() du vaisseau
        vessel.display_crew()
        
    elif choice == "2":
        # Sous-menu pour ajouter un membre
        print("\n1. Créer un nouveau membre")
        print("2. Ajouter un membre existant")
        sub_choice = input("Votre choix : ")
        
        member = None
        
        if sub_choice == "1":
            # Créer un nouveau membre
            member = create_member()
        elif sub_choice == "2":
            # Choisir un membre existant
            print("Membres disponibles :", ", ".join(MEMBERS_DICT.keys()))
            pseudo = input("Pseudo du membre : ").lower()
            member = MEMBERS_DICT.get(pseudo)
            if not member:
                print("Membre introuvable !")
        
        # Ajouter le membre au vaisseau (si trouvé/créé)
        if member:
            vessel.append_member(member)
            
    elif choice == "3":
        # Retirer un membre par son nom de famille
        name = input("Nom de famille du membre à retirer : ")
        vessel.remove_member(name)
        
    elif choice == "4":
        # Retour au menu précédent
        break
    else:
        print("Choix invalide !")

========== AFFICHAGE MENU PRINCIPAL ==========
def display_main_menu():
# Affiche le menu principal du programme.
print("\n" + "=" * 50)
print("         GESTION DE FLOTTES SPATIALES")
print("=" * 50)
print("1. Créer un vaisseau")
print("2. Supprimer un vaisseau")
print("3. Modifier un vaisseau")
print("4. Créer une flotte")
print("5. Supprimer une flotte")
print("6. Modifier une flotte")
print("7. Ajouter un vaisseau à une flotte")
print("8. Créer un membre")
print("9. Supprimer un membre")
print("10. Gérer l'équipage d'un vaisseau")
print("11. Vérifier la préparation au décollage")
print("12. Afficher les statistiques des flottes")
print("13. Actions des membres")
print("14. Sauvegarder l'état de votre jeu")
print("15. Charger une sauvegarde du jeu")
print("16. Supprimer une sauvegarde du jeu")
print("17. Quitter")
print("=" * 50)
def menu_manage_vessels():
# Menu pour sélectionner un vaisseau à gérer.
if not VESSELS_DICT:
print("Aucun vaisseau disponible !")
input("Appuyez sur Entrée pour continuer...")
return
# Afficher tous les vaisseaux
print("\nVaisseaux disponibles :")
vessels_list = list(VESSELS_DICT.keys())
for i, name in enumerate(vessels_list, 1):
    print(f"{i}. {name.capitalize()}")
print("R. Retour au menu principal")

choice = input(f"Choisir (1-{len(vessels_list)}) ou R : ").upper()

if choice == "R":
    return

try:
    index = int(choice) - 1
    if 0 <= index < len(vessels_list):
        vessel = VESSELS_DICT[vessels_list[index]]
        # Ouvrir le menu de gestion de l'équipage pour ce vaisseau
        manage_vessel_crew(vessel)
    else:
        print("Numéro invalide !")
        input("Appuyez sur Entrée pour continuer...")
except ValueError:
    print("Saisie invalide !")
    input("Appuyez sur Entrée pour continuer...")

def menu_verification():
# Menu de vérification de la préparation au décollage.
Vérifie que chaque vaisseau a au moins un pilote ET un technicien.

print("\n--- VERIFICATION DE PREPARATION ---")

if not VESSELS_DICT:
    print("Aucun vaisseau disponible !")
    input("Appuyez sur Entrée pour continuer...")
    return

# Afficher tous les vaisseaux
vessels_list = list(VESSELS_DICT.keys())
print("Vaisseaux disponibles :")
for i, name in enumerate(vessels_list, 1):
    print(f"{i}. {name.capitalize()}")
print("T. Tous les vaisseaux")
print("R. Retour au menu principal")

choice = input(f"Choisir (1-{len(vessels_list)}), T pour tous, ou R : ").upper()

if choice == "R":
    return

# Vérifier tous les vaisseaux
if choice == "T":
    print("\n--- VERIFICATION DE TOUS LES VAISSEAUX ---")
    for vessel in VESSELS_DICT.values():
        vessel.check_preparation()
    input("\nAppuyez sur Entrée pour continuer...")
# Vérifier un vaisseau spécifique
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
# Affiche les statistiques de toutes les flottes.
Pour chaque flotte, affiche :
- Nombre de vaisseaux
- Nombre total de membres
- Répartition des rôles
- Niveau moyen d'expérience des Opérateurs

print("\n--- STATISTIQUES DES FLOTTES ---")

if not FLEETS_DICT:
    print("Aucune flotte disponible !")
    input("Appuyez sur Entrée pour continuer...")
    return

# Afficher les statistiques de chaque flotte
for fleet in FLEETS_DICT.values():
    fleet.statistics()
    input("\nAppuyez sur Entrée pour continuer...")

def menu_member_actions():
# Menu des actions des membres.
Permet de :
- Faire se présenter un membre
- Faire gagner de l'expérience à un Opérateur

while True:
    print("\n--- ACTIONS DES MEMBRES ---")
    
    if not MEMBERS_DICT:
        print("Aucun membre disponible !")
        input("Appuyez sur Entrée pour continuer...")
        return
    
    print("\n1. Présentation d'un membre")
    print("2. Gagner de l'expérience (Opérateur)")
    print("3. Retour")
    
    choice = input("Votre choix : ")
    
    if choice == "3":
        break
    
    # ========== PRÉSENTATION D'UN MEMBRE ==========
    if choice == "1":
        # Afficher tous les membres (Opérateurs ET Mentalistes)
        print("\nMembres disponibles :")
        display_list_in_columns(list(MEMBERS_DICT.keys()))
        
        pseudo = input("\nPseudo du membre : ").lower()
        member = MEMBERS_DICT.get(pseudo)
        
        if not member:
            print("Membre introuvable !")
            input("Appuyez sur Entrée pour continuer...")
            continue
        
        # Appeler la méthode introduce_yourself() du membre
        if hasattr(member, "introduce_yourself"):
            member.introduce_yourself()
            input("\nAppuyez sur Entrée pour continuer...")
        else:
            print(f"{member._first_name} ne peut pas se présenter.")
            input("Appuyez sur Entrée pour continuer...")
    
    # ========== GAGNER DE L'EXPÉRIENCE (OPÉRATEURS SEULEMENT) ==========
    elif choice == "2":
        # Filtrer uniquement les Opérateurs (pas les Mentalistes)
        operators_dict = {
            pseudo: member 
            for pseudo, member in MEMBERS_DICT.items() 
            if isinstance(member, Operator)
        }
        
        if not operators_dict:
            print("Aucun Opérateur disponible !")
            input("Appuyez sur Entrée pour continuer...")
            continue
        
        # Afficher uniquement les Opérateurs avec leurs détails
        print("\nOpérateurs disponibles :")
        operators_list = list(operators_dict.keys())
        for i, pseudo in enumerate(operators_list, 1):
            operator = operators_dict[pseudo]
            print(f"{i}. {pseudo} - {operator._first_name} {operator._last_name} ({operator._role}) [XP: {operator._experience}]")
        
        pseudo = input("\nPseudo de l'Opérateur : ").lower()
        operator = operators_dict.get(pseudo)
        
        if not operator:
            print(f"Opérateur '{pseudo}' introuvable !")
            input("Appuyez sur Entrée pour continuer...")
            continue
        
        # Faire gagner 1 point d'expérience
        operator.gain_experience()
        input("\nAppuyez sur Entrée pour continuer...")
    else:
        print("Choix invalide !")
        input("Appuyez sur Entrée pour continuer...")

def main_program_loop():
# Boucle principale du programme.
- Charge une sauvegarde au démarrage (si disponible)
- Affiche le menu principal
- Traite le choix de l'utilisateur
- Répète jusqu'à ce que l'utilisateur quitte
# Tenter de charger une sauvegarde au démarrage
load_program_state()

while True:
    display_main_menu()
    choice = input("Votre choix : ")
    
    # Traiter le choix de l'utilisateur
    if choice == "1":
        create_spaceship()
    elif choice == "2":
        delete_spaceship()
    elif choice == "3":
        modify_spaceship()
    elif choice == "4":
        create_fleet()
    elif choice == "5":
        delete_fleet()
    elif choice == "6":
        modify_fleet()
    elif choice == "7":
        add_vessel_to_fleet()
    elif choice == "8":
        create_member()
    elif choice == "9":
        delete_member()
    elif choice == "10":
        menu_manage_vessels()
    elif choice == "11":
        menu_verification()
    elif choice == "12":
        menu_statistics()
    elif choice == "13":
        menu_member_actions()
    elif choice == "14":
        save_program_state()
    elif choice == "15":
        load_program_state()
    elif choice == "16":
        delete_save_file()
    elif choice == "17":
        # Quitter le programme
        print("\nAu revoir !")
        break
    else:
        print("Choix invalide ! Entrez un numéro entre 1 et 17.")

========== LANCEMENT DU PROGRAMME ==========
# Point d'entrée du programme
if name == "main":
main_program_loop()