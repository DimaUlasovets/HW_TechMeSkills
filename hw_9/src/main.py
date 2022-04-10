from app.gun import Gun
from app.ammo import Ammo, HEСartridge, HEATCartridge, APCartridge
from app.armour import Armour, HArmour, SArmour, CArmour
from app.tank import Tank


if __name__ == '__main__':

    gun_1 = Gun(105, 150)
    print('Попадание: ', gun_1.is_on_target())

    ammo_1 = HEСartridge(gun_1)
    print('Урон фугасный: ', ammo_1.get_demage())

    ammo_2 = HEATCartridge(gun_1)
    print('Урон кумулятивный: ', ammo_2.get_demage())

    ammo_3 = APCartridge(gun_1)
    print('Урон подкалиберный: ', ammo_3.get_demage())

    armor_1 = HArmour(100)
    print('Броня-1 пробита: ', armor_1.is_penetrated(ammo_2))

    armor_2 = SArmour(100)
    print('Броня-2 пробита: ', armor_2.is_penetrated(ammo_2))

    armor_3 = CArmour(100)
    print('Броня-3 пробита: ', armor_3.is_penetrated(ammo_2))

    test = Tank('T-34', gun_1, [armor_1, armor_2, armor_3], [ammo_1, ammo_2, ammo_3], 100)
