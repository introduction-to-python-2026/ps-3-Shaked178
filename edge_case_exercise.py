def move(my_list, direction):
    index = my_list.index(1)

    if direction == 'left' and index > 0:
        my_list[index], my_list[index - 1] = 0, 1
    elif direction == 'right' and index < len(my_list) - 1:
        my_list[index], my_list[index + 1] = 0, 1

    return my_list



