from sorting.Bubble import Bubb
from sorting.Insertion import Ins
from sorting.Merge import merge_sort
from sorting.Quick import QuickSort
from sorting.Py_sort import psort
from filesys.read import *
from filesys.write import *

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

def read(data_file):
    readfile(data_file)

def write(data_file, data):
    writefile(data_file, data)