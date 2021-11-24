from pprint import pprint
class Person:
    def __init__(self, name, age, address, height, weight):
        self.name, self.age, self.address, self.height, self.weight = name, age, address, height, weight
        self.key = (name, address)
    def __repr__(self):
        return "('%s','%s','%s','%s','%s')" % (self.name, self.age, self.address, self.height, self.weight)

Alisa = Person('Иванова Алиса Романовна', 17, "Lva Shatrova, 15, 109", 169, 55)
Alina = Person('Рахматуллина Алина Римовна', 32, "Komsomolskyi prospect, 23, 59", 161, 61)
Arina = Person('Костарева Арина Олеговна', 20, "Bratskaya, 33, 45", 180, 67)
people = {
    Alisa.key: {
        'ФИО': Alisa.name,
        'Адрес': Alisa.address,
        'Возраст': Alisa.age,
        'Рост': Alisa.height,
        'Вес': Alisa.weight
    },
    Alina.key: {
        'ФИО': Alina.name,
        'Адрес': Alina.address,
        'Возраст': Alina.age,
        'Рост': Alina.height,
        'Вес': Alina.weight
    },
    Arina.key: {
        'ФИО': Arina.name,
        'Адрес': Arina.address,
        'Возраст': Arina.age,
        'Рост': Arina.height,
        'Вес': Arina.weight
    }
}
#for k in people:
    #pprint(people[k])


print('enter min/max height')
mheight = int(input())
print('enter bigger(b) or smaller(s)')
option = input()
people_filter = {}

if option == 'b':
    for k in people:
        if people[k]['Рост'] > mheight:
            people_filter[k] = people[k]
else:
    for k in people:
        if people[k]['Рост'] < mheight:
            people_filter[k] = people[k]
pprint(people_filter)

from CompareFunction import fuzzyComparing
print('enter name')
names1 = str(input())
for k in people:
    x = fuzzyComparing(names1, people[k]['ФИО'])
    if x > 0.3:
        pprint(people[k])

print('enter weight')
weighs1 = int(input())
for k in people:
    if (people[k]['Вес'] > (0.95*weighs1)) and (people[k]['Вес'] < (1.05*weighs1)):
        pprint(people[k])