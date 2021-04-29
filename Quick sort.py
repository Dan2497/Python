def quick_sort(sequence):
    length = len(sequence)
    #if the list is length 0 or 1, it is sorted - return the list
    if length <= 1:
        return sequence
    #remove the last element from the list to use as a pivot
    pivot = sequence.pop()

    #create two new empty lists
    items_greater = []
    items_lower = []

    #go through the elements in the main list, put them in lower or greater when compared with pivot    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    #recursive call to each smaller list to carry out quick sort
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([5,6,7,8,9,8,7,6,5,6,7,8,9,0]))
