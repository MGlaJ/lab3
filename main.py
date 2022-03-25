# #zadanie_1
# a = [1-x for x in range(1,10)]
# b = [4**i for i in range(8)]
# c = [x for x in a if x % 2 == 0]
# print(a)
# print(b)
# print(c)

# #zadanie_2
# import random
# lista1 = [random.randint(0,1000)]
# lista1.append(random.randint(0,1000))
# lista1.append(random.randint(0,1000))
# lista1.append(random.randint(0,1000))
# lista1.append(random.randint(0,1000))
# lista1.append(random.randint(0,1000))
# lista1.append(random.randint(0,1000))
# lista1.append(random.randint(0,1000))
# lista1.append(random.randint(0,1000))
# lista1.append(random.randint(0,1000))
#
#
# print (lista1)
# lista2 = [i for i in lista1 if i % 2 == 0]
# print (lista2)

# #zadanie_3
#
# lista = {'bułki':'sztuka','pomidory':'kilogram',
#          'chleb':'sztuka','por':'sztuka',
#          'ziemniaki':'kilogram','mleko':'litr',
#          'woda mineralna':'litr'}
#
# #wersja_z_pętlą
# # for key in lista:
# #     if lista[key] == 'sztuka':
# #         print(key, lista[key])
# #wersja_comprehension
# lista1 = {key:value for key, value in lista.items() if lista[key]=='sztuka'}
# print(lista1)

# # zadanie_4
# # w trójkącie prostokątnym (a^2)+(b^2)=(c^2), gdzie a i b to przyprostokątne, oraz c to przeciwprostokątna
#
# def trójkąt_prostokątny(a,b,c):
#     Pitagoras = a*a + b*b
#     if Pitagoras == c*c:
#         print('Badany trójkąt jest prostokątny!')
#     else:
#         print('Ten trójkąt nie jest prostokątny...')
#
# print(trójkąt_prostokątny(3,4,5))
# print(trójkąt_prostokątny(3,5,12))

# # zadanie_5
# def pole_trapezu(a=1,b=2,h=1):
#     return ((a+b)/2)*h
# print(pole_trapezu(a=4))
# print(pole_trapezu(a=5,h=2))

# # zadanie_6
# def ciag(a=1,b=4,ile=10):
#     print(a*(pow((a*b),(ile-1)))*(pow(b,(ile-2))))
#
# print(ciag())
#
# # zadanie_7
# def ciagg(a=1, b=4, ile=10):
#     print((a*((a*b)**(ile-1)))*(b**(ile-2)))
#
# print(ciagg())

# # zadanie_8
# def lista_zakupow(**zakupy):
#     ile_produktow=len(zakupy)
#     zaplata=0
#     for x in zakupy:
#         zaplata = zaplata + zakupy[x]
#     print(zaplata, ile_produktow)
#
# print(lista_zakupow(mleko=4, jogurt=2, bulka=1, ser=7))

# #zadanie_9
#
# from ciagi import *









