def Ins(array):
    """
        array: An array consisting of numbers and it will sort it with the Insertion Algorithm
    """
    for i in range(0, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key
    return array