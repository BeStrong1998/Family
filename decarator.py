from time import time
from functools import wraps
from time import sleep

def time_moment(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        value = func(*args, **kwargs)
        end_time = time()
        print(f'Время выполнения функции {end_time-start_time} секунд')
        return value
    return wrapper

def counter(fun):
    def inner(*args, **kwargs):
        inner.count += 1
        sleep(1)
        return fun(*args, **kwargs)
    inner.count = 0
    return inner

@time_moment
@counter
def hello():
    #print(hello.count, 'Hello World!')
    print('Hello World!')

hello()
hello()
hello()

#print(hello.count)










"""def counter():
    count = 0
    def inner():
        nonlocal count #Говорим что мы берём значение атрибута count
        count += 1
        return count
    return inner"""