from Member import * 

class Mentalist(Member) :

    def __init__(self, mana):
        self.__mana = 100

    @property
    def _mana(self):
        return self.__mana

    @_mana.setter
    def _mana(self, value):
        self.__mana = value
        
    def act(self, operator) : 
        if self.mana >= 20:
            self.mana -= 20
            print(f"{self.name} utilise ses pouvoirs mentaux pour influencer {operator.name}. (Mana restant: {self.mana})")
            operator.act()
        else:
            print(f"{self.name} n'a pas assez de mana pour influencer {operator.name}. (Mana actuel: {self.mana})")
            
    def recharge_mana(self) : 
        ancien_mana = self.mana
        self.mana = min(self.mana + 50, 100)
        gain = self.mana - ancien_mana
        print(f"{self.name} recharge son mana de {gain} points. (Mana actuel: {self.mana})")
        
    def display_info(self) :
        super().display_info()
        print(f"Mana: {self.mana}")