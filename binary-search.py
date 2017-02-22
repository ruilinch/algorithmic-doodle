import random
import time
import csv

# implement binary search 
# read one file called largeText.csv, another file called whitelist.csv, compare them and print those in largeText.csv that are included in whitelist.csv, and save it in a new file called filter.csv
# randomly generate largeText and whitelist


def readText(textname):
    title = str(textname)
    with open(title, "r") as f:
        content = csv.reader(f)
        text = list(content)
        text = text[0]
        for i in range(len(text)-1):
            item = text[i+1]
            text[i] = int(item)
        return text


def generateText():
    # generate two int lists of numbers randomly sampled from [100,200] for test
    large = [str(random.randint(100,200)) for i in range(10)]
    white = [str(random.randint(100,200)) for i in range(100)]
    
    largeText = stringOutput(large,"text")
    whitelist = stringOutput(white,"whitelist")
    
    fo1 = open("largeText.csv", "w")
    fo1.write(largeText)
    fo2 = open("whitelist.csv","w")
    fo2.write(whitelist)
    
    
def stringOutput(codelist, variable):
    result = str(variable) + ","  
    for i in range(len(codelist)-1):
        result += str(codelist[i]) + ","
    result += str(codelist[len(codelist)-1])  
    return result

    
def binarySearch(codelist, code, low, high):
    # find code between codelist[low] and codelist[high]
    # return position if found; otherwise, return -1. 
    # Note: codelist must be sorted. 
    hi = high
    lo = low 
    mid = 0
    found_flag = False
    for i in range(len(codelist)):
        if codelist[i] == "":
            del codelist[i]
    while not found_flag and lo <= hi:
        mid = lo + (hi-lo)/2
        if int(codelist[mid]) < int(code):
            lo = mid + 1
        elif int(codelist[mid]) > int(code):
            hi = mid - 1
        else:
            found_flag = True
            
    if found_flag:
        return mid
    else:
        return -1

        
if __name__ == "__main__":    
    t0 = time.time() 
    generateText()
    text = readText("largeText.csv")
    whitelist = readText("whitelist.csv")
    whitelist.sort()
    whitelistLength = len(whitelist)
    filterlist = []
    for item in text:
        if item != "":
            result = binarySearch(whitelist, item, 0, whitelistLength-1)
            if result < 0:
                filterlist.append(item)
                print item, "not found."
    
    output = stringOutput(filterlist, "filter")
    fo = open("filter.csv", "w")
    fo.write(output)
        
    t1 = time.time()
    print "Finished searching."
    print "Time consumed:", t1-t0
    

                
        
            
            

            
            
            

