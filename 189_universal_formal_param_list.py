def combo_1(a, b, c, *args, p, q):
    print("In combo_1")
    print(a, b, c)
    print(args)
    print(p, q)

combo_1(10, 20, 30, 40, 50, 60, p=1.1, q=2.2)

def combo_2(x, y, p=100, q=200, **kwargs):
    print("In combo_2")
    print(x, y)
    print(p, q)
    print(kwargs)


combo_2(1000, 2000, q=-200, a=1.1, b=2.2)

def test(*args, **kwargs):
    print("In test")
    print(args)
    print(kwargs)

test(10, 20, 30, 40, 50, 60, p=1.1, q=2.2) # combo_1
test(1000, 2000, q=-200, a=1.1, b=2.2) # combo_2 

#-------------------------------------------------------
