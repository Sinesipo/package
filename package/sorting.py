def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    length = len(items) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if items[i] > items[i+1]:
                sorted = False
                items[i], items[i+1] = items[i+1], items[i]
    return items



def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    if len(items) < 2:
        return items

    array,mid = [],int(len(items)/2)

    x = merge_sort(items[:mid])
    y = merge_sort(items[mid:])

    while (len(x) > 0) and (len(y) > 0):
            if x[0] > y[0]:array.append(y.pop(0))
            else:array.append(x.pop(0))

    array.extend(x+y)
    return array


def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    if items:
        x = [i for i in items[1:] if i < items[0]]
        y = [i for i in items[1:] if i >= items[0]]
        z = quick_sort(x) + [items[0]] + quick_sort(y)
        return z
    else:
        return items
