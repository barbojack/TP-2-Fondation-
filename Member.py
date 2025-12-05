class Member : 

    def __init__(self, first_name, last_name, gender, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__age = int(age)

    @property                                       # Le @property permet de rendre privées les informations
    def _first_name(self):                          # Début de la liste des getters / setters
        return self.__first_name

    @_first_name.setter
    def _first_name(self, value):
        self.__first_name = value

    @property
    def _last_name(self):
        return self.__last_name

    @_last_name.setter
    def _last_name(self, value):
        self.__last_name = value

    @property
    def _gender(self):
        return self.__gender

    @_gender.setter
    def _gender(self, value):
        self.__gender = value

    @property
    def _age(self):
        return self.__age

    @_age.setter
    def _age(self, value):
        self.__age = value                          # Fin de la liste des getters / setters
        
    def introduce_yourself(self) : 
        print("Je m'appelle", self.__first_name, self.__last_name, "je suis", self.__gender, "de", self.__age, "ans.")
