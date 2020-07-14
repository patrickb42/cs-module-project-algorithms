'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    j = len(arr) - 1
    for index, item in enumerate(arr):
        if index > j:
            break
        if item == 0:
            while arr[j] == 0 and j > index:
                j -= 1
            if index < j:
                arr[index] = arr[j]
                arr[j] = 0
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
