from Operator import *
from Mentalist import *

class Spaceship :
    def __init__(self, name, ship_type, condition) : 
        self.name = name
        self.ship_type = ship_type
        self.condition = condition
        self.crew = []
    
    def append_member(self, member) :
        if len(self.crew) >= 10 :
            print(f"Impossible d'ajouter {member.name} : l'équipage du {self.name} est complet).")
            return False 
        else :
            self.crew.append(member)
            print(f"{member.name} a rejoint l'équipage du {self.name}. (Équipage: {len(self.crew)}/10)")
            return True
        
    def check_preparation(self) :
        has_pilot = False
        has_technician = False
        
        for member in self.crew:
            if isinstance(member, Operator):                        # isinstance permet de vérifier le type exact d'un objet 
                if member.role.lower() == "pilote":                 # lower permet de tous mettre en minuscule 
                    has_pilot = True
                elif member.role.lower() == "technicien":
                    has_technician = True
        
        return has_pilot and has_technician
    
    def display_info(self):
        print(f"\n=== Vaisseau: {self.name} ===")
        print(f"Type: {self.ship_type}")
        print(f"Condition: {self.condition}")
        print(f"Équipage: {len(self.crew)}/{10} membres")
        
        if self.crew:
            print("\nMembres d'équipage:")
            for i, member in enumerate(self.crew, 1):
                if isinstance(member, Operator):                                                            # isinstance permet de vérifier le type exact d'un objet 
                    print(f"  {i}. {member.name} - {member.role} (expérience: {member.experience})")
                elif isinstance(member, Mentalist):                                                         # # isinstance permet de vérifier le type exact d'un objet 
                    print(f"  {i}. {member.name} - Mentaliste (mana: {member.mana})")
                else:
                    print(f"  {i}. {member.name} - Membre")
        
        preparation = self.check_preparation()
        print(f"\nPrêt au départ: {'Oui' if preparation else 'Non'}")
        if not preparation:
            has_pilot = any(isinstance(m, Operator) and m.role.lower() == "pilote" for m in self.crew)          # isinstance permet de vérifier le type exact d'un objet 
            has_tech = any(isinstance(m, Operator) and m.role.lower() == "technicien" for m in self.crew)          # isinstance permet de vérifier le type exact d'un objet 
            if not has_pilot:
                print("Il manque un pilote")
            if not has_tech:
                print("Il manque un technicien")