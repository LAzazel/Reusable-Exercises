'''Identifiers'''
from configparser import Error
from os import error

name = 'Myron'
YEAR_OF_BIRTH = 2007

def hello(x):
    return f'Hello, {x}!'


print(hello(name))

'''Loops'''

def range_(start, end):
    return [i for i in range(start, end+1)]

def range_odd(start, end):
    return [i for i in range(start, end+1) if i % 2 != 0]


print(range_(15,30))
print(range_odd(15,30))

'''Functions'''

def average(a, b):
    return (a + b) / 2

def square(a):
    return a ** 2

def cube(a):
    return a ** 3

def calculate():
    res = []
    for i in range(10):
        i_sq = square(i)
        i_cube = cube(i)
        avg = average(i_sq, i_cube)
        res.append(avg)
    return res


print(calculate())

'''Objects'''

def fn():

    OBJ = {"name": "Constant"}
    obj = {"name": "Variable"}

    # Зміна значення поля `name` в обох об'єктів
    OBJ["name"] = "Changed in OBJ"
    obj["name"] = "Changed in obj"

    # Спроба записати посилання на інший об'єкт в обидва ідентифікатори
    OBJ = {"name": "New Object for OBJ"}
    obj = {"name": "New Object for obj"}
    return OBJ, obj

print(fn())

# У Python нема такого поняття як константа, є лише домовленість між розробниками, що змінні, назви яких записані у
# верхньому реєстрі краще не чіпати.

def create_user(name, city):
    return {'name': name, 'city': city}

print(create_user('John Smith', 'London'))

'''Collections: Array, Hash (Object)'''

collection = [
    {'name': 'Marcus Aurelius', 'phone': '+380445554433'},
    {'name': 'Seneca', 'phone': '+380123456789'},
    {'name': 'Plato', 'phone': '+380987654321'},
    {'name': 'Socrates', 'phone': '+380111223344'}
]
collection_1 = {
    'Marcus Aurelius': '+380445554433',
    'Seneca': '+380123456789',
    'Plato': '+380987654321',
    'Socrates': '+380111223344',
}

def find_phone_by_name(name):
    for i in collection:
        if i['name'] == name:
            return i['phone']
        return 'Number not found'

def find_phone_by_name_1(name: str) -> str:
    return collection_1.get(name, 'Number not found')

print(find_phone_by_name('Marcus Aurelius'))
print(find_phone_by_name('Aristotle'))
print(find_phone_by_name_1('Marcus Aurelius'))
print(find_phone_by_name_1('Aristotle'))