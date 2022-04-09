import random


class Gun:

    def __init__(self, caliber: int, barrel_length: int) -> None:
        self._caliber = caliber
        self._barrel_length = barrel_length

    def is_on_target(self) -> bool:
        dice = random.uniform(0, 1)
        return True if self._barrel_length * dice > 100 else False


class Ammo:

    def __init__(self, gun: object, ammo_type: str) -> None:
        self._gun = gun
        self._ammo_type = ammo_type

    def get_demage(self) -> int:
        gun_caliber = getattr(self._gun, '_caliber')
        return int(gun_caliber * 3)

    def get_penetration(self) -> int:
        gun_caliber = getattr(self._gun, '_caliber')
        return gun_caliber


class HEСartridge(Ammo):

    def __init__(self, gun, ammo_type) -> None:
        super().__init__(gun, ammo_type)


class HEATCartridge(Ammo):

    def __init__(self, gun, ammo_type) -> None:
        super().__init__(gun, ammo_type)

    def get_demage(self) -> int:
        return super().get_demage() * 0.6


class APCartridge(Ammo):

    def __init__(self, gun, ammo_type) -> None:
        super().__init__(gun, ammo_type)

    def get_demage(self) -> int:
        return super().get_demage() * 0.3


class Armour:

    armour_type_ammo = {
        'фугасный': 1.2,
        'кумулятивный': 1,
        'подкалиберный': 0.7

    }

    def __init__(self, thickness: int, type_armour: str) -> None:
        self._thickness = thickness
        self._type_armour = type_armour

    def is_penetrated(self, ammo: object) -> bool():
        return True if getattr(ammo._gun, '_caliber') > self._thickness else False


class HArmour(Armour):

    def __init__(self, thickness: int, type_armour: str) -> None:
        super().__init__(thickness, type_armour)

    def is_penetrated(self, ammo: object) -> bool:
        return True if getattr(ammo._gun, '_caliber') > self._thickness * self.armour_type_ammo[getattr(ammo, '_ammo_type')] else False


if __name__ == '__main__':

    gun_1 = Gun(105, 150)
    print(gun_1.is_on_target())

    ammo_1 = HEСartridge(gun_1, 'фугасный')
    print(ammo_1.get_demage())

    ammo_2 = HEATCartridge(gun_1, 'кумулятивный')
    print(ammo_2.get_demage())

    armor_1 = HArmour(100, 'гомогенная')
    print(armor_1.is_penetrated(ammo_2))
