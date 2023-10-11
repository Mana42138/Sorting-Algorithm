
def Bubb(array):
    """
    array: An array consisting of numbers and it will sort it with the Bubble Algorithm
    """
    for i in range(len(array)):
        swapped = False
        for k in range(0, len(array) - i - 1):
            if array[k] > array[k + 1]:
                temp = array[k]
                array[k] = array[k + 1]
                array[k + 1] = temp
                swapped = True
    
        if not swapped:
            continue
    return array

