#mod 3. task 3.2.1
shopping_dict = {
    "цукерню": ["тістечко", "торт", "булочку"],
    "продуктовий": ["молоко", "хліб", "сметану"],
    }

for keys, values in shopping_dict.items():
  print(f"Заходжу в", keys.capitalize(), "купую тут такі товари:", values)

number = sum([len(v) for v in shopping_dict.values()])
print("Разом купую", number ,"товарів.")

#mod 3. task 3.2.2
#числа, які діляться на 5
for i in range(1, 101):
  if (i % 5) == 0:
    print(i)
#підносимо до 3ї степені
num3 = [i**3 for i in range(1, 101) if (i % 5) == 0]
print(num3)
