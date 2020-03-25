"""
PROBLEM ONE

Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def function(array, k):
    end = array[len(array) - 1]
    bool = False
    while (bool == False):
        for value in array:
            temp = value
            for value in array:
                if (temp + value) == k:
                    bool = True
                    print("{0} + {1} is {2}".format(temp, value, k))
            if (temp == end) and bool == False:
                print('no possibility')
                bool = True

def set_array_and_k():
    length = int(input("size of array = "))
    k = int(input('target = '))
    array = []

    for i in range(length):
        array.append(int(input('element {0} = '.format(i+1))))

    return [array,k]



if __name__ == "__main__":
    array = set_array_and_k()
    function(array[0],array[1])  