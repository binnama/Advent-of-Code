def read_file_to_lists(inputfile):
    file = open(inputfile, "r")
    data = file.read()
    data = data.split()
    return data

def create_two_separate_lists(datalist):
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

def calculate(left, right):
    left.sort()
    right.sort()

    distances = [abs(a - b) for a, b in zip(left, right)]
    print(distances)
    sum = 0
    for number in distances:
        sum += number
    return sum

def main():
    list = read_file_to_lists("locations.txt")
    left, right = create_two_separate_lists(list)
    sum = calculate(left, right)
    print(f"Sum: {sum}")

main()
