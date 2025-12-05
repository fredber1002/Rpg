from enemy import Enemy
from player import Player
from random import shuffle, randint
from item import Weapon, Heal

def generate_objects():
    enemies = []

    enemy1 = Enemy("enemy_1", "Афреканец", 7, 2, 4)
    enemy2 = Enemy("enemy_2", "Чурка", 14, 4, 9)
    enemy3 = Enemy("enemy_3", "Трампа", 5, 2, 3)
    enemy4 = Enemy("enemy_4", "Огр", 16, 5, 20)
    enemy5 = Enemy("enemy5", "Путин", 100, 25, 10)

    enemies.append(enemy1)
    enemies.append(enemy2)
    enemies.append(enemy3)
    enemies.append(enemy4)
    enemies.append(enemy5)

    player = Player("player", "Игрок", 25)
    shuffle(enemies)

    object = {
        "player": player,
        "enemies": enemies
    }
    
    return object

def show_game_menu():
    print("╔════════════════════════════════════════════════╗")
    print("║                  Ваши действия                 ║")
    print("╠════════════════════════════════════════════════╣")
    print("║ 1. Атака                                       ║")
    print("║ 2. Защита                                      ║")
    print("║ 3. Убежать                                     ║")
    print("║ 4. Использовать зелье здоровья                 ║")
    print("║ 5. Показать инвентарь                          ║")
    print("╚════════════════════════════════════════════════╝")

def handle_enemy_loot(player, enemy):
    player.find_random_item(enemy.title)
    if enemy.cost_xp >= 10 and randint(1, 100) <= 20:
        weapons = [
            Weapon("weapon_drop1", "Кинжал разбойника", 15, 5),
            Weapon("weapon_drop2", "Топор воина", 20, 7),
            Weapon("weapon_drop3", "Меч паладина", 25, 9)
        ]
        weapon = weapons[randint(0, len(weapons)-1)]
        
        print(f"╔════════════════════════════════════════════╗")
        print(f"║ {enemy.title} выронил {weapon.title}!       ║")
        print(f"║ Урон: {weapon.damage} | Ценность: {weapon.cost} ║")
        print(f"╚════════════════════════════════════════════╝")
        
        player.add_to_inventory(weapon)

    elif randint(1, 100) <= 30:
        heals = [
            Heal("heal_drop1", "Малое зелье", 5, 8),
            Heal("heal_drop2", "Среднее зелье", 8, 15),
            Heal("heal_drop3", "Большое зелье", 12, 25)
        ]
        heal_item = heals[randint(0, len(heals)-1)]
        
        print(f"╔════════════════════════════════════════════╗")
        print(f"║ Найдено у {enemy.title}: {heal_item.title}  ║")
        print(f"║ Лечение: +{heal_item.heal_amount} HP          ║")
        print(f"╚════════════════════════════════════════════╝")
        
        player.add_to_inventory(heal_item)

object = generate_objects()
enemy_alive = False

print("╔════════════════════════════════════════════════╗")
print("║                 ★ Добро пожаловать ★           ║")
print("║               Вы заходите в белый дом         ║")
print("╚════════════════════════════════════════════════╝\n")

while True:
    if not enemy_alive:
        if len(object["enemies"]) == 0:
            print("╔════════════════════════╗")
            print("║ Враги закончились!     ║")
            print("╚════════════════════════╝")
            break 
        
        enemy = object["enemies"].pop()
        print("╔══════════════════════════════════════╗")
        print(f"║ Вы встретили {enemy.title}!                  ║")
        enemy_alive = True
    
    print(f"╔══════════════════════════════════════╗")
    print(f"║ У {enemy.title} осталось {enemy.current_hp} ХП             ║")
    print(f"║ У вас осталось {object['player'].current_hp} ХП из {object['player'].max_hp}           ║")
    print("║                                      ║")
    print("║ Уровень: {} | Опыт: {}/{}           ║".format(
        object['player'].level, 
        object['player'].xp, 
        object['player'].require_xp
    ))
    print("║ Урон: {} | Оружие: {}     ║".format(
        object['player'].damage,
        object['player'].current_weapon.title if object['player'].current_weapon else "Нет"
    ))
    print("╚══════════════════════════════════════╝")
    
    show_game_menu()
    nubmer_action = input("Введите цифру действия: ")
    
    while nubmer_action not in ["1", "2", "3", "4", "5"]:
        print("Некоректное действие!")
        show_game_menu()
        nubmer_action = input("Введите цифру действия: ")

    if nubmer_action == "1":
        print("╔══════════════════════════════════════════╗")
        print(f"║ Атакуем {enemy.title}!                  ║")
        print(f"║ Снято ХП {object['player'].damage}      ║")
        print("╚══════════════════════════════════════════╝")

        result = enemy.deal_damage(object["player"].damage)

        if result: 
            enemy_alive = False
            object["player"].set_xp(enemy.cost_xp)
            handle_enemy_loot(object["player"], enemy)
        else:
            print("╔══════════════════════════════════════════╗")
            print(f"║ Нас атакует {enemy.title}!              ║")
            print(f"║ Снято ХП {enemy.damage}                 ║")
            print("╚══════════════════════════════════════════╝")
            object["player"].deal_damage(enemy.damage)

    elif nubmer_action == "2":
        print("╔══════════════════════════════════════════╗")
        print("║ Защищаемся                               ║")
        print(f"║ Нас атакует {enemy.title}               ║")
        print(f"║  Сработала защита, было снято: {round(enemy.damage / 2)}    ║")
        print("╚══════════════════════════════════════════╝")

        object["player"].deal_damage(round(enemy.damage / 2))

    elif nubmer_action == "3":
        print("╔══════════════════════════════════════════╗")
        print("║ Вы сбежали                               ║")
        print(f"║ Вас атаковал {enemy.title}, но вы успешно убежали! ║")
        print("╚══════════════════════════════════════════╝")
        enemy_alive = False  
        continue

    elif nubmer_action == "4":
        object["player"].use_heal()

    elif nubmer_action == "5":
        object["player"].show_inventory()
        continue 

    if object["player"].dead:
        print("╔══════════════════════════════════════════╗")
        print("║              Вы погибли                  ║")
        print("╚══════════════════════════════════════════╝")
        break
    
    if len(object["enemies"]) == 0 and not enemy_alive:
        print("╔════════════════════════════════════════════════╗")
        print("║          ★ Поздравляем! Все враги побеждены ★  ║")
        print("╠════════════════════════════════════════════════╣")
        
        player = object["player"]
        total_value = player.get_inventory_value()
        
        print(f"║ Уровень: {player.level}                              ║")
        print(f"║ Здоровье: {player.current_hp}/{player.max_hp}                      ║")
        print(f"║ Количество предметов: {len(player.inventory)}                      ║")
        print(f"║ Общая ценность инвентаря: {total_value} очков           ║")
        print("╚════════════════════════════════════════════════╝")

        player.show_inventory()
        break
