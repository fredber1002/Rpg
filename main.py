from enemy import Enemy
from player import Player
from random import shuffle

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

object = generate_objects()
enemy_alive = False
print("★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★")
print("☆ Вы заходите в белый дом... ★")
print("★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★")
while True:
    if not enemy_alive:
     if len(object["enemies"]) == 0:
        print("╔════════════════════════╗")
        print("║ Враги закончились!     ║")
        print("╚════════════════════════╝")
        break 
    enemy = object["enemies"].pop()
    print("╔══════════════════════════════════════╗")
    print(f"║ Вы встретили {enemy.title}!              ║")
    enemy_alive = True
    print(f"║ У {enemy.title} осталось {enemy.current_hp} ХП            ║")
    print(f"║ У вас осталось {object["player"].current_hp} ХП из {object["player"].max_hp}           ║")
    print("║                                      ║")
    print("║ Ваши действия:                       ║")
    print("║ 1. Атака                             ║")
    print("║ 2. Защита                            ║")
    print("║ 3. Убежать                           ║")
    print("╚══════════════════════════════════════╝")
    nubmer_action = input("Введите цифру действия: ")
    
    while nubmer_action not in ["1", "2", "3"]:
        print("Некоректоное действие!")
        print("╔══════════════════════════════════════╗")
        print("║ Ваши действия:                       ║")
        print("║ 1. Атака                             ║")
        print("║ 2. Защита                            ║")
        print("║ 3. Убежать                           ║")
        print("╚══════════════════════════════════════╝")
        nubmer_action = input("Введите цифру действия: ")

    if nubmer_action == "1":
        print("╔══════════════════════════╗")
        print(f"║ Атакуем {enemy.title}!         ║")
        print(f"║ Снято ХП {object['player'].damage}         ║")
        print("╚══════════════════════════╝")

        result = enemy.deal_damage(object["player"].damage)

        if result: 
            enemy_alive = False
            object["player"].set_xp(enemy.cost_xp)
        else:
            print("╔══════════════════════════╗")
            print(f"║ Нас атакует {enemy.title}!         ║")
            print(f"║ Снято ХП {enemy.damage}               ║")
            print("╚══════════════════════════╝")
            object["player"].deal_damage(enemy.damage)

    elif nubmer_action == "2":
        print("╔══════════════════╗")
        print("║ Защищаемся        ║")
        print(f"║ Нас атакует {enemy.title}     ║")
        print(f"║  Сработала защита, было снято: {round(enemy.damage / 2)}    ║")
        print("╚══════════════════╝")

        object["player"].deal_damage(round(enemy.damage / 2))

    elif nubmer_action == "3":
        print("╔════════════════════════════════════════════╗")
        print("║ Вы сбежали                                 ║")
        print(f"║ Вас атаковал {enemy.title}, но вы успешно убежали! ║")
        print("╚════════════════════════════════════════════╝")
        enemy_alive = False  
        continue  

    if object["player"].dead:
        print("╔════════════════╗")
        print("║ Вы погибли     ║")
        print("╚════════════════╝")
        break
    
    if len(object["enemies"]) == 0 and enemy_alive:
        print("╔════════════════════════╗")
        print("║ Вы всех победили!       ║")
        print("╚════════════════════════╝")
        break