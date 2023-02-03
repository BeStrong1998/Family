from abc import ABC, abstractmethod


class Family(ABC):
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def profession(self):
        pass
    @abstractmethod
    def date_of_birth(self):
        pass


class Dad(Family):
    def __init__(self, name, profession, date_of_birth):
        self.name_dad = name
        self.profession_dad = profession
        self.date_of_birth_dad = date_of_birth
    def name(self):
        return self.name_dad
    def profession(self):
        return self.profession_dad
    def date_of_birth(self):
        return self.date_of_birth_dad
dad = Dad("Ben", "Engineer", "15.10.1987")


class Mom(Family):
    def __init__(self, name, profession, date_of_birth):
        self.name_mom = name
        self.profession_mom = profession
        self.date_of_birth_mom = date_of_birth
    def name(self):
        return self.name_mom
    def profession(self):
        return self.profession_mom
    def date_of_birth(self):
        return self.date_of_birth_mom
mom = Mom("Sofia", "Lowyer", "05.09.1990")


class Son(Family):
    def __init__(self,name, profession, date_of_birth):
        self.__name_son = name
        self.__profession_son = profession
        self.__date_of_birth_son = date_of_birth
    def name(self):
        return self.__name_son
    def profession(self):
        return self.__profession_son
    def date_of_birth(self):
        return self.__date_of_birth_son
son = Son("Jack", "Student", "14.08.2012")


class Daughter(Family):
    def __init__(self,name, profession, date_of_birth):
        self.__name_daughter = name
        self.__profession_daughter = profession
        self.__date_of_birth_daughter = date_of_birth
    def name(self):
        return self.__name_daughter
    def profession(self):
        return self.__profession_daughter
    def date_of_birth(self):
        return self.__date_of_birth_daughter
daughter = Daughter("Anna", "Student", "02.09.2011")


family_lis = [dad, mom, son, daughter]
for lis in family_lis:
    print(lis.name())
    print(lis.profession())
    print(lis.date_of_birth())

print(Son.mro())

if __name__ == "__main__":
    main()
