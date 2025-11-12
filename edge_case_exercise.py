def move(my_list, direction):
    index = my_list.index(1)
    result = [0] * len(my_list)
    
    if direction == 'left' and index > 0:
        result[index - 1] = 1
    elif direction == 'right' and index < len(my_list) - 1:
        result[index + 1] = 1
    
    return result



