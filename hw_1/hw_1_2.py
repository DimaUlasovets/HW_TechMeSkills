def get_your_name():
    my_name = input('\nGive me your name: ')
    return print(f'Your name if {my_name}')


def film_rating():
    you_age = int(input('Input your age: '))
    if you_age <= 12 and you_age >= 1:
        return print('can only see rated PG movies')
    elif you_age > 12 and you_age <= 17:
        return print('can see a rated PG-13 movie')
    elif you_age <= 0:
        return print("we'll figure something out")
    else:
        return print('can see a rated R movie')
    

def view_for_loop():
    for el in [1, 3, "Michele", None]: print(el)


def print_nested_list():
    for i in [1, 2, 3, ['multiple', 'list']]:
        if type(i) == list:
            for j in i:
                print(j)
        else:
            print(i)


def check_studend_list():
    list_of_stud = ["Michele", "Sara", "Cassie"]
    my_name = input('Type name to check: ')
    if my_name in list_of_stud:
        return print('This student in list')
    else:
        return print('This student is not enrolled')


def str_slicing():
    user_input_word = input('Write some word: ')
    return print(user_input_word[0:-1])
    




if __name__ == '__main__':
    get_your_name()
    film_rating()
    view_for_loop()
    nested_list()
    check_studend_list()
    str_slicing()