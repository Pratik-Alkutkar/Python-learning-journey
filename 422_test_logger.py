from logger import logger 
from time import sleep 

@logger 
def compute1(a, b, c): 
    rs1 = a - b 
    rs2 = b + c 
    rs3 = c - a 
    return (rs1 * rs2) + rs3 

@logger
def compute2(x,y): 
    return x**2 - y**2 

@logger
def compute3(n):
    if n == 0: 
        return 1 
    else: 
        return n * compute3(n-1)

ret = compute1(10, b=20, c=30)
print("ret:", ret)
sleep(1)
ret = compute2(3, y=1)
print("ret:", ret)
sleep(2)
ret = compute3(n=5)
print("ret:", ret)
sleep(1)
ret = compute1(6, 3, 1)
print("ret:", ret)
sleep(1)
ret = compute1(a=8, b=3, c=1)
print("ret:", ret)
sleep(1)
ret = compute2(4, 1)
print("ret:", ret)
sleep(1)
ret = compute3(3)
print("ret:", ret)
sleep(1)
ret = compute2(x=6, y=1)
print("ret:", ret)