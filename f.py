def reverse(x):#reverses the string
    return x[::-1]
def altswap(x): #swaps pairs of cosecutive characters:"abcdef">"badcfe"
    return "".join([x[2*i:2*i+2][::-1] for i in range(len(x))]) 
def halfswap(x): #splits the string in half and switches the parts: "abcdef">"defabc"
    return x[int(len(x)/2):]+x[:int(len(x)/2)]
def halfreverse(x): #splits string in half and reverses each part: "abcdef">"cbafed"
    return x[:int(len(x)/2)][::-1]+x[int(len(x)/2):][::-1]
def leftshift(x): #cyclic shift to the left:"abcdef">"bcdefa"
    return x[1:]+x[0]
def rightshift(x): #cyclic shift to the right: "abcdef">"fabcde"
    return x[-1]+x[:-1]
def MTmind(a,b): #returns a tuple (x,y); x=#of i's s.t a_i=b_i, y=#of i's s.t. a_i\in b
    return [sum([a[i]==b[i] for i in range(len(a))]),sum([a[i] in b for i in range(len(a))])]
#def MTmind(a,b):
#    return (sum([a[i]==b[i] for i in range(len(a))]),sum([a[i] in b for i in range(len(a))]))
#If you want to return a tuple, uncomment this one and comment out the other one
