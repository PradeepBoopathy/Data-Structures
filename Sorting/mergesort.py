def merge_sort(a):
    if len(a) <=1:
        return a
    mid = len(a)//2
    l = a[:mid]
    r = a[mid:]
    
    l = merge_sort(l)
    r = merge_sort(r)
    
    return mergesort_two_sorted(l,r)
        

def mergesort_two_sorted(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i,j = 0,0
    
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1
    
    #leftouts
    
    while i <len_a:
        sorted_list.append(a[i])
        i+=1
    while j < len_b:
        sorted_list.append(b[j])
        j+=1
    return sorted_list
    
a = [1,2,3,8,4,5,6,7,9]

print(merge_sort(a))
