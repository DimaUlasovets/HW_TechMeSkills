from functools import reduce
import time


class Engine:

    motor_accelerat_factor = {
        'v6': 0.2,
        'v8': 0.4,
        'v10': 0.6
    }

    def __init__(self, motor_type: str, strength: int, turbine: bool) -> None:
        self.motor_type = motor_type
        self.accelerat_factor = self.motor_accelerat_factor[self.motor_type]
        self.strength = strength
        self.turbine = turbine

    def generate_power(self) -> float:
        return self.strength * self.accelerat_factor if self.turbine else (
            self.strength * self.accelerat_factor) / 0.8


class Wheel:
    wheel_stat = {
        16: 20,
        17: 22,
        18: 24,
        19: 26,
        20: 28,
        21: 30,
        22: 32,
    }

    def __init__(self, diameter: int) -> None:
        self.diameter = diameter
        self.weight = self.wheel_stat[self.diameter]

        if diameter not in [el for el in range(16, 22)]:  # хз, правильно ли так делать, но я не нашел четкого ответа в интернетах этих ваших
            print("Sorry, we don't have that wheel size")
            self.diameter = 16


class Car:

    type_and_width_car = {
        'jeep': 1500,
        'passenger_car': 1200,
        'cargo': 1800
    }

    def __init__(self, motor, wheels: list, type_car: str) -> None:
        self.motor = motor
        self.wheels = wheels
        self.type_car = type_car

        if len(wheels) < 4:
            raise NameError('the car must have at least 4 wheels')

    def start_engine(self, start_status=False):
        return start_status

    def move(self, distance: float, motor) -> None:
        if self.start_engine:
            wheel_weight = reduce(lambda x, y: x + getattr(y, 'weight'), self.wheels, 0)
            res = (self.type_and_width_car[self.type_car] + wheel_weight) / self.motor.generate_power() * distance
            return res
        else:
            raise NameError('motor not running')


def car_race():

    while True:
        print("\n---------------------------------------"
              "\nHello, you are in the car race game !\n")
        print("[0] - start game\n"
              "[/q] - quite the game\n")

        user_input_menu_1 = input('Choose the menu option: ')

        if user_input_menu_1 == '/q':
            break

        elif user_input_menu_1 == '0':

            while True:

                print("\n[0] - create car\n"
                        "[1] - start race\n"
                        "[2] - restart race\n"
                        "[/q] - quite to main menu\n")


                user_input_menu_2 = input('Choose the menu option: ')

                if user_input_menu_2 == '/q':
                    break

                elif user_input_menu_2 == '0':
                    
                    count_of_players = int(input('Ok, input count of players: '))
                    
                    if count_of_players > 0:

                        car_distanse = int(input('Choose car distanse: '))

                        if car_distanse > 0:
                            
                            user_car = {}

                            for user in range(count_of_players):

                                print(f'\nPlayer_{user}')

                                motor_t = input('chose motor type [v6, v8, v10]: ')

                                if motor_t in ('v6', 'v8', 'v10'):

                                    strength = int(input('select strength of motor (1-300): '))

                                    if strength > 0 and strength <= 300:

                                        turbin = bool(input('select Turbin status (True/ False): '))

                                        if turbin in (True, False):

                                            motor = Engine(motor_t, strength, turbin)
                                            wheel_diametr = int(input('chose wheel diametr [16-22]: '))

                                            if wheel_diametr >= 16 and wheel_diametr <= 22:

                                                wheel_stat = Wheel(wheel_diametr)
                                                type_of_car = input('chose type of you car [jeep, passenger_car, cargo]: ')

                                                if type_of_car in ('jeep', 'passenger_car', 'cargo'):
                                                    car_stat = Car(motor, [wheel_stat for el in range(4)], type_of_car)
                                                    car_stat.start_engine(True)
                                                    user_car[f'user_{user}'] = car_stat.move(car_distanse, motor)         
                                                
                                                else:
                                                    print('type of you car must be like [jeep, passenger_car, cargo]')
                                            
                                            else:
                                                print('diametr of wheel must me (16-22)')

                                        else:
                                            print('turbine status must be (True or False)')

                                    else:
                                        print('strength of motor must be (1-300)')
                                
                                else:
                                    print('sorry, you should choose motor type like this: [v6, v8, v10]')
                        
                        
                        else:
                            print('\nsorry, car distanse must be > 0')
                        
                    else:
                        print('\nsorry, count of players must be > 0')

                elif user_input_menu_2 == '1' or user_input_menu_2 == '2':

                    if len(user_car):

                        for el in range(6, 0, -1):
                            print(el)
                            time.sleep(1)

                        print(f"\n{user_car}")

                    else:
                        print('\n------------You should create a car---------------')

                else:
                    print('Chose menu option pls')     
        else:
            print('\n----------Chose menu option pls-------------')


if __name__ == '__main__':

    # motor_v6 = Engine('v6', 100, True)
    # wheel = Wheel(16)
    # car = Car(motor_v6, [wheel for el in range(4)], 'jeep')
    
    # car.start_engine(True)
    # car.move(100, 'v6')

    car_race()