# Задание № 6.1
# class Animal:
#     def __init__(self, name, species, age=0, weight=0, is_domestic=True):
#         self.__name = name
#         self.__species = species
#         self.__age = age
#         self.__weight = weight
#         self.__is_domestic = is_domestic
#
#     def __str__(self) -> str:
#         return f'Имя животного {self.__name}, вид животного {self.__species}, возраст {self.__age}, \nвес {self.__weight}, является домашним {self.__is_domestic}'
#
#     def get_name(self) -> str:
#         return self.__name
#
#     def set_name(self, name:str) -> str:
#         self.__name = name
#
#     def get_species(self) -> str:
#         return self.__species
#
#     def set_species(self, species:str) -> str:
#         self.__species = species
#
#     def get_age(self) -> int:
#         return self.__age
#
#     def set_age(self, age:int) -> int:
#         self.__age = age
#
#     def get_weight(self) -> float:
#         return self.__weight
#
#     def set_weight(self, weight:float) -> float:
#         self.__weight = weight
#
#     def get_is_domestic(self) -> bool:
#         return self.__is_domestic
#
#     def set_is_domestic(self, is_domestic: bool) -> bool:
#         self.__is_domestic = is_domestic
#
#     def make_sound(self, sound:str) -> str:
#         return f'Животное издало звук {sound}'
#
#
#     def feed(self, food:float) -> float or str:
#         if food > 0:
#             self.__weight = self.__weight + food
#         else:
#             return f'Введите корректное значение'
#
#
# a1 = Animal('Бегемот', "кот", 1, 1)
# print(a1)
# a1.set_name('lex')
# a1.feed(0.1)
# print(a1)

# 6.2

class Pizza:
    def __init__(self, name, ingredients, size, price=None):
        self.__name = name
        self.__ingredients = ingredients
        self.__size = size
        self.__price = price

    def __str__(self):
        pass

    def add_ingredients(self, ingredients):
        self.__count_ingredients = []
        self.__count_ingredients.append(ingredients)
    def calculate_price(self):
        pass



