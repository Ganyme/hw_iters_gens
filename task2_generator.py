import types

def flat_generator(list_of_list):
    end = len(list_of_list[0]) + len(list_of_list[1]) + len(list_of_list[2])
    main_counter = 1
    counter = 0
    counter1 = 0
    while main_counter <= end:
        if counter < len(list_of_list):
            if counter1 < len(list_of_list[counter]):
                item = list_of_list[counter][counter1]
                counter1 += 1
                yield item
            else:
                counter += 1
                counter1 = 0
                item = list_of_list[counter][counter1]
                counter1 += 1
                yield item
        main_counter += 1

def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()