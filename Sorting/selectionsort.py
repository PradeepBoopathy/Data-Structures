def selection_sort(A):
    for i in range(len(A)):
        k = i
        for j in range(i+1, len(A)):
            if A[k] > A[j]:
                k = j
        A[i], A[k] = A[k], A[i]


a = [1,2,3,8,4,5,6,7,9]
selection_sort(a)
print(a)
