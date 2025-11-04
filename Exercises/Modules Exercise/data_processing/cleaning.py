def remove_duplicates(a_list: list):
    new_list = []
    for i in a_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

