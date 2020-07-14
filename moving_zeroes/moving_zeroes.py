'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    filtered_arr = list(filter(lambda item: item != 0, arr))
    filtered_arr.extend([0] * (len(arr) - len(filtered_arr)))
    return filtered_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
