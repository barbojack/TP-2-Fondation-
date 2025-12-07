from Member import * 
from Operator import *
from Mentalist import *
from Spaceship import *
from Fleet import *

chris = Member("Chris", "Chevalier", "homme", 33)
print(chris._first_name)
charif = Operator("Charif", "El Bakkali", "homme", 19, "homme de ménage")
print(charif._role)
khalil = Operator("Khalil", "Serdoun", "homme", "19", "technicien")
paul = Mentalist("Paul", "VAN de WALLE", "homme", 19, 10000)
yoda = Operator("Yoda", "Maître", "homme", 100, "commandant")      
anakin = Operator("Anakin", "Skywalker", "homme", 26, "pilote")
luke = Mentalist("Luke", "Skywalker", "homme", 18, 100)
      
charif.act()

paul.act(charif)

star_destroyer = Spaceship("Star_Destroyer", "battle_ship")
hunter = Spaceship("Hunter", "battle_ship")

sith = Fleet("Sith", "Hunter")

star_destroyer.append_member(charif)
star_destroyer.append_member(chris)
star_destroyer.append_member(khalil)
star_destroyer.append_member(paul)
star_destroyer.append_member(yoda)
star_destroyer.append_member(anakin)


star_destroyer.check_preparation()
# print(star_destroyer._crew) n'affiche ce que je voudrais

paul.introduce_yourself()
luke.refill_mana()
khalil.gain_experience()

sith.statistics() # fonctionne pas

