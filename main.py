from Member import * 
from Operator import *
from Mentalist import *
from Spaceship import *
from Fleet import *

chris = Operator("Chris", "Chevalier", "homme", 33, "armurier")
print(chris._first_name)
charif = Operator("Charif", "El Bakkali", "homme", 19, "homme de ménage")
print(charif._role)

khalil = Operator("Khalil", "Serdoun", "homme", "19", "technicien")
paul = Mentalist("Paul", "VAN de WALLE", "homme", 19, 10000)
yoda = Operator("Yoda", "Maître", "homme", 100, "commandant")      
anakin = Operator("Anakin", "Skywalker", "homme", 26, "pilote")
luke = Mentalist("Luke", "Skywalker", "homme", 18, 100)
obiwan = Mentalist("Obi-Wan", "Kenobi", "homme", 30, 100)
r2d2 = Operator("R2D2", "Droide", "homme", 20, "technicien")
poe = Operator("Poe", "Dameron", "homme", 30, "pilote")
leia = Operator("Leia", "Skywalker", "femme", 18, "pilote")
c3pO = Operator("C3PO", "Droide", "homme", 30, "technicien")
sidious = Mentalist("Dark", "Sidious", "homme", 50, 100)
trooper = Operator("Trooper", "Ang", "homme", 25, "technicien")

charif.act()

paul.act(charif)

star_destroyer = Spaceship("Star_Destroyer", "battle_ship")
hunter = Spaceship("Hunter", "battle_ship")
amiral = Spaceship("Amiral", "Amiral")
x_wing = Spaceship("X-Wing", "battle_ship")

# sith = Fleet("Sith", [])      # On a besoin des [] car c'est une liste de vaisseaux dans la flotte

sith = Fleet ("Sith", [])
republic = Fleet("Republic", [])

# Ajout des vaisseaux dans la flotte

sith.append_spaceship(star_destroyer)
sith.append_spaceship(hunter)
republic.append_spaceship(amiral)
republic.append_spaceship(x_wing)


# Ajout de membres dans le vaisseau Star_Destroyer

star_destroyer.append_member(charif)
star_destroyer.append_member(chris)
star_destroyer.append_member(khalil)
star_destroyer.append_member(paul)
star_destroyer.append_member(anakin)

amiral.append_member(yoda)
amiral.append_member(leia)
amiral.append_member(c3pO)
amiral.append_member(obiwan)
amiral.append_member(luke)

x_wing.append_member(poe)
x_wing.append_member(r2d2)

# Ajout de membres dans le vaisseau Hunter

hunter.append_member(sidious)
hunter.append_member(trooper)
hunter.append_member(anakin)

# Vérification de la préparation du vaisseau Star Destroyer

star_destroyer.check_preparation()
hunter.check_preparation()

# Test des classes 

paul.introduce_yourself()
luke.refill_mana()
khalil.gain_experience()

sith.statistics() 
republic.statistics()               # les mentalists ne sont pas afficher dans la répartition des rôles

