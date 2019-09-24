# Bubblesort 101

# def: Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through 
# the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated 
# until the list is sorted.

def bubblesort(lst):
    for passes_left in range(len(lst)-1, 0, 1):
        for index in range(passes_left):
            if lst[index] > lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
    return lst
    

l=[27, 0, 23, 90, 71, 77]

print(bubblesort(l))


# credit @ chris@finxter.com
