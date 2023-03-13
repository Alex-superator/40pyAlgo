
def insertSort(lst):
    for i in range(1, len(lst)):
        j = i - 1
        nextElement = lst[i]
        while (lst[j] > nextElement) and (j >= 0):
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = nextElement
    print(lst)
