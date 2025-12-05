class Spaceship :

    def __init__(self, name, shipType, condition, crew):
        self.__name = name
        self.__shipType = shipType
        self.__condition = condition
        self.__crew = []

    @property                                   # Le @property permet de rendre privées les informations
    def _name(self):                            # Début des getters / setters
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
        self.__crew = value                     # Fin des getters / setters

    def append_member(self, member) :
        if len(self.crew) >= 10 :
            print(f"Impossible d'ajouter {member.name} : l'équipage du {self.name} est complet).")
            return False 
        else :
            self.crew.append(member)
            print(f"{member.name} a rejoint l'équipage du {self.name}. (Équipage: {len(self.crew)}/10)")
            return True

    def check_preparation(self):
        has_pilot = False
        has_technician = False

        for member in self.crew:
            try:
                if member.role.lower() == "pilote":
                    has_pilot = True
                elif member.role.lower() == "technicien":
                    has_technician = True
            except AttributeError:
                pass                                                    # Le membre n'a pas d'attribut 'role', on ignore

        return has_pilot and has_technician
