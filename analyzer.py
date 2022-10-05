import time #import time module
from stringdata import get_data #import get_data method from stringdata.py

def binary_search(container: "tuple[str]", element: str): #takes list parameter named container, and string parameter named element

    low = 0 #creates variable for low value
    high = len(container) #creates variable for high value sets to length of container

    while (low < high): #while low is less than high, set mid value to average of mid and high

        mid = int((high - low) / 2 + low)

        if (container[mid] == element): #checks to see is value at index mid is equal to element, if so return mid
            return mid
        elif (element > container[mid]): #checks to see is elemenet is greater than elemenet at index mid, if so new low is set
            low = mid + 1
        else: #if element is not greaeter than value at index mid, set new high
            high = mid

    return -1 #if element is never found return -1

def linear_search(container: "tuple[str]", element: str): #takes list parameter named container, and string parameter named element

    for index in range(len(container)): #loops as many times as there are elements in contaier
        if container[index] == element: #check each vakue one by one starting with index 0
            return index #if value at specifc index equals element, return index
        
    return -1 #if no value is found return -1




if __name__ == '__main__':
    container = get_data()

    print("Looking for not_here with binary search")
    start = time.time()
    index = binary_search(container,"not_here")
    end = time.time()
    print("Found at index: ", index)
    print("Time taken: ", end - start)

    print()

    print("Looking for mzzzz with binary search")
    start = time.time()
    index = binary_search(container, "mzzzz")
    end = time.time()
    print("Found at index: ", index)
    print("Time taken: ", end - start)

    print()

    print("Looking for aaaaa with binary search")
    start = time.time()
    index = binary_search(container, "aaaaa")
    end = time.time()
    print("Found at index: ", index)
    print("Time taken: ", end - start)

    print()

    print("Looking for not_here with linear search")
    start = time.time()
    index = linear_search(container, "not_here")
    end = time.time()
    print("Found at index: ", index)
    print("Time taken: ", end - start)

    print()

    print("Looking for mzzzz with linear search")
    start = time.time()
    index = linear_search(container, "mzzzz")
    end = time.time()
    print("Found at index: ", index)
    print("Time taken: ", end - start)

    print()

    print("Looking for aaaaa with linear search")
    start = time.time()
    index = linear_search(container, "aaaaa")
    end = time.time()
    print("Found at index: ", index)
    print("Time taken: ", end - start)
