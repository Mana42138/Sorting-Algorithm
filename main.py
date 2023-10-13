from list import *

load_dotenv() # Load Enviorment

def main(argv):
    Algorithm_ = ''
    Amount_ = ''
    Seed_ = ''
    Repeat_ = ''
    write_data = ''
    options, arguments = getopt.getopt(sys.argv[1:], "ha:l:s:r:d:", ["help", "algorithm", "length", "seed", "repeat", "data"])
    for opt, arg in options:
        if opt in ("-h", "--help"):
            print('main.py\n -a Choose Algorithm\n 1: Python\n 2: Bubble Sort\n 3: Insert Sort\n 4: Merge Sort\n 5: Quick Sort\n -l <List Length> \n -s <seed> \n -r <repeat 1> \n -d <write data 1>')
            sys.exit()
        elif opt in ("-a", "--algorithm"):
            Algorithm_ = arg
        elif opt in ("-l", "--length"):
            Amount_ = arg
        elif opt in ("-s", "--seed"):
            Seed_ = arg
        elif opt in ("-r", "--repeat"):
            Repeat_ = arg
        elif opt in ("-d", "--data"):
            write_data = arg

    # Creat Array(s)
    main_list = []

    for i in range(0, int(Repeat_)):
            
        # Set Random Seed
        random.seed(int(Seed_))

        setting = int(Amount_)

        # Generate Random Array

        for i in range(0,setting):
            n = random.randint(0,setting)
            main_list.append(n)

        Sorted_Array = ''
        Sort_name = ''
        
        # Sort the random Arrays
        if Algorithm_ == "1":
            print("Python Sort")
            Sort_name = "Python Sort"
            Sorted_Array = py_sort(main_list)
        elif Algorithm_ == "2":
            print("Bubble Sort")
            Sort_name = "Bubble Sort"
            Sorted_Array = Bubble_sort(main_list)
        elif Algorithm_ == "3":
            print("Insert Sort")
            Sort_name = "Insert Sort"
            Sorted_Array = Insert_sort(main_list)
        elif Algorithm_ == "4":
            print("Merge Sort")
            Sort_name = "Merge Sort"
            Sorted_Array = Merge_sort(main_list)
        elif Algorithm_ == "5":
            print("Quick Sort")
            Sort_name = "Quick Sort"
            Sorted_Array = Quick_sort(main_list, 0, len(main_list) - 1)

    if int(write_data) == 1:
        Status_Data = {
            "Algorithm": Sort_name,
            "Numbers": Sorted_Array
        }
        writefile("data/comparing.json", Status_Data)

if __name__ == "__main__":
   main(sys.argv[1:])