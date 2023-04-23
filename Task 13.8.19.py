# tickets = int(input("При покупке от 3-х билетов действует скидка 10% от стоимости заказа!\n"
#                    "Введите количество билетов, которое хотите приобрести: "))
# age = list(int(input("Введите возраст посетителей: ")) for i in range(tickets))# узнаем возраст посетителей
#
# # count1 = 0
# # count1 = sum(True for i in age if i < 18)# считаем сколько берут бесплатных билетов
# # print("Билеты участникам до 18 лет: ", count1, "бесплатно")
# # count2 = 0
# # count2 = sum(True for i in age if  18 <= i <= 25)# считаем сколько берут билетов за 990 р
# # print("Билеты участникам от 18 до 25 лет: ", count2, "за 990 р")
# # count3 = 0
# # count3 = sum(True for i in age if i > 25)# считаем сколько берут билетов за 1390
# # print("Билеты участникам старше 25 лет: ", count3, "за 1390 р")
# #
# # pay = count1 * 0 + count2 * 990 + count3 * 1390# считаем общую стоимость
# # if tickets >= 3:# рассчитываем скидку, если берут больше 3 билетов
# #     pay = pay - pay * 0.1
# #     print("Общая стоимость со скидкой 10% за покупку более 3 билетов: ", pay)# общая стоимость при покупке более 3 билетов
# # else:
# #     print("Общая стоимость билетов: ", pay)# выводим общую стоимость для пользователя
#
# # Вариант 2
# price = []# создаем список билетов, соответсвенно возрасту
# for i in age:
#     if i in range(0, 18):
#         price.append(0)
#     elif i in range(18, 25):
#         price.append(990)
#     else:
#         price.append(1390)
#
# a = int(sum(price))# считаем сумму всех билетов
#
# if tickets >= 3:# рассчитываем скидку, если берут больше 3 билетов
#     pay = a - a * 0.1
#     print("Общая стоимость со скидкой 10% за покупку более 3 билетов: ", pay)# общая стоимость при покупке более 3 билетов
# else:
#     print("Общая стоимость билетов: ", sum(price))# выводим общую стоимость для пользователя


# myFile = open('filename.txt', encoding="utf8")
# for line in myFile:
#     print(line)

# myFile = open('namefile.txt', 'w')
# myFile.write('tttt')
# # print('zzzz', file=myFile)
# class Event:
#     def __init__(self, timestamp, event_type, session_id):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
# events = [
#     {
#      "timestamp": 1554583508000,
#      "type": "itemViewEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1555296337000,
#      "type": "itemViewEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1549461608000,
#      "type": "itemBuyEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
# ]
# for event in events:
#     event_obj = Event(timestamp=event.get("timestamp"),
#                       event_type=event.get("type"),
#                       session_id=event.get("session_id"))
#     print(event_obj.timestamp)
#
# stack = (5+6)*(7+8)/(4+3)
# def par_checker(string):
#     stack = []  # инициализируем стек
#
#     for s in string:  # читаем строку посимвольно
#         if s == "(":  # если открывающая скобка,
#             stack.append(s)  # добавляем её в стек
#         elif s == ")":
#             # если встретилась закрывающая скобка, то проверяем
#             # пуст ли стек и является ли верхний элемент — открывающей скобкой
#             if len(stack) > 0 and stack[-1] == "(":
#                 stack.pop()  # удаляем из стека
#             else:  # иначе завершаем функцию с False
#                 return False
#     # если стек пустой, то незакрытых скобок не осталось
#     # значит, возвращаем True, иначе — False
#     return len(stack) == 0
# print()
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
counter = 0
for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx+1] > x:
        array[idx] = array[idx+1]
        idx += 1
    array[idx] = x

print(counter)
