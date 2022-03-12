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

#zadanie_3

lista = {'bułki':'sztuka','pomidory':'kilogram',
         'chleb':'sztuka','por':'sztuka',
         'ziemniaki':'kilogram','mleko':'litr',
         'woda mineralna':'litr'}


lista1 = [{lista.keys():lista.values() for ('sztuka') in lista.values()}]