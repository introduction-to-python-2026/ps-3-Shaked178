def move(my_list, direction):
    index = my_list.index(1)
    result = my_list[:]
    result[index] = 0

    if direction == 'left':
        if index > 0:
            result[index - 1] = 1
        else:
            result[index] = 1
    elif direction == 'right':
        if index < len(my_list) - 1:
            result[index + 1] = 1
        else:
            result[index] = 1
    else:
        raise ValueError("Direction must be 'left' or 'right'")

    return result
