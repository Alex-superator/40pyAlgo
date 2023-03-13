def bubbleSort(lst):
    """

    :param lst: 

    """
    lastElementIndex = len(lst) - 1
    for passNum in range(lastElementIndex, 0, -1):
        for idx in range(passNum):
            if lst[idx] > lst[idx+1]:
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
    return lst
