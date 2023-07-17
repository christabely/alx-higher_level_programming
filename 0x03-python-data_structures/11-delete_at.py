def delete_at(my_list=None, idx=0):
    if my_list is None:
        my_list = []

    if 0 <= idx < len(my_list):
        del my_list[idx]

    return my_list

