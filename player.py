from base import Creature

class Player(Creature):
    def __init__(self, id, title, max_hp):
        super().__init__(id, title, max_hp, 3)

        self.level = 1
        self.xp = 0
        self.require_xp = self.level * 10

    def set_xp(self, amount):
        self.xp += amount
        if (self.xp >= self.require_xp):
            remainder = self.xp - self.require_xp 

            self.xp = 0
            self.level_up()
            self.require_xp = self.level * 10

            self.set_xp(remainder)

    def level_up(self):
        print("╔═════════════════════╗")
        print("║ Повышение уровня!   ║")
        print("╚═════════════════════╝")
        self.level += 1
        self.max_hp += 10
        self.current_hp = self.max_hp


