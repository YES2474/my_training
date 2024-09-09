my_dict = {'Алекса': 1999, 'Мария': 2000, 'Иван': 2001, 'Роман': 2002,}
print('Словарь:', my_dict)
print('Год рождения Марии:', my_dict['Мария'])
print('Год рождения Елены:', my_dict.get('Елена', 'нет такого ключа'))
my_dict.update({'Денис': 1998, 'Анна': 2005})
removed_year = my_dict.pop('Анна')
print('Значение удалённого элемента \'Анна\':', removed_year)
print('Изменённый словарь:', my_dict)

print()

my_set={1,2,3,4,5,1,2,3,4,'String',True,(1,2,3)}
print('Множество',my_set)
my_set.add(66)
my_set.add('Float')
my_set.discard(2)
print('Изменённое множество:',my_set)
