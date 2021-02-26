tree_of_classes = {}                            #"дети" : "родители"
for number_of_classes in range(int(input())):   # вводится колличество запросов
    order = input().replace(":", " ").split()   # вводится строка с отношениями Дети : Родители
    if len(order) == 1:
        order.append('null')                    # если нет потомков, то добавляем NULL
        tree_of_classes[order[0]] = order[1]    # тут все хорошо
    else:
        if order[0] in tree_of_classes.keys():  # если такой ключ уже есть в словаре, то добавляем значения
            for i in order[1:]:                 # не работает т.к. воспринимает срез как строку (посимвольно)
                tree_of_classes[order[0]] += [i]
        else:                                   # если ключа нет, то создаем и после добавляем значения
            tree_of_classes[order[0]] = []
            for i in order[1:]:                 # не работает т.к. воспринимает срез как строку (посимвольно) !!!! 
                tree_of_classes[order[0]] += [i]
print(tree_of_classes)
for number_of_request in range(int(input())):
    inheritance_request = input().split()
    if inheritance_request[1] == inheritance_request[0]:            # если класс наследуется от себя явно
        print('Yes')
    if ((inheritance_request[1] in tree_of_classes.keys())          # если класс есть в словаре
            and (inheritance_request[0] in tree_of_classes[inheritance_request[1]])):
        print('Yes')
    else:
        print('No')
