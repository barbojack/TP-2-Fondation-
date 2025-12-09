from classes.Member import *


class Operator(Member):
    def __init__(self, first_name, last_name, gender, age, role):
        super().__init__(first_name, last_name, gender, age)
        self.__role = role
        self.__experience = 0

    @property  # Le @property permet de rendre privées les informations
    def _role(self):  # Début des getters / setters
        return self.__role

    @_role.setter
    def _role(self, value):
        self.__role = value

    @property
    def _experience(self):
        return self.__experience

    @_experience.setter
    def _experience(self, value):
        self.__experience = value  # Fin des getters / setters

    def act(self):  # affiche le message pour chaque rôle
        actions = {
            "technicien": "répare les sytèmes du vaisseau",
            "homme de ménage": "nettoie le vaisseau",
            "pilote": "pilote le vaisseau",
            "commandant": "dirige les membres du vaisseau",
            "armurier": "gère les armes du vaisseau",
            "cuisinier": "prépare les repas",
        }

        print(f"{self._role} : {self._first_name} {actions[self._role]}")

    def gain_experience(self):
        self._experience += 1
        print(
            f"{self._first_name} a gagné de l'expérience ! Niveau actuel : {self._experience}"
        )
