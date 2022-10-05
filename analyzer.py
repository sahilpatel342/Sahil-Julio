import timeit
from stringdata import get_data
def linear_search(container: "tuple[str]", element: str):
    for i in range(len(container) - 1):
        if container[i] == element:
            return i
        else:
            i += 1
    return -1

def binary_search(container: "tuple[str]", element: str):
    bot_index = 0
    top_index = len(container)-1
    while bot_index <= top_index:
        mid_index = int((bot_index + top_index) / 2)
        if container[mid_index] < element:
            bot_index = mid_index + 1
        elif container[mid_index] > element:
            top_index = mid_index - 1
        else:
            return mid_index
    return -1

if __name__ == '__main__':
    container = get_data()
    #The element will be 'not_here'
    start_linear = timeit.default_timer()
    print(linear_search(container, "not_here"))
    end_linear = timeit.default_timer()
    start_binary = timeit.default_timer()
    print(binary_search(container, "not_here"))
    end_binary = timeit.default_timer()
    print(start_linear - end_linear, start_binary - end_binary)
    #The element will be 'not_here'
    start_linear = timeit.default_timer()
    print(linear_search(container, "aaaaa"))
    end_linear = timeit.default_timer()
    start_binary = timeit.default_timer()
    print(binary_search(container, "aaaaa"))
    end_binary = timeit.default_timer()
    print(start_linear-end_linear, start_binary-end_binary)
    #The element will be 'mzzzz'
    start_linear = timeit.default_timer()
    print(linear_search(container, "mzzzz"))
    end_linear = timeit.default_timer()
    start_binary = timeit.default_timer()
    print(binary_search(container, "mzzzz"))
    end_binary = timeit.default_timer()
    print(start_linear - end_linear, start_binary - end_binary)