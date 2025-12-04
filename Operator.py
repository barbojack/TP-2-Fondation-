from Member import * 

class Operator(Member) :

    def __init__(self, role, experience):
        self.__role = role
        self.__experience = 0

    @property
    def _role(self):
        return self.__role

    @_role.setter
    def _role(self, value):
        self.__role = value

    @property
    def _experience(self):
        return self.__experience

    @_experience.setter
    def _experience(self, value):
        self.__experience = value

    def act(self) :      # affiche le message pour chaque rôle
        actions = { 
            "technicien" : "Répare les sytèmes du vaisseau",
            "pilote" : "Pilote le vaisseau",
            "commandant" : "Dirige les membres du vaisseau",
            "armurier" : "Gère les armes du vaisseau",
            "cuisinier" : "Prépare les repas",
            "entretien" : "Nettoie le vaisseau"
        }

    def gain_experience(self) :
        self.experience += 1
        print(f"{self.name} a gagné de l'expérience ! Niveau actuel : {self.experience}")
        
    def display_info(self) :      # permet de voir les informations de la personne 
        super().display_info()
        print(f"Rôle: {self.role}, Expérience: {self.experience}")