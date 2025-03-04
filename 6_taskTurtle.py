# from gettext import dngettext
#
# from turtle import * # импорт всех функций модуля turtle
# down() # опустить хвост
# up() # поднять хвост
#
# tracer(0) # трассировка - нет (не следим за черепахой)
# speed() # ускорение
#
# screensize(2000, 2000) # размер холста
# forward() # вперед пикселей
# back() # назад
# left() # влево
# right() # вправо
# goto(10, 10) # перейти в точку с координатами()
# dot(3, 'blue') # поставить точку(размер, цвет)
# exitonclick() # выйти по клику
# done() # остановить выполнение

# изначально в питоне черепаха смотрит вправо (по оси абсцисс)
# в задачах часто изначально смотрит вдоль оси ординат,
# поэтому поворачиваем на 90 градусов влево

# Цветочек
# from turtle import *
# screensize(1000, 1000)
# speed(50)
# left(135)
# for i in range(0, 8):
#     forward(50)
#     right(45)
#     forward(50)
#     right(135)
#     forward(50)
#     right(45)
#     forward(50)
# done()


# Задание 1
# from turtle import *
# tracer(0)
# screensize(1000, 1000)
# speed(50)
# k = 35
# for i in range(0, 10):
#     forward(6*k)
#     right(120)
# up()
# for x in range(0, 7):
#     for y in range(-5, 1):
#         goto(x*k, y*k)
#         dot(4, 'blue')
# done()


# Задание 2
# from turtle import *
# speed(50)
# k = 10
# screensize(1000, 1000)
# for i in range(0, 100):
#     forward(10*k)
#     right(30)
# done()


# Задание 3
# from turtle import *
# speed(50)
# tracer(0)
# k = 5
# screensize(1000, 1000)
# for i in range(0, 10):
#     for j in range(0, 3):
#         forward(10*k)
#         right(90)
#         forward(10*k)
#         right(270)
#     right(90)
# up()
# for x in range(-30, 30):
#     for y in range(-61, 2):
#         goto(x*k, y*k)
#         dot(2, 'blue')
# done()


# Задание 4
# from turtle import *
# tracer(0)
# speed(50)
# screensize(1000, 1000)
# k = 25
# for i in range(0, 3):
#     forward(10*k)
#     right(120)
# up()
# forward(10*k)
# right(90)
# forward(3*k)
# down()
# for j in range(0, 4):
#     forward(10*k)
#     right(90)
# up()
# for x in range(-10, 20):
#     for y in range(-20, 10):
#         goto(x*k, y*k)
#         dot(3, 'blue')
# done()


# 1
# from turtle import *
# tracer(0)
# speed(50)
# screensize(1000, 1000)
# k = 45
# left(90)
# for i in range(0, 5):
#     forward(7*k)
#     right(120)
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x*k, y*k)
#         dot(3, 'blue')
# done()


# 2
# from turtle import *
# tracer(0)
# speed(50)
# screensize(2000, 2000)
# k = 5
# left(90)
# for i in range(0, 100):
#     forward(10*k)
#     right(8)
# done()


# 3
# from turtle import *
# tracer(0)
# speed(50)
# screensize(2000, 2000)
# k = 20
# down()
# left(90)
# forward(25*k)
# right(45)
# forward(50*k)
# up()
# backward(50*k)
# right(45)
# forward(15*k)
# left(90)
# forward(30*k)
# down()
# right(180)
# forward(60*k)
# backward(5*k)
# right(90)
# forward(31*k)
# up()
# for x in range(50):
#     for y in range(50):
#         goto(x*k, y*k)
#         dot(3, 'blue')
# done()


# 4
# from turtle import *
# tracer(0)
# speed(50)
# screensize(2000, 2000)
# k = 25
# down()
# for i in range(0, 2):
#     forward(11*k)
#     right(90)
#     forward(17*k)
#     right(90)
# up()
# forward(7*k)
# left(90)
# backward(1*k)
# right(90)
# down()
# for i in range(0, 2):
#     forward(15*k)
#     right(90)
#     forward(7*k)
#     right(90)
# up()
# for x in range(0, 25):
#     for y in range(-20, 1):
#         goto(x*k, y*k)
#         dot(3, 'blue')
# done()


# 5
# from turtle import *
# tracer(0)
# speed(50)
# screensize(2000, 2000)
# k = 25
# down()
# for i in range(0, 2):
#     forward(24*k)
#     right(90)
#     forward(16*k)
#     right(90)
# up()
# forward(10*k)
# right(90)
# forward(8*k)
# left(90)
# down()
# for i in range(0, 2):
#     forward(15*k)
#     right(90)
#     forward(28*k)
#     right(90)
# up()
# for x in range(0, 25):
#     for y in range(-20, 1):
#         goto(x*k, y*k)
#         dot(3, 'blue')
# done()


