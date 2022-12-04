class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.length = len(list_of_list)
        self.end = len(self.list_of_list[0]) + len(self.list_of_list[1]) + len(self.list_of_list[2])

    def __iter__(self):
        self.counter = 0
        self.counter1 = 0
        self.main_counter = 1
        return self

    def __next__(self):
        if self.main_counter <= self.end:
            self.main_counter += 1
            if self.counter < self.length:
                if self.counter1 < len(self.list_of_list[self.counter]):
                    item = self.list_of_list[self.counter][self.counter1]
                    self.counter1 += 1
                    return item
                else:
                    self.counter += 1
                    self.counter1 = 0
                    item = self.list_of_list[self.counter][self.counter1]
                    self.counter1 += 1
                    return item
        else:
            raise StopIteration

def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    test_1()
