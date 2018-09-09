"""
    module bubble_sort
"""
def bubble_sort(my_list):
    """
        function bubble_sort
    """
    for elem in range(len(my_list)-1, 0, -1):
        for i in range(elem):
            if my_list[i] > my_list[i+1]:
                temp = my_list[i]
                my_list[i] = my_list[i+1]
                my_list[i+1] = temp

ALIST = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(ALIST)
print(ALIST)
