"""class Family:
    def names(self):
        return 4
    a = ["Ben", "Engineer", "12.06.1977"]
    b = ["Sofia", "Lawyуr", "22.09.1980"]
    c = ["Jack", "Student", "17.05.2000"]
    d = ["Maria", "Student", "29.12.2010"]

family_objects = Family()
print("Общее колличество членов семьи: ", family_objects.names())
print()

class Dad(Family):
    def name_dad(self):
        return family_objects.a[0]
       
    def profession_dad(self):
        return family_objects.a[1]

    def date_of_birth(self):
        return family_objects.a[2]

Dad_objects = Dad()
print("Имя папы: ", Dad_objects.name_dad())
print("Профессия папы: ", Dad_objects.profession_dad())
print("Дата рождения папы: ", Dad_objects.date_of_birth())
print()"""


print()
class Dad:
    def name_ded(self):
        return "Ben"
    def profession_dad(self):
        return "Engineer"
    def date_of_birth_dad(self):
        return "15.10.1987"
    def __init__(self, name, profession, date_of_birth):
        self.name = name
        self.profession = profession
        self.date_of_birth = date_of_birth
objects_dad = Dad('Ben','Engineer','15.10.1987')
res1 = objects_dad.__dict__
for i in res1.values():
    print(i)
print()


class Mom(Dad):
    def name_mom(self):
        return "Sofia"
    def profession_mom(self):
        return "Lowyer"
    def date_of_birth_mom(self):
        return "30.06.1990"
    def __init__(self, name, profession, date_of_birth):
        self.name = name
        self.profession = profession
        self.date_of_birth = date_of_birth
objects_mom = Mom('Sofia','Lowyer','30.06.1990')
res2 = objects_mom.__dict__
for j in res2.values():
    print(j)
print()


class Sun(Mom):
    def name_sun(self):
        return "Jack"
    def profession_sun(self):
        return "Student"
    def date_of_birth_sun(self):
        return "12.11.2000"
    def __init__(self, name, profession, date_of_birth):
        self.name = name
        self.profession = profession
        self.date_of_birth = date_of_birth
objects_sun = Sun('Jack','Student','12.11.2000')
res3 = objects_sun.__dict__
for k in res3.values():
    print(k)
print()


class Daughter(Sun):
    def name_daughter(self):
        return "Maria"
    def profession_daughter(self):
        return "Student"
    def date_of_birth_daughter(self):
        return "02.04.2003"
    def __init__(self, name, profession, date_of_birth):
        self.name = name
        self.profession = profession
        self.date_of_birth = date_of_birth
objects_daughter = Daughter('Maria','Student','02.04.2003')
res4 = objects_daughter.__dict__
for z in res4.values():
    print(z)
print()