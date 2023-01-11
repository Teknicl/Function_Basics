# Question 1
def countdown(num):
    for series in range(num,-1,-1):
        print(series)

countdown(10)


# Question 2
def prnReturn(a,b):
    print(a)
    return b

print(prnReturn(5,10))


# Question 3
def firstPlusLength(arrs):
    x = len(arrs)
    print(arrs[0]+x)

arrs = [9,2,3,4,5]
firstPlusLength(arrs)

# Question 4
arr = [5,7,9,11,12,14,15,3,4,25,100]

def valuesGreater(num):
    # pass
    newList1 = []
    for x in num:
        if x > num[1]:
            newList1.append(x)
    
    count = len(newList1)
    print("There are {} elements in the array.".format(count))
    print("See for yourself {}".format(newList1))

    lessthan2 = (count < 2)
    print(f"Are there less than 2 elements? {lessthan2}")

valuesGreater(arr)

# Question 5
def lengthValue(a,b):
    for x in range(a):
        print(b)

lengthValue(5,10)