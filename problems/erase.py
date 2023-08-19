def erase_elements(lst):
    new_lst = []
    for sub_lst in lst:
        valid = True
        for num in sub_lst:
            if len(sub_lst) != len(str(num)):
                valid = False
                break
        if valid:
            new_lst.append(sub_lst)
    return new_lst

# Example usage
lst = [[123, 123, 123], [], [145, 145], [157], [169, 169, 169], []]
result = erase_elements(lst)
print(result)
