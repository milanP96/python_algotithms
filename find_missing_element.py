import collections


def finder(arr1, arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        d[num] -= 1

    for num in d:
        print(d, num, d[num])
    print(d)
