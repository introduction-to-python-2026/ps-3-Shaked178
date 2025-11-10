# edge_case_exercise.py

def move(my_list, direction):
    """
    Moves the pig (1) left or right across a list of zeros.
    If movement would go out of bounds, the pig stays in place.

    Args:
        my_list (list): A list containing zeros and one 1.
        direction (str): Either 'left' or 'right'.

    Returns:
        list: A new list with the pig moved if possible.
    """
    # Find current position of the pig (1)
    index = my_list.index(1)

    # Create a copy to avoid mutating the original list
    result = my_list[:]
    result[index] = 0

    if direction == 'left':
        # Move left if not at the start
        if index > 0:
            result[index - 1] = 1
        else:
            result[index] = 1  # Stay in place
    elif direction == 'right':
        # Move right if not at the end
        if index < len(my_list) - 1:
            result[index + 1] = 1
        else:
            result[index] = 1  # Stay in place
    else:
        # Invalid direction input
        raise ValueError("Direction must be 'left' or 'right'")

    return result

