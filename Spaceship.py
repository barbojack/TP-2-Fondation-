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
        