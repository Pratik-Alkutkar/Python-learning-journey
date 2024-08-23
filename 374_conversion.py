s1 = '{10 : 100, 20 : 200}'
# do not use any package 
# covert this string into a dict 
# you are allowed to use all built in funtions of 
# str class. other python language features 

s1 = s1.strip() 
s1 = s1[1:len(s1)-1]
L = s1.split(",")
pairs = [] 
for entry in L: 
    tmp = entry.split(":")
    for i in range(len(tmp)): 
        tmp[i] = tmp[i].strip() 
    pairs.append(tmp) 
for (key, value) in pairs: 
    print(key, type(key)) # str 
    print(value, type(value)) # str 

pairs_types = [] 
for pair in pairs: 
    pairs_types.append((int(pair[0]), int(pair[1])))
print(pairs_types)
D = dict(pairs_types)
print(D)
for (key, value) in D.items(): 
    print(key, type(key))
    print(value, type(value))

# more tedious example 
s2 = '{True : [100, 200, 300], False : (-1, -2, -3)}'

s2 = s2.strip() 
s2 = s2[1:len(s2)-1]

in_first = 1 
in_second = 2 

words = [] 
state = in_first 

start_index = 0 
for i in range(len(s2)): 
    if state == in_first and s2[i] == ':' : 
        words.append(s2[start_index : i])
        state = in_second 
        start_index = i+1
    elif state == in_second and s2[i] == ',': 
        words.append(s2[start_index:i])
        state = in_first 
        start_index = i+1 
words.append(s2[start_index:])
for i in range(len(words)): 
    words[i]=words[i].strip()

print(words)

"""
complex info D : dict 

D -> json -> str -> bytes -> travel over network -> 

D to str -> json.dumps 
str to bytes -> str.encode

bytes -> str -> json -> dict 

bytes -> str -> str.decode 
str -> dict -> json.lods 

bool, int, float, str, tuple, list, dict, set, None 
Dict 
-> Json -> str 

""" 