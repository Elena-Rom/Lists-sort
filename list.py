list_a=[1,2,3,-1,-2,-3,True,False,[1,2],[3,4],'test1','test2',0.5,0.6]
list_b=[1,2,-1,-2,True,[1,2],'test1',0.5]
list3 = [x for x in list_a if x not in list_b] # сформироли список со значениями которых нет в list_b , но есть в list_a
print(list3)
# вытаскиваем из списка значения нужного нам типа
list4 = [x for x in list3 if type(x) == bool]
list5 = [x for x in list3 if type(x) == str]
list6 = [x for x in list3 if type(x) == int]
list7 = [x for x in list3 if type(x) == list]
list8 = [x for x in list3 if type(x) == float]
c = {'bool': list4, 'str': list5,'int':list6,'list':list7,'float':list8} # создаем словарь
print(c)