""" Given input array of length n, sort it via the merge-sort algorithm"""

def merge(left, right):
    """Merge two sorted arrays named left and right"""
    merged = []
    i, j = 0, 0
    for _ in range(len(left) + len(right)):
        if i < len(left) and j < len(right):
            if right[j] > left[i]:
                # print("i:", left[i])
                merged.append(left[i])
                i += 1
            elif left[i] >= right[j]:
                # print("j:", right[j])
                merged.append(right[j])
                j += 1
            else:
                pass
        elif i >= len(left):
            merged.append(right[j])
            j += 1
        elif j >= len(right):
            merged.append(left[i])
            i += 1
        else:
            pass
    print("Merged:", merged)
    return merged

def split(array):
    if len(array) % 2 == 0:
        L = array[0:int(len(array) / 2)]
        R = array[int(len(array) / 2):]
    else:
        L = array[0:int(1 + len(array) // 2)]
        R = array[int(1 + len(array) // 2):]
    return L, R

def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        L, R = split(array)
        print(f"L: {L} R: {R}")
        left = merge_sort(L)
        right = merge_sort(R)
        return merge(left, right) 

test = [1,9,4,3,2,13,0,15,19,11,5]
print(merge_sort(test))
