scope = {}                            # "namespace" : "var"
for number_of_request in range(int(input())):   # вводится колличество запросов
    order = input().split()   # вводится строка с командой
    if order[0] == 'add':
        # add <namespace> <var> – добавить в пространство <namespace> переменную <var>
        namespace, var = order[1], order[2]
        if namespace in scope.keys():
            scope[namespace] += [var]
        else:
            scope[namespace] = [var]

    variables = {'global': []} # ключ - namespace_parent : значение - множество переменных и имена пространства_children
number_of_requests = int(input())
for number in range(number_of_requests):
    order = input().split()
    if order[0] == 'create':
        if order[2] in variables.keys():
            variables[order[2]].append(order[1])
            variables[order[1]] = []
    if order[0] == 'add':
        variables[order[1]].append(order[2])
    if order[0] == 'get':
        print('другой')
print(variables)