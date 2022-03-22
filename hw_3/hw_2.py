import random
from datetime import datetime

# Homework 3 - task(1,2,3)
def task_2_and_3_in_one():
    menu_information = (
        '\n(1) - Start "find number game"\n'
        '(2) - Start "examination your age"\n'
        '(0) - Exit while loop\n')


    while True:
        print(menu_information)
        user_input = int(input('Input number of option: '))
        
        if user_input == 1:
            print("Hello lets play the game!!!!!\nYou have to guess the number,\nnumber between 0 and 100\n")
            random_number = random.randint(0, 100)
            
            while True:
                user_number_input = int(input('Write the number: '))
                if user_number_input != random_number and user_number_input < random_number:
                    print('try again, your number is (LESS) than the given one\n')
                elif user_number_input != random_number and user_number_input > random_number:
                    print('try again, your number is (GREATER) than the given one\n')
                else:
                    print(f'Congratulations you guessed it.\nYour number = {user_number_input} == {random_number}')
                    break

        elif user_input == 2:

            user_name = input('Write your name pls: ')
            user_age = int(input('Write your age pls: '))
            
            if user_age > 18:
                print(f'Hello, {user_name}!! Сongratulations, you can buy some beer')
            else:
                print('Sorry, not today')

        elif user_input == 0:
            print('\nGoodbuy!')
            break

        else:
            print('\n!!!!!!! Something went wrong check your input !!!!!!!')


# Homework 4 - task(1,2)
def list_comprehation(start_num:int, stop_num:int) -> list:
    return print([el for el in range(start_num, stop_num)])

# Homework 4 - task(3)
def get_time_now():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return print(current_time)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Additional task - task(1) (homework 2)
def number_check_pos_neg_zero():
    user_input_number = int(input('Enter a number: '))

    if user_input_number == 0:
        print('Zero')
    elif user_input_number < 0:
        print('Negative number')
    else:
        print('Positive number')


# Additional task - task(2) (homework 2)
def price_of_sandwich(name_sandwich:str):
    menu = {
        'Ham Roll': '$1.75',
        'Cheese Roll': '$1.80',
        'Bacon Roll': '$2.10',
        'Other Filled Roll': '$2.00',
    }
    
    if name_sandwich in menu:
        return print(name_sandwich, menu[name_sandwich])
    else:
        print('Ew dont have this sandwich')



# Additional task LOOOPS - task(1,2) (homework 2)
def sort_loop():
    my_list = random.sample(range(1, 200), 15)
    
    even_numbers = []
    odd_numbers = []
    outliers = []
    
    for el in my_list:
        if el % 2 != 0:
            odd_numbers.append(el)
        elif el >= 100:
            outliers.append(el)
        else:
            even_numbers.append(el)
    
    print(f'Out:\nEven numbers {even_numbers}\nOdd numbers {odd_numbers}\nOutliers {outliers}\nThe count of even numbers in the list {len(even_numbers)}')


# Additional task LOOOPS - task(3) (homework 2)
def cumulative_sum():
    lst = [1,2,3,4,5,6,7,100,110,21,33,32,2,4]
    for el in range(1,len(lst)):
        lst[el] = lst[el-1] + lst[el]
    print(lst)

# Additional task LOOOPS - task(4) (homework 2)
def drow_tree(count_star:int):
    for el in range(1,count_star+1):
        print("*" * el)
    



if __name__ == '__main__':
    task_2_and_3_in_one()
    list_comprehation(1, 10)
    number_check_pos_neg_zero()
    price_of_sandwich('Cheese Roll')
    sort_loop()
    cummulate_sum()
    drow_tree(6)
    [get_time_now() for i in range(10)] # Homework 4 - task(3)
