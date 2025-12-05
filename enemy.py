from base import Creature

class Enemy(Creature):
    def __init__(self, id, title, max_hp, damage, cost_xp):
        super().__init__(id, title, max_hp, damage)

        self.cost_xp = cost_xp