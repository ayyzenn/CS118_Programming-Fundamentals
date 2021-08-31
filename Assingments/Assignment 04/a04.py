### YOUR CODE FOR openLocks() FUNCTION GOES HERE ###
def f(x):
    a = 2                                                        
    counter = 1
    while a<=x:
        if x%a==0:
            counter = counter +1
            a = a+1
        else :
            a = a+1
    return counter


def openLocks(number_of_lockers,number_of_students):
    if number_of_lockers<0 or number_of_students<0:
        return None
    if number_of_lockers ==0 or number_of_students ==0:
        return 0
    counter = 0
    for i in range (1,number_of_lockers+1):
        a = f(i)
        if not(a%2==0):
            counter = counter+1
        else:
            continue
    return counter




#### End OF MARKER





### YOUR CODE FOR mostTouchableLocker() FUNCTION GOES HERE ###
def mostTouchableLocker(number_of_lockers,number_of_students):
    if number_of_lockers<0 or number_of_students<0:
        return None
    if number_of_lockers ==0 or number_of_students ==0:
        return 0
    counter = 0
    b = 0
    for i in range (1,number_of_lockers+1):
        a = f(i)
        if a>=b:
            counter = i
            b = a
    return counter



#### End OF MARKER


