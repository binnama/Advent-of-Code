
def read_file_to_lists(inputfile):
    file = open(inputfile, "r")
    data = file.read()
    data_into_list = data.split("\n")
    data_into_list = data_into_list.split(" ")
    return data_into_list

def create_two_separate_lists(datalist):
    listLeft = []
    listRight = []
    counter = 0
    for element in datalist:
        if counter % 2 == 0:
            listLeft.append(element)
            counter = counter + 1
        else:
            listRight.append(element)
            counter = counter + 1

    return listLeft, listRight


def main():
    list = read_file_to_lists("dummyList.txt")
    print(f"List after reading from file: {list}")
    left, right = create_two_separate_lists(list)
    print(f"List1: {left}, List2: {right}")

main()
