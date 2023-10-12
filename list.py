from sorting.Bubble import Bubb
from sorting.Insertion import Ins
from sorting.Merge import merge_sort
from sorting.Quick import QuickSort
from sorting.Py_sort import psort
def Bubble(array):
    return Bubb(array)

def Insert(array):
    return Ins(array)

def Merge(array):
    return merge_sort(array)

def Quick(array):
    return QuickSort(array, 0, len(array) - 1)

def PYSort(array):
    return psort(array)

