from Member import * 

class Mentalist(Member) :

    def __init__(self, first_name, last_name, gender, age, mana = 100):
        super().__init__(first_name, last_name, gender, age)
        self.mana = mana

    @property                           # Le @property permet de rendre privée l'information contenue
    def _mana(self):                    # Début du getter / setter
        return self.__mana

    @_mana.setter
    def _mana(self, value):
        self.__mana = value

    def get_mana(self):
        return self.mana

    def set_mana(self, value):
        self.mana = value

    @property                           
    def _mana(self):                    
        return self.__mana

    @_mana.setter
    def _mana(self, value):
        self.__mana = value             # Fin du getter / setter

    def act(self, operator) : 
        if self.mana >= 20:
            self.mana -= 20
            print(f"{self.name} utilise ses pouvoirs mentaux pour influencer {operator.name}. (Mana restant: {self.mana})")
            operator.act()
        else:
            print(f"{self.name} n'a pas assez de mana pour influencer {operator.name}. (Mana actuel: {self.mana})")

    def refill_mana(self) : 
        former_mana = self.mana
        self.mana = min(self.mana + 50, 100)
        gain = self.mana - former_mana
        print(f"{self.name} recharge son mana de {gain} points. (Mana actuel: {self.mana})")
