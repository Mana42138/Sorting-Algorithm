from sorting.Bubble import Bubb
from sorting.Insertion import Ins
from sorting.Merge import merge_sort
from sorting.Quick import QuickSort
def Bubble(array):
    return Bubb(array)

def Insert(array):
    return Ins(array)

def Merge(array):
    return merge_sort(array)

def Quick(array):
    return QuickSort(array, len(array) - 1)