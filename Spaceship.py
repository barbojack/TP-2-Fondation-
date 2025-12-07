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

    def append_member(self, member):
        if len(self._crew) >= 10:
            print(
                f"Impossible d'ajouter {member._first_name} : l'équipage du {self._name} est complet)."
            )
            return False
        else:
            self._crew.append(member)
            print(
                f"{member._first_name} a rejoint l'équipage du {self._name}. (Équipage: {len(self._crew)}/10)"
            )
            return True

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
