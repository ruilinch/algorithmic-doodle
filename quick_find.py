##### Practice for Coursera: Algorithm Part I by Robert Sedgewick @ Princeton
## Quick-find for determining connectivity
# based on a series of inputs, return connected components
## process the inputs to allow inaccuracy
# find the first two numbers contained in the inputs as the connected pair

def tuple_input(inp):
    # update the global dict of numbers and their ids
    # assign the id of a[0] to a[1] and all its connected points 
    # if a not in global dict, add a into dict first, the id value of which is the length of the dict plus 1
    # note: do not change the dict directly while accessing the elements in the dict
    global num_dict
    a = (inp[0], inp[1])
    if not num_dict.has_key(a[0]):
        num_dict[a[0]] = len(num_dict) + 1 
    if num_dict.has_key(a[1]):
        aid = num_dict.get(a[0])
        bid = num_dict.get(a[1])
        for item in num_dict:
            if num_dict.get(item) == bid:
                num_dict[item] = aid
        del aid, bid
        
    else:
        aid = num_dict.get(a[0])
        num_dict[a[1]] = aid
        del aid
        
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
    
def print_components(a_dict):
    b_dict = a_dict.copy()
    for item in b_dict:
        print "number ", item, "has id ", b_dict[item]
    

if __name__ == "__main__":
    num_dict = {}
    while True:
        pair = raw_input("Please Enter a Pair of Numbers to be Connected:")
        pair = get_digits(pair)
        if pair:
            tuple_input(pair)
            print_components(num_dict)
            
        
    
