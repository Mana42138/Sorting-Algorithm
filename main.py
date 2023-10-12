import sys, getopt
import random, json, os, time
import pandas as pd
from list import Bubble, Insert, Merge, Quick, PYSort
from dotenv import load_dotenv
from pygnuplot import gnuplot

load_dotenv() # Load Enviorment

def main(argv):
    Algorithm_ = ''
    Amount_ = ''
    Seed_ = ''
    Repeat_ = ''
    options, arguments = getopt.getopt(sys.argv[1:], "ha:l:s:r:", ["help", "algorithm", "length", "seed", "repeat"])
    for opt, arg in options:
        if opt in ("-h", "--help"):
            print('main.py\n -a Choose Algorithm\n 1: Python\n 2: Bubble Sort\n 3: Insert Sort\n 4: Merge Sort\n 5: Quick Sort\n -l <List Length> \n -s <seed> \n -r <repeat : 2>')
            sys.exit()
        elif opt in ("-a", "--algorithm"):
            Algorithm_ = arg
        elif opt in ("-l", "--length"):
            Amount_ = arg
        elif opt in ("-s", "--seed"):
            Seed_ = arg
        elif opt in ("-r", "--repeat"):
            Repeat_ = arg

    # Algorithm_ = input("Select Algorithm 1, 2, 3, 4, 5: ")
    # Amount_ = input("Amount: ")

    # Creat Arrays
    randomlist, py_list, ins_list, Merge_list, Quick_list = [], [], [], [], []

    for i in range(0, int(Repeat_)):
            
        # Set Random Seed
        random.seed(int(Seed_))
        
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

        setting = int(Amount_) # int(os.getenv('SETTING'))
        
        # Calcualte lowest/highest time to get the average time for each number to be sorted
        Min = 0.06376266479492188
        Max = 0.09207344055175781

        def Ins_Array(n):
            randomlist.append(n)
            py_list.append(n)
            ins_list.append(n)
            Merge_list.append(n)
            Quick_list.append(n)

        # Generate Random Array
        for i in range(0,setting):
            n = random.randint(0,setting)
            Ins_Array(n)

        # Sort the random Arrays
        if Algorithm_ == "1":
            print("Python Sort")
            PYSort(py_list)
        elif Algorithm_ == "2":
            print("Bubble Sort")
            Final = Bubble(randomlist)
            # print(Final)
        elif Algorithm_ == "3":
            print("Insert Sort")
            Insertion = Insert(ins_list)
        elif Algorithm_ == "4":
            print("Merge Sort")
            MergeSort = Merge(Merge_list)
        elif Algorithm_ == "5":
            print("Quick Sort")
            QuickSort = Quick(Quick_list)

        # Export Data to json file
        # read_data = {}
        # read_data["Py_sort"] = py_list
        # read_data["Bubble"] = Final
        # read_data["Insert"] = Insertion
        # read_data["Merge"] = MergeSort
        # read_data["Quick"] = QuickSort

        # writefile(data_file, read_data)

        # # Get Stats
        # stats = {
        #     "Final": Final,
        #     "Time": time.time() - measure_time,
        #     "Average": Max - Min
        # }

        # print(pd.DataFrame(stats))

if __name__ == "__main__":
   main(sys.argv[1:])