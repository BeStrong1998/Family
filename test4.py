# Декоратор

"""def func_decorator(func):
    def wrapper(*args, **kwargs):
        print('что то делаем пред вызовом функции')
        res = func(*args, **kwargs)
        print('что то делаем после вызова функции')
        return res

    return wrapper


def some_func(title, tag):
    print(f"title = {title}, tag = {tag}")
    return f"<{tag}>{title}</{tag}>"


#f = func_decorator(some_func)
#f()
some_func = func_decorator(some_func) #Декарируем функцию
some_func("Python", "h1")"""



import time

def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"Время работы: {dt} сек")
        return res

    return wrapper


"""def some_func(title, tag):
    print(f"title = {title}, tag = {tag}")
    return f"<{tag}>{title}</{tag}>"""
    

@test_time
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


#f = func_decorator(some_func)
#f()
#get_fast_nod = test_time(get_fast_nod) #Декарируем
res2 = get_fast_nod(2, 100000)
print(res2)

#get_nod = test_time(get_nod) #Декарируем
res1 = get_nod(2, 100000)
print(res1)