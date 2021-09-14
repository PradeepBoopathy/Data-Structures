def Linearsearch(elements,searchvalue):
    ind = []
    for i in range(len(elements)):
        if elements[i] == searchvalue:
            ind.append(i)
    return 'Not Found' if ind is None else ('Found at index:', ind)

if __name__ == '__main__':
    elements = [12, 15, 17, 19, 15, 23, 25, 27]
    search = 15
    l = Linearsearch(elements, search)
    print(l)
