from classes.Mentalist import Mentalist

class Fleet:

    def __init__(self, name, spaceships):
        self._spaceships = spaceships
        self.__name = name

    @property  # Début de la liste des getters : setters
    def _name(self):  # Le @property est dû au double (__) pour rendre privées les informations
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    def append_spaceship(
        self, spaceships
    ):  # Vérifie que la capacité maximale de 15 vaisseaux est respecter
        if len(self._spaceships) == 15:
            print(
                f"La flotte {self._name} a atteint sa capacité maximale de 15 vaisseaux !!!"
            )
            return False
        self._spaceships.append(spaceships)  # Ajoute un vaisseau à la flotte
        print(
            f"Le vaisseau {self._name} a été ajouté à la flotte. La flotte est composée de {len(self._spaceships)}/15"
        )
        return True

    def statistics(self):
        print(
            f"\n--- Statistiques de la flotte {self._name}---\n"
        )  # Affiche les statistiques de la flotte
        print(
            f"Nombre de vaisseaux : {len(self._spaceships)}"
        )  # Nombres de vaisseaux de la flotte
        if len(self._spaceships) == 0:  # Vérifie si la flotte contient un vaisseau
            print("La flotte est vide.")
            return

        total_members = 0  # Calcul du nombre total de membres présent dans l'équipage
        mentalist_count = 0
        for spaceship in self._spaceships:
            total_members += len(spaceship._crew)
            for member in spaceship._crew:
                if isinstance(member, Mentalist):
                    mentalist_count += 1
        print(f"\nNombre total de membres d'équipage : {total_members}")
        print(f"Nombre total de Mentalists : {mentalist_count}")

        roles = {}  # Répartition des rôles
        for spaceship in self._spaceships:
            for member in spaceship._crew:
                if hasattr(member, '_role'):            # Vérifie si le rôle existe
                    role = member._role
                    if role in roles:
                        roles[role] += 1
                    else:
                        roles[role] = 1

        print(
            "\nRépartition des rôles :"
        )  # Permet d'afficher le nombre de personnes possédant le même rôle
        for role, count in roles.items():
            print(f" -{role} : {count}")

        total_experience = 0
        operators_count = 0

        for spaceship in self._spaceships:
            for member in spaceship._crew:
                if hasattr(member, '_experience'):                  # Vérifie si le membre possède de l'expérience et est donc un Operator
                    total_experience += member._experience
                    operators_count += 1
        if operators_count > 0:
            level_average = (
                total_experience / operators_count
            )  # Calcul du niveau moyen d'expérience des Opérateurs
            print(
                f"\nNiveau moyen d'expérience des opérateurs : {level_average: .2f}"
            )  # Le ".2f" permet d'afficher un nombre avec deux chiffres après la virgule tous le temps
        else:
            print("\nIl n'y a aucun opérateur dans la flotte.")
