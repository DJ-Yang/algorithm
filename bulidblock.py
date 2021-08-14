def product_exclusion2(args):
    length = len(args)
    result = []

    left_start = [1]
    right_start = [1]
    for i in range(length):
        left_start.append(left_start[i] * args[i])
        right_start.append(right_start[i] * args[length - i -1])

    for i in range(length):
        result.append(left_start[i] * right_start[length - i - 1])

    return result


print(product_exclusion2([2, 3, 4, 5]))