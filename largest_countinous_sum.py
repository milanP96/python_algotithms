def large_cont_sum(arr):

    if len(arr) == 0:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum += num
        max_sum = max(max_sum, current_sum)
    print(max_sum)