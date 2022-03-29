from datetime import datetime
from functools import reduce

# HW 5: task(1,2,3,4)
def my_decorator(func):
    ''' 
    parent function that accepts a nested function (child) with the described logic

    Args:
        func - the function to be wrapped

    '''

    def wrapper():
        '''
        a child function in which additional logic is written for the wrapped function
        '''

        time_start = datetime.now()
        func()
        time_end = datetime.now()
        print(f'function running time: {time_end - time_start}')
    return wrapper
        

@my_decorator
def simple_lambda(len_range: int) -> None:
    '''
    This function squares a number between zero and the specified parameter: len_range

    Args:
        len_range - end point in range
    '''

    list(map(lambda num: num ** 2, [i for i in range(len_range)]))

# HW 7: task(1,2,3,4,5,6)

# ---------------------------------------------Task-1---------------------------------------------------
def bread(func):
    def wrapper(ingridient):
        print()
        func(ingridient)
        print('Хлеб')
    return wrapper


def vegetables(func):
    def wrapper(ingridient):
        print('помидор')
        func(ingridient)
        print('салат')
    return wrapper


@vegetables
@bread
def sendwich(ingridient: str) -> None:
    print(ingridient)


# ---------------------------------------------Task-2---------------------------------------------------
def benchmark_3(func):
    def wrapper(*args):
        func(*args)
        print("don't worry here's all the info")
        print(f'Func name: {func.__name__}')
        print(f'Func args: {args}')
    return wrapper()



@benchmark_3
def test_func(*args):
    print("Help me now my func_name and my args")


# ---------------------------------------------Task-4---------------------------------------------------
def rounding_numbers(values: list) -> list:
    return print(list(map(lambda num: int(num), values)))


# ---------------------------------------------Task-5---------------------------------------------------
def sort_num_grater_80(values: list) -> list:
    return print(list(filter(lambda el: el > 80, values)))


# ---------------------------------------------Task-6---------------------------------------------------
def find_polindrom(values: list) -> list:
    return print(list(r(lambda el: el == el[::-1], values)))


# ---------------------------------------------Task-7---------------------------------------------------
def count_sum_of_el(values: list) -> list:
    return print(reduce(lambda x, y: x*y, values))
    


# ---------------------------------------------Task-8---------------------------------------------------
def max_iten_in_list(values: list) -> list:
    return print(max(values))


# ---------------------------------------------Task-9---------------------------------------------------
def count_of_word_cap(values: list) -> list:
    count = reduce(lambda a, x: a + x.count('капитан'), values,0)
    print(count)






if __name__ == '__main__':
    simple_lambda(100)
    sendwich('котлета')
    test_func('Hello', [1,2,3]) # TODO Alarm!! хз, что-то не могу вдуплить, поч ошибка и поч args не работает
    rounding_numbers([6.424, 123.131231, 1.123, 0.123, 11.11])
    sort_num_grater_80([1,23,57,82,111,234124,1223,5161,0])
    find_polindrom(["demigod", "rewire", "madam", "fortran", "python", "xamarin", "salas", "PHP"])
    count_sum_of_el([1, 2, 3, 4])
    max_iten_in_list([3, 5, 2, 4, 7, 1])
    count_of_word_cap(['капитан джек воробей', 'капитан дальнего плавания', 'ваша лодка готова, капитан'])