s = "Test String"
T = (100, 200, 300, 400)
L = [True, 10, 3.14, "Hello", (-1, -2)]
D = {100:1000, 3.14:2000, "xyz":3000}
S = {-1, -2, -3, -4, -5}

print("type(s):%s, type(T):%s" % (type(s), type(T)))
print("type(L):%s, type(D):%s" % (type(L), type(D)))
print("type(S):%s" % type(S))

print("string:")
for c in s:
    print(c)

print("tuple:")
for x in T:
    print(x)

print("list:")
for element in L:
    print(element)

print("dictionary:")
for key in D:
    print(key, D[key])

print("set:")
for n in S:
    print(n)

    
