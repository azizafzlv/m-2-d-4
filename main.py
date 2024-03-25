#1
"""
Посчитать кол-во одинаковых эл в списке. Дан список целых чисел
[1, 1, 3, 2, 1, 3, 4]
"""

# class MyList:

#     def __init__(self, num_list) -> None:
#         self.num_list = num_list

#     def get_num_rep_count(self):
#         result = {}

#         for num in self.num_list:
#             if num in result:
#                 result[num] += 1
#             else:
#                 result[num] = 1

#         for k, v in result.items():
#             print(f'Число {k} встречается {v} раз')

#     def __str__(self) -> str:
#         return f'Список: {self.num_list}'

# my_list = MyList([1, 1, 3, 2, 1, 3, 4])
# my_list.get_num_rep_count()
# print(my_list)

#2
"""
В строке заменить пробелы символом * Если встречается
подряд несколько, то их все равно менять на одну звезду.
Пробелы в начале и конце удалить.
"""

# class Star:

#     def __init__(self, text) -> None:
#         self.text = text

#     def replace_space_to_star(self):
#        result = ''
#        for t in self.text.strip().split():
#            result += t
#            result += '*'

#        print(result[:-1])


# star = Star('     Hello World! ')
# star.replace_space_to_star()

#3
"""
Принимает имя файла и выводит его расширение
Если расшир невозможно опр-ть, выбросить исключение
"""

# import os

# path = '' #путь на мой стол или папку (через терминал)
# result = []

# class Path:
#     def __init__(self, path) -> None:
#         self.path = path

#     def get_files_ext(self):
#         for name in os.listdir(path=self.path):
#             if os.path.isfile(os.path.join(self.path, name)):
#                 if name.split('.')[-1] in ('pdf', 'doc', 'txt'):
#                     print(f"{name.split('.')[0]} - формат {name.split('.')[-1]}")

# path = Path('') #тут должен быть мой путь на файлы
# path.get_files_ext()

#4
"""
Сложить цифры целого числа 35732
"""

number = 35732
result = 0 

for n in str(number):
    result += int(n)

print(result)