import random, json, os, time
import pandas as pd
from list import Bubble, Insert, Merge
from dotenv import load_dotenv

load_dotenv() # Load Enviorment

# Creat Arrays
randomlist, py_list, ins_list, Merge_list = [], [], [], []

# Start Time Measuring
measure_time = time.time()

# read/write file
def readfile(data_file):
    with open(data_file, "r") as f:
        data = json.load(f)
    return data

def writefile(data_file, data):
    with open(data_file, "w") as f:
        data = json.dump(data, f, indent=4)
    return data

data_file = "data/comparing.json"

setting = int(os.getenv('SETTING'))

# Calcualte lowest/highest time to get the average time for each number to be sorted
Min = 0.06376266479492188
Max = 0.09207344055175781

def Ins_Array(n):
    randomlist.append(n)
    py_list.append(n)
    ins_list.append(n)
    Merge_list.append(n)

# Generate Random Array
for i in range(0,setting):
    n = random.randint(0,setting)
    Ins_Array(n)

# Sort the random Arrays 
py_list.sort()
Final = Bubble(randomlist)
Insertion = Insert(ins_list)
MergeSort = Merge(Merge_list)

# Export Data to json file
read_data = {}
read_data["Py_sort"] = py_list
read_data["Bubble"] = Final
read_data["Insert"] = Insertion
read_data["Merge"] = MergeSort

writefile(data_file, read_data)

# Get Stats
stats = {
    "Final": Final,
    "Time": time.time() - measure_time,
    "Average": Max - Min
}

print(pd.DataFrame(stats))

