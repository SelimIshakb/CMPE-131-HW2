def sort_list(alist: list) -> list:
    n = len(alist)
    i = 0

    while i < n:
        j = 0
        while j < n-i-1:
            if alist[j] > alist[j+1]:
                temp = alist[j+1]
                alist[j+1] = alist[j]
                alist[j] = temp
            j += 1
        i += 1
    return alist
