import random
import time

# compared to quick union, the weighted quick union can save about 1/2 running time.
# given weighted quick unoin, having path compression is only mildly quicker than otherwise. 

# For a square with a certain length and the probability of neighboring nodes being connected given
# Determine if the top of the square is connected with its bottom
# It is found that the threshold value is around 0.49
# When P > 0.49, the square is almost certainly connected. When P < 0.49, the square is almost certainly not connected. 

def generate_pair_set(length, probability):
    # correct
    # randomly add lines to nodes according to probability
    # return a dict containing (node1, node2):0/1
    pair_set = {}
    length = int(length)
    square = []
    for i in range(length):
        if i == length-1:
            for j in range(length):
                if j != length-1:
                    pair_set[(i,j),(i,j+1)] = 0
        else:
            for j in range(length):
                if j != length-1:
                    pair_set[(i,j),(i+1,j)] = 0
                    pair_set[(i,j),(i,j+1)] = 0
                else:
                    pair_set[(i,j),(i+1,j)] = 0
    clip_length = int(float(probability) * len(pair_set))
    clip = random.sample(pair_set, clip_length)
    for item in clip:
        pair_set[item] = 1
    check = 0
    for item in clip:
        check += pair_set[item]    
    return pair_set
    
def generate_node_code(length):
    # correct
    # create a dict to label each of elements in the matrix
    node_code_set = {}
    for i in range(int(length)):
        for j in range(int(length)):
            node_code_set[(i,j)] = i*10+j+1
    return node_code_set


def generate_connect_set(length, probability):
    pair_set = generate_pair_set(length, probability)
    for item in pair_set:
        if pair_set[item] == 1:
            acode = node_code_set[item[0]]
            bcode = node_code_set[item[1]]
            add_connect(acode, bcode)
            
            
def add_connect(acode,bcode):
    
    global connect_dict
    if not acode in connect_dict:
        connect_dict[acode] = acode
    aroot = get_weighted_root(acode)    
    if bcode in connect_dict:
        broot = get_weighted_root(bcode)
        connect_dict[broot] = aroot
    else:
        connect_dict[bcode] = aroot 

def get_weighted_root(code):
    global connect_dict
    tmp = code
    root = connect_dict[code]
    while True:
        root = connect_dict[tmp]
        if root == tmp:
            break
        else:
            tmp = root
    return root
    
def check_percolation(connect_set, length):
    flag = False
    for j in range(int(length)):
        for k in range(int(length)):
            acode = node_code_set[(0,j)]
            bcode = node_code_set[(int(length)-1,k)]
            if (acode in connect_dict) and (bcode in connect_dict) and \
                (get_weighted_root(acode) == get_weighted_root(bcode)):
                flag = True
    return flag
        
if __name__ == "__main__":
#    square_length = int(raw_input("Please Enter the Size of the Square:"))
#    square_prob = float(raw_input("Please Enter the Probability of Open Gate:"))
    square_length = 100
    prob = [i/50.0 for i in range(50)]
    t0 = time.time() 
    for square_prob in prob:
        connect_dict = {}
        node_code_set= generate_node_code(square_length)
        connect_set = generate_connect_set(square_length, square_prob)
        open_gate = check_percolation(connect_set, square_length)
        if open_gate:
            print "square_prob", square_prob, "Open Gate."
        else:
            print "square_prob", square_prob, "Closed Gate."
    t1 = time.time()
    print "Time consumed", t1-t0
