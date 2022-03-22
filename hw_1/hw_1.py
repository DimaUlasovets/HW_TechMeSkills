def printing_hello_my_name():
    return print('Hello, my name is Dima, nice to meet you')


def solves_math_equantion():
    equantion = ((2**5) * 2 - (16*2)) / (8**8)
    return print(f'The result of the equation is the type int: {type(equantion) == int}')


def show_all_data_type():
    return print([11, 22.1, 'hello', True, [1,2,3,4], {'name':'Dima'}, (1,2), {1,2,3}])



if __name__ == "__main__":
    printing_hello_my_name()
    solves_math_equantion()
    show_all_data_type()