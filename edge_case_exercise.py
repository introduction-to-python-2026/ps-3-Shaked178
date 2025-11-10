def move(my_list, direction):
    index = my_list.index(1)
    new_list = [0] * len(my_list)
    if direction == 'left' and index > 0:
        new_list[index - 1] = 1
    elif direction == 'right' and index < len(my_list) - 1:
        new_list[index + 1] = 1
    else:
        new_list[index] = 1
    return new_list

