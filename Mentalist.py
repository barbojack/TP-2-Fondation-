from Member import *


class Mentalist(Member):

    def __init__(self, first_name, last_name, gender, age, mana=100):
        super().__init__(first_name, last_name, gender, age)
        self.__mana = mana

    @property  # @property permet de mettre les informations en privées
    def _mana(self):  # début du getter / setter
        return self.__mana

    @_mana.setter
    def _mana(self, value):
        self.__mana = value  # Fin du getter / setter

    def act(self, operator):
        if self._mana >= 20:
            self._mana -= 20
            print(
                f"{self._first_name} utilise ses pouvoirs mentaux pour influencer {operator._first_name}. (Mana restant: {self._mana})"
            )
            operator.act()
        else:
            print(
                f"{self._first_name} n'a pas assez de mana pour influencer {operator._first_name}. (Mana actuel: {self._mana})"
            )

    def refill_mana(self):
        former_mana = self._mana
        self._mana = min(self._mana + 50, 100)
        gain = self._mana - former_mana
        print(
            f"{self._first_name} recharge son mana de {gain} points. (Mana actuel: {self._mana})"
        )
