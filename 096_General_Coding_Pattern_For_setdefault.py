L = [IMMUTABLE OBJECTS LIST]

D = {some dict}

for x in L:
    if x in D.keys():
        v = D[x]
        PROCESS(v)
    else:
        D[x] = v
        v = D[x]
        PROCESS(x)

#-------------------------------------

for x in L:
    v = D.setdefault(x, v)
    PROCESS(v)

#-------------------------------------
    
