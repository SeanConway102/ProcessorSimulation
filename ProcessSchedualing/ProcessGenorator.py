from Process import *
import random
nextId=0


# Gernerate a new random process
def generatenew(minlen,maxlen):
    global nextId
    r=int(random.uniform(minlen,maxlen))
    p = Process(nextId,r)
    nextId+=1
    return p

