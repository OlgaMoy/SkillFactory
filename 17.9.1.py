# Объявляем функцию сортировки
def sort_func(elements_list):
    for i in range(len(elements_list)):
        for j in range(len(elements_list) - i - 1):
            if elements_list[j] > elements_list[j + 1]:
                elements_list[j], elements_list[j + 1] = elements_list[j + 1], elements_list[j]
    return elements_list

# Объявляем функцию поиска индекса заданного пользователем числа в списке введенных значений
def binary_search(list_of_numbers, user_number):
    low = 0
    high = len(list_of_numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if list_of_numbers[mid] == user_number:
            return mid
        elif list_of_numbers[mid] < user_number:
            low = mid + 1
        else:
            high = mid - 1
    return low

# Ввод последовательности чисел и рандомного числа
list_of_numbers = input("Введите числа от 1 до 999 в любом порядке, через пробел: ")
user_number = int(input('Введите любое число: '))

# Убираем из списка все не числовые значения
elements_list = []
for elem in list_of_numbers.split():
    if elem.isdigit():
        elements_list.append(int(elem))


sort_result = sort_func(elements_list)
print(f'Упорядоченный по возрастанию список: {sort_result}')# выводим упорядоченный по возрастанию список
print(f'Индекс введенного числа в заданной последовательности: ', binary_search(sort_result, user_number))# выводим индекс заданного числа
