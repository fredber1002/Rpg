from base import Creature
from item import Weapon, Heal
from item import Item
from random import choice, randint
from item import Item, Weapon, Heal

class Player(Creature):
    def __init__(self, id, title, max_hp):
        super().__init__(id, title, max_hp, 3)
        
        self.level = 1
        self.xp = 0
        self.require_xp = self.level * 10
        
        self.inventory = []  
        self.current_weapon = None
        self.heal_items = []  
        
        self.add_starting_items()
    
    def add_starting_items(self):
        starter_weapon = Weapon("weapon_1", "Старый меч", 5, 3)
        self.add_to_inventory(starter_weapon)
        starter_weapon.use(self)

        small_heal = Heal("heal_1", "Малое зелье здоровья", 3, 10)
        self.add_to_inventory(small_heal)

        amulet = Item("item_1", "Старый амулет", 7)
        cup = Item("item_2", "Военный кубок", 5)
        self.add_to_inventory(amulet)
        self.add_to_inventory(cup)
    
    def add_to_inventory(self, item):
        self.inventory.append(item)

        if isinstance(item, Heal):
            self.heal_items.append(item)
        elif isinstance(item, Weapon):
            pass
    
    def get_inventory_value(self):
        total = 0
        for item in self.inventory:
            total += item.cost
        return total
    
    def show_inventory(self):
        print("\n" + "═" * 40)
        print("📦 ИНВЕНТАРЬ:")
        print("═" * 40)

        weapons = [item for item in self.inventory if isinstance(item, Weapon)]
        if weapons:
            print("🗡️  Оружие:")
            for weapon in weapons:
                current = " (Экипировано)" if weapon.damage == self.damage else ""
                print(f"  {weapon}{current}")

        if self.heal_items:
            print("\n❤️  Зелья здоровья:")
            for heal in self.heal_items:
                print(f"  {heal}")

        regular_items = [item for item in self.inventory 
                        if not isinstance(item, (Weapon, Heal))]
        if regular_items:
            print("\n🎁 Обычные предметы:")
            for item in regular_items:
                print(f"  {item}")
        
        print("═" * 40)
        print(f"💰 Общая ценность: {self.get_inventory_value()} очков")
        print("═" * 40)
    
    def use_heal(self):
        if not self.heal_items:
            print("╔══════════════════════════════════════════╗") 
            print("║ Нет зелий здоровья!                      ║")
            print("╚══════════════════════════════════════════╝")
        
            return False

        heal_item = self.heal_items.pop(0)
        heal_item.use(self)

        self.inventory.remove(heal_item)
        return True
    
    def find_random_item(self, enemy_title):

        if randint(1, 100) > 60:
            return None
        
        item_types = [
        ("Монета героя", 1),
        ("Искристый кристалл", 2),
        ("Древняя монета", 3),
        ("Серебряный амулет", 5),
        ("Золотое кольцо мудрости", 8)
        ]

        
        title, cost = choice(item_types)
        item = Item(f"loot_{randint(1000, 9999)}", title, cost)
        
        print(f"╔══════════════════════════════════════════╗")
        print(f"║ Найдено у {enemy_title}: {item.title}    ║")
        print(f"║ Ценность: {item.cost} очков              ║")
        print(f"╚══════════════════════════════════════════╝")
        
        self.add_to_inventory(item)
        return item
    
    def set_xp(self, amount):
        self.xp += amount
        if (self.xp >= self.require_xp):
            remainder = self.xp - self.require_xp 

            self.xp = 0
            self.level_up()
            self.require_xp = self.level * 10

            self.set_xp(remainder)

    def level_up(self):
        print(" ╔══════════════════════════════════════════╗")
        print(" ║ Повышение уровня!                        ║")
        print(" ╠══════════════════════════════════════════╣")
        print(f"║ Новый уровень: {self.level + 1}          ║")
        print(" ╚══════════════════════════════════════════╝")
        self.level += 1
        self.max_hp += 10
        self.current_hp = self.max_hp