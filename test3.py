class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.flattened_list = []
        self.__flatten(self.list_of_list)

    def __flatten(self, nested_list):
        for item in nested_list:
            if isinstance(item, list):
                self.__flatten(item)
            else:
                self.flattened_list.append(item)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):        
        while self.index < len(self.flattened_list):
            item = self.flattened_list[self.index]
            self.index += 1
            return item
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_2),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()