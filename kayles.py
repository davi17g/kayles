__author__ = 'david'

''' minimum excluded value just like it defined in the book!'''
def mex (sub):
    vec = sorted(sub)
    if vec[0]!=0:
        return 0
    if len(vec)==1:
        return 0
    for i in range(len(vec)-1):
        A = vec[i+1]
        B = vec[i]
        if A-B !=1 and A-B !=0:
            return B+1
    return vec[-1]+1

'''
we use this function because we want to know which values are directly connected to zero
and then we treat them also as zeros
'''
def isTransitiveZero(n):
    if n == 1 or n==2:
        return True
    return False
'''
this function gets n (some natural number) and table of previous grudy values
here we use Dynamic Programming in order to calculate the next grudy value called nimber
'''
def grudy_fun(n,table):
    sub = []
    for i in range(n-1):
        A = i
        B = n-i-1
        sum = table[A] ^ table[B]
        sub.append(sum)
        if isTransitiveZero(sum):
            sub.append(0)
    for j in range(0,n-1):
        A = j
        B = n-j-2
        sum = table[A] ^ table[B]
        if isTransitiveZero(sum):
            sub.append(0)
        sub.append(sum)
    return sub

'''
this is spurge grudy function for kayles in order to use it to
other impartial game we must re-define grudy_fun function and
also we may change our initial group (table)
'''


def spurge_grudy(nim):
    table = [0,1,2]
    for i in range(3,nim):
        a = grudy_fun(i,table)
        b = mex(a)
        table.append(b)
    return table

'''
this function returns a sequence of sizes of gaps between same nimbers I saw some patterns in the 
sequence a specially for large n values, but couldn't figure the exact formula as Nivash asked us.
I will continue to work on that

'''

def frequency(number):
    t = spurge_grudy(1000)
    print(len(t))
    f = []
    for i in range(len(t)):
        if t[i] == number:
            f.append(i)
            break
    print(f)
    for i in range(f[0]+1,len(t)):
        if t[i] == number:
            f.append(i-f[-1])
    return f


'''
Here I am process all the functions from above
'''
print(frequency(1))
