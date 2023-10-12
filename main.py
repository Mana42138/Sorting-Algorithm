import sys
import getopt
import random
import pandas as pd
from list import Bubble, Insert, Merge, Quick, PYSort
from dotenv import load_dotenv
from pygnuplot import gnuplot
from filesys import read, write

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
    main_list, randomlist, py_list, ins_list, Merge_list, Quick_list = [], [], [], [], [], []

    for i in range(0, int(Repeat_)):
            
        # Set Random Seed
        random.seed(int(Seed_))

        setting = int(Amount_)

        # Generate Random Array

        for i in range(0,setting):
            n = random.randint(0,setting)
            main_list.append(n)

        # Sort the random Arrays
        if Algorithm_ == "1":
            print("Python Sort")
            PYSort(main_list)
        elif Algorithm_ == "2":
            print("Bubble Sort")
            Final = Bubble(main_list)
        elif Algorithm_ == "3":
            print("Insert Sort")
            Insertion = Insert(main_list)
        elif Algorithm_ == "4":
            print("Merge Sort")
            MergeSort = Merge(main_list)
        elif Algorithm_ == "5":
            print("Quick Sort")
            QuickSort = Quick(main_list)

if __name__ == "__main__":
   main(sys.argv[1:])