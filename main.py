from Member import * 
from Operator import *
from Mentalist import *
from Spaceship import *
from Fleet import *

chris = Member("Chris", "Chevalier", "homme", 33)
print(chris._first_name)
charif = Operator("Charif", "El Bakkali", "homme", 19, "homme de ménage")
print(charif._role)

      
charif.act()

paul = Mentalist("Paul", "Van", "homme", 19, 1000000000000000000000)
