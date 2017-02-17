##### Practice for Coursera: Algorithm Part I by Robert Sedgewick @ Princeton
## Quick-union to determine connectivity
# based on a series of inputs, return connected components
## process the inputs to allow inaccuracy
# find the first two numbers contained in the inputs as the connected pair


import random

def generate_pair_set(length, probability):
    pair_set = {}
    length = int(length)
    probablity = float(probability)
    square = []
    for i in range(length):
        if i == length-1:
            for j in range(length):
                if j != length-1:
                    pair_set[[i,j],[i,j+1]] = 0
        else:
            for j in range(length):
                if j != length-1:
                    pair_set[[i,j],[i+1,j]] = 0
                    pair_set[[i,j],[i,j+1]] = 0
                else:
                    pair_set[[i,j],[i+1,j]] = 0
    clip_length = int(probability * len(pair_set))
    clip = random.sample(pair_set, clip_length)
    for item in clip:
        pair_set[item] = 1
    return pair_set
    
def generate_node_code(length):
    node_code_set = {}
    for i in range(length):
        for j in range(length):
            node_code_set[[i,j]] = i*10+j+1
    return node_code_set

def generate_connect_set(length, probability):
    pair_set = generate_pair_set(length, probability)
    node_code_set = generate_node_code(length)
    for item in pair_set:
        if pair_set[item] == 1:
            acode = node_code_set[item[0]]
            bcode = node_code_set[item[1]]
            tuple_input([acode,bcode])
            
def check_connect(acode, bcode):
    if get_root(acode) == get_root(bcode):
        return True
    else:
        return False
        
def check_perculation(connect_set):
    flag = False
    for j in range(length):
        for k in range(length):
            acode = node_code_set[[0,j]]
            bcode = node_code_set[[9,k]]
            if check_connect(acode,bcode):
                flag = True
    return flag
    

def get_root(item):
    # find the root of a node
    # the root of an unconnected node is the node itself
    global connect_dict
    if item in connect_dict:
        tmp = item
        while True:
            if tmp == connecct_dict[tmp]:
                break
            else:
                tmp = connect_dict[tmp]
        return tmp
    else:
        return False
        

def tuple_input(inp):
    # update the global dict of numbers and their ids
    # assign the root of a[0] to the root of a[1] 
    # if a[0] not in global dict, add a[0] into dict first, the id value of which is a[0] itself
    # if a[1] not in global dict, add a[1] into dict first, the id value of which is a[0]
    # note: do not change the dict directly while accessing the elements in the dict
    global connect_dict
    a = (inp[0], inp[1])
    if not connect_dict.has_key(a[0]):
        connect_dict[a[0]] = a[0]
    if connect_dict.has_key(a[1]):
        aroot = get_root(a[0])
        broot = get_root(a[1])
        connect_dict[broot] = aroot
        del aroot, broot
    else:
        aid = a[0]
        connect_dict[a[1]] = aid
        del aid
  


if __name__ == "__main__":
    connect_dict = {}
    square_length = raw_input("Please Enter the Size of the Square:")
    square_prob = raw_input("Please Enter the Probability of Open Gate:")
    connect_set = generate_connect_set(square_length, square_prob)
    open = check_perculation(connect_set)
    if open:
        print "Open Gate."
    else:
        print "Closed Gate."
    
        
        
            
        
    
