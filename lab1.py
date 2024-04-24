#   lab 1 variant 6

from functools import reduce
#  тізім / список элементов
numbers = [-12, 17, -36, 48, 65, 16, 56]
# Әр санды оның реттік нөміріне бөлеміз
result_list = [num / (index + 1) for index, num in enumerate(numbers)]
# 1-ден үлкен мәндерді сұрыптаймыз
filtered_list = list(filter(lambda x: x > 1, result_list))
# Сұрыпталған мәндерді тауып, қосамыз

sum_of_filtered = sum(filtered_list)
result_list = reduce(lambda x, y: x + y, filtered_list)
print(f"Оригинальный список: {numbers}")
print(f"Список после деления на порядковый номер: {result_list}")
print(f"Отфильтроваванный список (больше 1): {filtered_list}")
print(f"Сумма отфильтроваванных чисел: {result_list}")
