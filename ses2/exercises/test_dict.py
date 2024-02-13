def test(actual, expected):
    assert actual == expected, f"Expected: {expected}, but got: {actual}"

def create_dict(keys, values):
    return dict(zip(keys, values))

def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

def get_value(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return 'Key not found'

def key_exists(dictionary, key):
    return key in dictionary

def update_value(dictionary, key, value):
    dictionary[key] = value
    return dictionary

def remove_key(dictionary, key):
    dictionary.pop(key, None)
    return dictionary

def dict_to_list(dictionary):
    return list(dictionary.items())

def main():
    print('create_dict')
    test(create_dict(['a', 'b', 'c'], [1, 2, 3]), {'a': 1, 'b': 2, 'c': 3})
    test(create_dict(['x', 'y', 'z'], ['cat', 'dog', 'bird']), {'x': 'cat', 'y': 'dog', 'z': 'bird'})
    test(create_dict([1, 2, 3], ['one', 'two', 'three']), {1: 'one', 2: 'two', 3: 'three'})
    print()

    print('merge_dicts')
    test(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}), {'a': 1, 'b': 3, 'c': 4})
    test(merge_dicts({'x': 'cat', 'y': 'dog'}, {'y': 'parrot', 'z': 'fish'}), {'x': 'cat', 'y': 'parrot', 'z': 'fish'})
    test(merge_dicts({1: 'one', 2: 'two'}, {3: 'three', 4: 'four'}), {1: 'one', 2: 'two', 3: 'three', 4: 'four'})
    print()

    print('get_value')
    test(get_value({'a': 1, 'b': 2}, 'b'), 2)
    test(get_value({'x': 'cat', 'y': 'dog'}, 'z'), 'Key not found')
    test(get_value({1: 'one', 2: 'two'}, 1), 'one')
    print()

    print('key_exists')
    test(key_exists({'a': 1, 'b': 2}, 'c'), False)
    test(key_exists({'x': 'cat', 'y': 'dog'}, 'x'), True)
    test(key_exists({1: 'one', 2: 'two'}, 3), False)
    print()

    print('update_value')
    test(update_value({'a': 1, 'b': 2}, 'b', 3), {'a': 1, 'b': 3})
    test(update_value({'x': 'cat', 'y': 'dog'}, 'y', 'parrot'), {'x': 'cat', 'y': 'parrot'})
    test(update_value({1: 'one', 2: 'two'}, 3, 'three'), {1: 'one', 2: 'two', 3: 'three'})
    print()

    print('remove_key')
    test(remove_key({'a': 1, 'b': 2}, 'a'), {'b': 2})
    test(remove_key({'x': 'cat', 'y': 'dog'}, 'z'), {'x': 'cat', 'y': 'dog'})
    test(remove_key({1: 'one', 2: 'two'}, 1), {2: 'two'})
    print()

    print('dict_to_list')
    test(dict_to_list({'a': 1, 'b': 2}), [('a', 1), ('b', 2)])
    test(dict_to_list({'x': 'cat', 'y': 'dog'}), [('x', 'cat'), ('y', 'dog')])
    test(dict_to_list({1: 'one', 2: 'two'}), [(1, 'one'), (2, 'two')])
    print()

if __name__ == "__main__":
    main()