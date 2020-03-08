import re


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def get_list_names(path):
    with open(path, encoding='utf-8') as file:
        text = file.readline()
    list_names = list()
    while True:
        match = re.search(r'\"\w*\"', text)
        if match:
            list_names.append(text[match.start() + 1:match.end() - 1])
            text = text[match.end():]
        else:
            break
    return quick_sort(list_names)