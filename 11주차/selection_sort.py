def selection_sort(a):
    for i in range(0, len(a)-1):
        minimun = i
        for j in range(i, len(a)):
            if a[minimun] > a[j]:
                minimun = j
        a[i], a[minimun] = a[minimun], a[i]

