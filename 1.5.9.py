class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.some_list = []

    def add(self, *a):
        # добавить следующую часть последовательности
        for digit in a:
            self.some_list.append(digit)
            if len(self.some_list) == 5:
                print(sum(self.some_list))
                self.some_list = []

    def get_current_part(self):
        return self.some_list   # вернуть сохраненные в текущий момент
                                # элементы последовательности в порядке, в котором они были добавлены