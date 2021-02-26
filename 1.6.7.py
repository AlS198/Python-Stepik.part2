tree_of_classes = {}    #"дети" : "родители"
for number_of_classes in range(int(input())):
    order = input().replace(":", " ").split()
    if len(order) == 1:
        order.append('null')    # если нет потомков, то добавляем NULL
        tree_of_classes[order[0]] = order[1]
    if len(order) > 2:
        tree_of_classes[order[0]] = []  # все случаи когда родителей > 1
        for i in order[1:]:
            tree_of_classes[order[0]] += i
    else:
        tree_of_classes[order[0]] = order[1]
for number_of_request in range(int(input())):
    inheritance_request = input().split()
    if inheritance_request[1] == inheritance_request[0]:    # если класс наследуется от себя явно
        print('Yes')
    if ((inheritance_request[1] in tree_of_classes.keys())  # если класс есть в словаре
        and (inheritance_request[0] in tree_of_classes[inheritance_request[1]])):
        print('Yes')
    else:
        print('No')
