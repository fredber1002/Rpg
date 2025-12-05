set_id = set()

class Object:
    def __init__(self, id, title):
        if id in set_id:
            raise ValueError("Уже существует данное id: ", id)
        self.id = id
        set_id.add(id)

        self.title = title
        
class Creature(Object):
    def __init__(self, id, title, max_hp, damage=2):
        super().__init__(id, title)

        self.damage = damage
            
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.dead = False

    def deal_damage(self, amount):
        if self.dead:
            return True
        
        self.current_hp -= amount

        if self.current_hp <= 0:
            self.death()
            return True
        else:
            return False

    def death(self):
        self.dead = True
        print("╔" + "═" * 40 + "╗")
        print(f"║ 💀  {self.title} умер...".ljust(40) + "║")
        print("╚" + "═" * 40 + "╝")

        

        


