from pandas import Series
import pandas as pd

Obj = Series([4,7,-5,3])

#print(Obj)

#print(Obj.index)

#print(Obj.values)

#print(type(Obj))

obj2 = Series([4,7,-5,3], index = ['a', 'b', 'c', 'd'])

#print(obj2)

#print(obj2.values)

#print(obj2.index)

#print(obj2[obj2 > 3])

#print(obj2['b'])

#print('d' in obj2)

dict = {'futebol':5200, 'tenis':120, 'natacao':698, 'voleibol':1550}

obj3 = Series(dict)

#print(obj3)

esportes = ['futebol', 'tenis', 'natacao', 'basquete']
obj4 = Series(dict, index=esportes)

#print(obj4)

#print(obj3)

#print(obj4)

#print(pd.isnull(obj4))

#print(pd.notnull(obj4))

#print(obj3 + obj4)

obj4.name = 'populacao'
obj4.index.name = 'esporte'

#print(obj4)