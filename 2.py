# Задание 2
# в наличии список множеств. внутри множества целые числа
# посчитать
#  1. общее количество чисел
#  2. общую сумму чисел
#  3. посчитать среднее значение
#  4. собрать все числа из множеств в один кортеж

import statistics

m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
# *написать решения в одну строку

#  1. общее количество чисел
print('Общее количество чисел: {}'.format(sum(len(each_set) for each_set in m)))
#  2. общую сумму чисел
print('Общая сумму чисел: {}'.format(sum(list(sum(each_set) for each_set in m))))
#  3. посчитать среднее значение
print('Среднее значение каждого множества: {}'.format(list(statistics.mean(each_set) for each_set in m)))
print('Среднее значение всех чисел: {}'.format(statistics.mean(el for each_set in m for el in each_set)))
#  4. собрать все числа из множеств в один кортеж
print('Все числа из множеств в один кортеж:{}'.format(tuple(el for each_set in m for el in each_set)))
