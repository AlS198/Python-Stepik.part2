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