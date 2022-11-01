# class Cat:
#     name = "Чаппи"
#     age = 4
#
# print(Cat.name, Cat.age)

# class Car:
#     color = 'Grey'
#     # Статические поля(переменные класса)
#     default_color = 'Grey'
#     default_weight = 5000
#
#     def __init__(self, color, model):
#         # Динамические поля (переменные объекта)
#         self.color = color
#         self.model = model
#
#     def turn_on(self):
#         pass
#
#     def ride(self):
#         pass
#
#
# car_object = Car()

### Домашнее задание № 1 ###
# class Example:
#     num_1 = 10
#     num_2 = 40
#
#     def __init__(self, ch_1, ch_2):
#         self.ch_1 = ch_1
#         self.ch_2 = ch_2
#
#     def fun_1(self):
#         return self.ch_1
#
#     def fun_2(self):
#         return Example.num_1 + Example.num_2
#
#     def fun_3(self):
#         return self.ch_1 ** self.ch_2
#
#
# a = Example(20, 5)
#
# print(a.fun_1())
# print(a.fun_2())
# print(a.fun_3())

### Домашнее задание № 2 ###
# class Calculator:
#
# # def __init__(self):
# #     self.a = int(input("Введите число: "))
# #     self.w = input("Введите знак(+,-,*,/): ")
# #     self.b = int(input("Введите число: "))
# #     if self.w == '+':
# #         print(qwe.sloj())
# #     elif self.w == '-':
# #         print(qwe.otnim())
# #     elif self.w == '*':
# #         print(qwe.umnoj())
# #     elif self.w == '/':
# #         print(qwe.delen())
#
#         def sloj(self):
#             return a + b
#
#         def otnim(self):
#             return a - b
#
#         def umnoj(self):
#             return a * b
#
#         def delen(self):
#             return a / b
#
# qwe = Calculator()
#
# # Не могу сообразить как сделать. Хоть и понимаю, что не правильное такое решение.
#
# a = int(input('Введите число: '))
# w = input('Введите знак(+,-,*,/): ')
# b = int(input('Введите число: '))
# if w == '+':
#     print(qwe.sloj())
# elif w == '-':
#     print(qwe.otnim())
# elif w == '*':
#     print(qwe.umnoj())
# elif w == '/':
#     print(qwe.delen())
# else:
#     print("Не корректный ввод данных!")

### Домашнее задание № 3 ###

# class Method:
#
#     def priem(self):
#         if

text = input('Ведите число и слово: ')
a = 1
for i in text:
    if i.isdigit():
        if int(i) % 2 == 0:
            a = a + int(i)
        print(i)