# 6
# from turtle import *
# tracer(0)
# speed(50)
# screensize(2000, 2000)
# k = 25
# down()
# for i in range(0, 2):
#     forward(5*k)
#     left(90)
#     backward(13*k)
#     left(90)
# up()
# backward(10*k)
# right(90)
# forward(9*k)
# left(90)
# down()
# for i in range(0, 2):
#     forward(11*k)
#     right(90)
#     forward(7*k)
#     right(90)
# up()
# for x in range(-18, 10):
#     for y in range(-18, 1):
#         goto(x*k, y*k)
#         dot(4, 'blue')
# done()


# 7
# from turtle import *
# tracer(0)
# speed(50)
# screensize(2000, 2000)
# k = 25
# down()
# for i in range(0, 2):
#     forward(8*k)
#     right(90)
#     forward(18*k)
#     right(90)
# up()
# forward(4*k)
# right(90)
# forward(10*k)
# left(90)
# down()
# for i in range(0, 2):
#     forward(17*k)
#     right(90)
#     forward(7*k)
#     right(90)
# up()
# for x in range(0, 22):
#     for y in range(-18, 1):
#         goto(x*k, y*k)
#         dot(5, 'blue')
# done()


# 8
# from turtle import *
# tracer(0)
# speed(50)
# screensize(2000, 2000)
# k = 15
# down()
# for i in range(0, 4):
#     forward(16*k)
#     left(90)
#     forward(20*k)
#     left(90)
# up()
# forward(4*k)
# left(90)
# forward(8*k)
# right(180)
# down()
# for i in range(0, 3):
#     forward(35*k)
#     left(90)
#     forward(6*k)
#     left(90)
# up()
# for x in range(4, 11):
#     for y in range(-27, 1):
#         goto(x*k, y*k)
#         dot(5, 'blue')
# done()


# 9
# from turtle import *
# tracer(0)
# speed(50)
# screensize(2000, 2000)
# k = 30
# down()
# for i in range(0, 2):
#     forward(7*k)
#     right(60)
#     forward(12*k)
#     right(120)
# up()
# forward(7*k)
# right(60)
# down()
# for i in range(0, 2):
#     forward(5*k)
#     right(120)
#     forward(10*k)
#     right(60)
# up()
# for x in range(0, 11):
#     for y in range(-6, 1):
#         goto(x*k, y*k)
#         dot(5, 'blue')
# done()


# 10
# from turtle import *
# tracer(0)
# speed(50)
# screensize(2000, 2000)
# k = 30
# down()
# left(180)
# for i in range(0, 3):
#     right(45)
#     forward(12*k)
#     right(45)
# left(315)
# forward(12*k)
# for i in range(0, 2):
#     right(90)
#     forward(12*k)
# up()
# for x in range(-10, 11):
#     for y in range(0, 20):
#         goto(x*k, y*k)
#         dot(5, 'blue')
# done()


# 11
# from turtle import *
# tracer(0)
# speed(50)
# screensize(2000, 2000)
# k = 35
#
# down()
# left(45)
# forward(10*k)
# right(75)
# forward(4*k)
#
# right(60)
# forward(3*k)
# right(60)
# forward(4*k)
#
# left(120)
# forward(4*k)
# right(60)
# forward(3*k)
#
# right(60)
# forward(4*k)
# right(75)
# forward(10*k)
# up()
# for x in range(0, 12):
#     for y in range(-10, 10):
#         goto(x*k, y*k)
#         dot(5, 'blue')
# done()


# from turtle import *
# screensize(2000, 1000)
# speed(50)
# tracer(0)
# left(90)
# k = 20
# pendown()
# for i in range(0, 4):
#     forward(19*k)
#     right(90)
#     forward(30*k)
#     right(90)
# penup()
# forward(2*k)
# right(90)
# forward(8*k)
# left(90)
# pendown()
# for s in range(0, 4):
#     forward(93*k)
#     right(90)
#     forward(97*k)
#     right(90)
# penup()
# for x in range(8, 31):
#     for y in range(2, 20):
#         goto(x*k, y*k)
#         dot(5, 'blue')
# done()


# from turtle import *
# screensize(2000, 1000)
# speed(50)
# tracer(0)
# left(90)
# k = 20
# for x in range(0, 3):
#     pendown()
#     for y in range(0, 2):
#         forward(10*k)
#         right(90)
#         forward(10 * k)
#         right(90)
#     penup()
#     forward(5*k)
#     right(90)
#     forward(5*k)
#     left(90)
# penup()
# for x in range(8, 31):
#     for y in range(2, 20):
#         goto(x*k, y*k)
#         dot(5, 'blue')
# done()


# from turtle import *
# screensize(1000, 1000)
# speed(50)
# tracer(0)
# k = 30
# left(90)
# pendown()
# for i in range(0, 3):
#     forward(7*k)
#     right(90)
# forward(8*k)
# for i in range(0, 3):
#     left(90)
#     forward(5*k)
# penup()
# for x in range(-10, 10):
#     for y in range(-10, 10):
#         goto(x*k, y*k)
#         dot(3, 'blue')
# done()



