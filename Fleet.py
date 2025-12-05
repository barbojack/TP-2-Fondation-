class Fleet :

    def __init__(self, name, spaceships):
        self.__name = name
        self.__Spaceship = []

    @property                               # Début de la liste des getters : setters
    def _name(self):                        # Le @property est dû au double (__) pour rendre privées les informations
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _Spaceship(self):
        return self.__Spaceship

    @_Spaceship.setter
    def _Spaceship(self, value):
        self.__Spaceship = value            # Fin de la liste des getters / setters


    def append_spaceship(self, Spaceship) :
        if len(self.Spaceship) == 15 :
            print(f"La flotte {self.name} a atteint sa capacité maximale de 15 vaisseaux !!!")
            return False 
        self.spaceships.append(Spaceship)
        print(f"Le vaisseau {self.name} a été ajouté à la flotte. La flotte est composée de {len(self.Spaceship)}/15")
        return True 
    
    def statistics(self) :
        