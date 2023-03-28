#Task 3.1

#модуль3 завдання1
#https://replit.com/@MaryBuriak/HummingSuburbanSandbox#main.py
#Заходжу в Пекарня, купую тут такі товари: ['Хліб', 'Пончик', 'Булки'].
#Їду до Продуктовий, купую такі товари: ['Морква', 'Селера', 'Рукола'].
#Разом купую 6 товарів.

shopping_dict = {
    "пекарня": ["хліб", "пончик", "булки"],
    "продуктовий": ["морква", "селера", "рукола"],
    }

for keys, values in shopping_dict.items():
  print(f"Заходжу в", keys.capitalize(), "купую тут такі товари:", [v.capitalize() for v in values])
#прописавши [v.capitalize() for v in values] ми зможемо зробити values з великої букви

#варіант1
#number = (len(shopping_dict["пекарня"])+len(shopping_dict["продуктовий"]))
#так прописувати не дуже вдала ідея, оскільки рахує лише по 2 в дв. доданим ключам. Оскільки ключів може бути багото, то краще прописувати по іншому

#var 2
number=0
for value in shopping_dict.values():
  number += len(value)

print("Разом купую", number ,"товарів.")

#var 3
number = sum([len(v) for v in shopping_dict.values()])
print("Разом купую", number ,"товарів.")

