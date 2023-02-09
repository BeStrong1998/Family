# Пишем контекстный менеджер

class Resource:
    def __init__(self): #Создаём конструктор
        self.opened = False  #При создании ресурса помещаем его в переменную и говорим что он закрыт
    def open(self, *args): #Метод открытия ресурса которым мы пользуемся
        print(f'Ресурс открыт {args}') #Печатаем в консоли что ресурс открыт с аргументами которые переданы в {args}
        self.opened = True #Подтверждаем что теперь ресурс открыт
    def close(self): #Метод закрытия(высвобождения) ресурса которым мы пользуемся
        print('Ресурс закрыт') #Печатаем в конгсоли что ресурс закрыт
        self.opened = False #Говорим что ресурс под флажоком opened Закрыт
    def __del__(self): 
        if self.opened:
            print('Обнаружена утечка памяти! Русурс не был закрыт!')
    def action(self): #Создаём метод который что то делает с ресурсом
        print('Мы что то делаем с ресурсом') #Печатаем в консоль


class ResourceWorker:
    def __init__(self, *args): #При создании объекта ResourceWorker мы передаём какие то аргументы
        self.args = args #Сохраняем в переменной
        self.resource = None #Покак не будем создавать ресурс а присвоит ему Non
    def __enter__(self): #Запустим специальный магический метод (Вход)
        self.resource = Resource() #Создастся объект нашего ресурса
        self.resource.open(*self.args) #Откроем объект нашего ресурса c аргументами которые мы сохранили в нашем конструкторе __init__() self.args = args
        return self.resource #Вернёт сам ресурс в переменныю res
    def __exit__(self, exc_type, exc_val, exc_tb): #Запустим специальный магический метод (Выход). self, exc_type, exc_val, exc_tb аргументы по умолчанию
        if self.resource: #Проверяем если ресурс не Non
            self.resource.close() #Закрываем ресурс
            #return True
    
if __name__ == "__main__":
    with ResourceWorker("failer") as res:
        res.action()
        #raise ValueError('Stop')
