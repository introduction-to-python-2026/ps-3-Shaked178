def move(my_list, direction):
    index = my_list.index(1)
    result = [0] * len(my_list)

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

    return result




