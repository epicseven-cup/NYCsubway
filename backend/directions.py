#TODO:
# setup:
# 1 read the data
# 2 convert the data
# 3 read through the data

def readingCSV(filename):
    with open(filename,"r") as file:
        for line in file:
            print(line)