from base import Object

class Item(Object):
    def __init__(self, id, title, cost):
        super().__init__(id, title)
        self.cost = cost  
        self.usable = False 
    
    def use(self, target=None):
        print(f"Предмет {self.title} не имеет эффект.")
        return False
    
    def __str__(self):
        return f"{self.title} (Ценность: {self.cost})"

class Weapon(Item):
    def __init__(self, id, title, cost, damage):
        super().__init__(id, title, cost)
        self.damage = damage
        self.usable = True
    
    def use(self, target=None):
        if hasattr(target, 'damage'):
            old_damage = target.damage
            target.damage = self.damage
            print(f"╔════════════════════════════════╗")
            print(f"║ Оружие {self.title} экипировано! ║")
            print(f"║ Урон увеличен: {old_damage} → {self.damage} ║")
            print(f"╚════════════════════════════════╝")
            return True
        return False
    
    def __str__(self):
        return f"{self.title} (Урон: {self.damage}, Ценность: {self.cost})"

class Heal(Item):
    def __init__(self, id, title, cost, heal_amount):
        super().__init__(id, title, cost)
        self.heal_amount = heal_amount
        self.usable = True
    
    def use(self, target=None):
        if hasattr(target, 'current_hp') and hasattr(target, 'max_hp'):
            old_hp = target.current_hp
            target.current_hp = min(target.current_hp + self.heal_amount, target.max_hp)
            actual_heal = target.current_hp - old_hp
            
            print(f"╔════════════════════════════════╗")
            print(f"║ Использовано: {self.title}      ║")
            print(f"║ Восстановлено: {actual_heal} HP ║")
            print(f"║ Текущее HP: {target.current_hp}/{target.max_hp} ║")
            print(f"╚════════════════════════════════╝")
            return True
        return False
    
    def __str__(self):
        return f"{self.title} (+{self.heal_amount} HP, Ценность: {self.cost})"