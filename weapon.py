from random import randint

class Item:
    def __init__(self, title, cost):
        self.title = title
        self.cost = cost


class Weapon(Item):
    def __init__(self, title, cost, damage):
        super().__init__(title, cost)
        self.damage = damage


class Heal(Item):
    def __init__(self, title, cost, heal_amount):
        super().__init__(title, cost)
        self.heal_amount = heal_amount


item = {
    "small_heal": Heal("Малое зелье лечения", 5, 5),
    "big_heal": Heal("Большое зелье лечения", 12, 15),
    "rusty_sword": Weapon("Ржавый меч", 8, 3),
    "iron_sword": Weapon("Железный меч", 18, 6),
    "golden_ring": Item("Золотое кольцо", 10),
    "diamond": Item("Алмаз", 50)
}
