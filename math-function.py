import time 
import csv
import numpy as np
import random

# implement mathematical functions

def greatCommonDivisor(p, q):
    # return the greatest common divisor between two integers p and q
    # Euclid's Algorithm
    if q == 0:
        return p
    else:
        r = p%q
        return greatCommonDivisor(q,r)
        
def getMax(numlist):
    # return the largest item in a list of numbers
    maxvalue = numlist[0]
    for i in range(len(numlist)-1):
        if maxvalue < numlist[i+1]:
            maxvalue = numlist[i+1]
    return maxvalue
    
    
    
    
def getAverage(numlist):
    # return the average value of a list of numbers
    meanvalue = 0.0
    for item in numlist:
        meanvalue += item
    meanvalue /= len(numlist)
    return meanvalue
    
    
    
    
def reverseArray(array):
    # put the elements of a list in reverse order
    # Note i <-> N-i-1, not N-i
    listlength = len(array)
    for i in range(listlength/2):
        tmp = array[i]
        array[i] = array[listlength-i-1]
        array[listlength-i-1] = tmp
    return array
    
    
    
def matrixMultiply(a,b):
    # multiply two matrixes a[m][n] and b[n][m]
    # a and b are numpy matrix
    a_size = np.shape(a)
    b_size = np.shape(b)
    if a_size[1] != b_size[0]:
        print "Error! Matrix size mismatch."
        return -1
    else:
        matrix = []
        for i in range(a_size[0]):
            ivalue = []
            for j in range(b_size[1]):
                ijValue = 0
                for k in range(a_size[1]):
                    ijValue += a[i, k]*b[k,j]
                ivalue.append(ijValue)
            matrix.append(ivalue)
        return matrix
        
        
def absValue(a):
    # return the absolute value of a
    if a >= 0:
        return a
    else:
        return (-a)  
        
        
        
def sqrt(a, digit):
    # return the square value of a with a certain number of digits
    t = a*1.0
    digit = int(digit)
    accuracy = 1.0
    for i in range(digit*2):
        accuracy /= 10.0
    while absValue(t - a/t) >= accuracy * t:
        tmp = t
        t = (tmp + a/tmp)/2.0
    string = "%."+str(digit)+"f"
    trough = round(t,digit)
    return trough
    
    
def shuffle(array):
    # randomly shuffle an array
    length = len(array)
    for i in range(length-1):
        pos = int((length-i) * random.random() + i)
        tmp = array[i]
        array[i] = array[pos]
        array[pos] = tmp
    return array
    

def matrixTranspose(a):
    matrix = []
    a = np.matrix(a)
    a_size = np.shape(a)
    for j in range(a_size[1]):
        jvalue = []
        for i in range(a_size[0]):
            jvalue.append(a[i,j])
        matrix.append(jvalue)
    return matrix


def get_digits(inp):
    # inp is a string input
    # process the input so that numbers are separated by "," for convenient split
    # get the digits contained in this string, which is treated as connected pair to be processed        
    pos = []
    for i in range(len(inp)):
        if not inp[i].isdigit():
            pos.append(i)   
    rinp = ''   
    for i in range(len(inp)):
        if i in pos:
            rinp += ","
        else:
            rinp += str(inp[i])
    digits = [int(s) for s in rinp.split(",") if s.isdigit()]
        
    if len(digits) >= 2:
        return digits
    else:
        return False
    
    
if __name__ == "__main__":
    t0 = time.time()
    array = [random.randint(-500,500) for i in range(10)]
    print "array is ", array
    print "in reverse order is ", reverseArray(array)
    print "maximum value is ", getMax(array)
    print "average value is ", getAverage(array)
    print "after random shuffle, the array becomes ", shuffle(array) 
    pair = raw_input("Please enter the rank of two numbers:")
    pair = get_digits(pair)
    print "greatCommonDivisor between", array[pair[0]], " and ", array[pair[1]], " is ", \
              greatCommonDivisor(array[pair[0]], array[pair[1]])
    print "the sqrt roots of their absolute values are", sqrt(absValue(array[pair[0]]), 2), \
            " and ", sqrt(absValue(array[pair[1]]),2)
    print "the sum of ", absValue(array[pair[0]]), " and ", -absValue(array[pair[0]]), "is 0"
    matrix1 = []
    matrix2 = []
    for i in range(5):
        a = [1 for i in range(7)]
        b = shuffle(a)
        matrix1.append(a)
        matrix2.append(b)
    matrix2 = matrixTranspose(matrix2)
    
    matrix1 = np.matrix(matrix1)
    matrix2 = np.matrix(matrix2)
    print "matrix1:", matrix1
    print "shape", np.shape(matrix1)
    print "matrix2", matrix2
    print "shape", np.shape(matrix2)
    matrixresult = np.matrix(matrixMultiply(matrix1, matrix2))
    print "matrix multiply",matrixresult
    print "shape", np.shape(matrixresult)
    t1 = time.time()
    print "Time consumed:", "%.2fs"%(t1-t0)
    
    

    




















    




            
            
    

    
    