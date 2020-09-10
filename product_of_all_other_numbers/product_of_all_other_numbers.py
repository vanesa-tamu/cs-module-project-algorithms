'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    new_arr = []
    for i in range(0, len(arr)):
        print(f'index i is at: {i}')
        # save index's value (old)
        old_value_i = arr[i]
        # change value to: 1
        arr[i] = 1
        # multiply all nums in arr and traverse
        result = 1
        for j in range(0, len(arr)):
            print(f'what is j value? {j} value is {arr[j]}')
            result = result * arr[j]
            print(f'result in j loop: {result}')
        new_arr.append(result)  # append result of j after loop
        # change value back to old value:
        arr[i] = old_value_i
    # return new array
    return new_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
