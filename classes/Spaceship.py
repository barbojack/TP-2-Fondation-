from classes.Member import *
from classes.Operator import *
from classes.Mentalist import *

class Spaceship:

    def __init__(self, name, shipType):
        self.__name = name
        self.__shipType = shipType
        self.__condition = "opérationnel"
        self.__crew = []

    @property  # @property permet de mettre en privée les informations
    def _name(self):  # Début des getters / setters
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _shipType(self):
        return self.__shipType

    @_shipType.setter
    def _shipType(self, value):
        self.__shipType = value

    @property
    def _condition(self):
        return self.__condition

    @_condition.setter
    def _condition(self, value):
        self.__condition = value

    @property
    def _crew(self):
        return self.__crew

    @_crew.setter
    def _crew(self, value):
        self.__crew = value  # Fin des getters / setters
        
    # Fonction permettant d'ajouter un membre à l'équipage

    def append_member(self, member):
        if not isinstance(member, (Operator, Mentalist)):
            print(f"Impossible d'ajouter ce membre : il doit être de type Operator ou Mentalist.")
            return False
        if len(self._crew) >= 10:
            try:
                member_name = member._first_name
            except AttributeError:
                member_name = "ce membre"
            print(
                f"Impossible d'ajouter {member_name} : l'équipage du {self._name} est complet (10/10))."
            )
            return False
        else:
            self._crew.append(member)
            try:
                member_name = member._first_name
            except AttributeError:
                member_name = "Nouveau membre"
            print(
                f"{member_name} a rejoint l'équipage du {self._name}. (Équipage: {len(self._crew)}/10)"
            )
            return True

    # Fonction permettant de retirer un membre de l'équipage 

    def remove_member(self, lastname: str)->bool:               # Recherche un membre de l'équipage par son nom de famille et le retire s'il est trouvé.
        member_to_remove = None
        for member in self._crew:
            try:
                if member._last_name.lower() == lastname.lower():
                    member_to_remove = member
                    break                                       # Arrête la boucle si un membre est trouvé
            except AttributeError:                              # Gère le cas où un objet dans la liste n'aurait pas l'attribut _last_name
                continue
        if member_to_remove:
            self._crew.remove(member_to_remove)
            try:
                first_name = member_to_remove._first_name
            except AttributeError:                  
                first_name = ""
            print(f"{first_name} {lastname} a été retiré de l'équipage du {self._name}. (Equipage: {len(self._crew)}/10)")
            return True
        else:
            print(f"Erreur : Le membre avec le nom de famille '{lastname}' n'a pas été trouvé dans l'équipage du {self._name}.")
            return False 

    # Fonction permettant de vérifier si l'équipage possède un pilote et un technicien pour décoller

    def check_preparation(self):
        
        has_pilot = False
        has_technician = False
        
        for member in self._crew:
            try:
                if member._role.lower() == "pilote":
                    has_pilot = True
                elif member._role.lower() == "technicien":
                    has_technician = True
            except AttributeError:
                pass  # Le membre n'a pas d'attribut 'role', on ignore

        if has_pilot and has_technician:
            print("Le vaisseau est prêt au décollage !")
            return True
        else:
            print("Il manque un pilote ou un technicien dans le vaisseau. Impossible de décoller !")
            return False


    def display_crew(self):
        print(f"\n--- Equipage du Vaisseau {self._name} (c'est un {self._shipType}) ---\n")
        if not self._crew:
            print("L'équipage est vide.")
            return
        for member in self._crew:
            try:
                member.introduce_yourself()
            except AttributeError:
                print(f"Erreur d'affichage : Le membre '{member._first_name}' ne possède pas de méthode d'affichage.")