'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # for loop
    if 0 not in arr:
        return arr
    else:
        for i in arr:
            # check if i != 0
            if i != 0:
                #  pop & move to the front of the array
                old_value = arr[i]
                arr.pop(i)
                arr.insert(0, old_value)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")