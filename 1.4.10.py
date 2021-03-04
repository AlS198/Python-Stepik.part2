scope = {}                            # "namespace" : "var"
for number_of_request in range(int(input())):   # вводится колличество запросов
    order = input().split()   # вводится строка с командой
    if order[0] == 'add':
        # add <namespace> <var> – добавить в пространство <namespace> переменную <var>
        namespace, var = order[1], order[2]
        if namespace in scope.keys():
            scope[namespace] += var
        else:
            scope[namespace] = var

    if order[0] == 'create':
        # create <namespace> <parent> –  создать новое пространство имен
        # с именем <namespace> внутри пространства <parent>
        namespace, parent = order[1], order[2]
        if parent in scope.keys():
            scope[parent] += {namespace: []}
        else:
            scope[parent] += {namespace: []}

    if order[0] == 'get':
        # get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var>
        # при запросе из пространства <namespace>, или None, если такого пространства не существует
        namespace, var = order[1], order[2]
        if namespace in scope.keys() and var in scope[namespace]:
            print(namespace)
        if namespace in scope.keys() and var not in scope[namespace]:
            print(scope[namespace])
        if namespace not in scope.keys():
            print('None')
print(scope)





    #if len(order) == 1:
    #    order.append('null')                    # если нет потомков, то добавляем NULL
    #   tree_of_classes[order[0]] = order[1]    # тут все хорошо
    #else:
    #    if order[0] in tree_of_classes.keys():  # если такой ключ уже есть в словаре, то добавляем значения
    #        for i in order[1:]:                 # не работает т.к. воспринимает срез как строку (посимвольно)
    #            tree_of_classes[order[0]] += [i]
    #    else:                                   # если ключа нет, то создаем и после добавляем значения
    #        tree_of_classes[order[0]] = []
    #        for i in order[1:]:                 # не работает т.к. воспринимает срез как строку (посимвольно) !!!!
    #            tree_of_classes[order[0]] += [i]
#print(tree_of_classes)
#for number_of_request in range(int(input())):
    #inheritance_request = input().split()
    #if inheritance_request[1] == inheritance_request[0]:    # если класс наследуется от себя явно
        #print('Yes')
    #if ((inheritance_request[1] in tree_of_classes.keys())  # если класс есть в словаре
            #and (inheritance_request[0] in tree_of_classes[inheritance_request[1]])):
        #print('Yes')
    #else:
        #print('No')