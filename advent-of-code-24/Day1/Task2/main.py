from collections import Counter

def read_file_to_list(inputfile):
    file = open(inputfile, "r")
    data = file.read()
    data = data.split()
    return data

def create_separate_lists(datalist):
    listLeft = []
    listRight = []
    counter = 0

    for element in datalist:
        if counter % 2 == 0:
            listLeft.append(int(element))
            counter = counter + 1
        else:
            listRight.append(int(element))
            counter = counter + 1

    return listLeft, listRight

def similarity_counter(left, right):
    countedRight = Counter(right)
    sum = []
    coordList = []
    valueList = []

    for coord, value in countedRight.items():
        print(coord)
        coordList.append(coord)
        valueList.append(value)

    print(coordList)
    for element in left:
        if coord in left:
            sum.append(value)
        else:
            sum.append(0) 
    return sum
                
def main():
    list = read_file_to_list("dummyList.txt")
    #list = read_file_to_list("locations.txt")
    left, right = create_separate_lists(list)
    sum = similarity_counter(left, right)
    print(f"Sum: {sum}")

main()
