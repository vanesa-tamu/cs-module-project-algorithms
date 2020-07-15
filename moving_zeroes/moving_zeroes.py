'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    if 0 not in arr:
        return arr
    else:
        for i in range(len(arr)):
            # check if i != 0
            if arr[i] != 0:
                #  pop & move to the front of the array
                old_value = arr[i]
                arr.pop(i)
                arr.insert(0, old_value)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr1 = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr1)}")