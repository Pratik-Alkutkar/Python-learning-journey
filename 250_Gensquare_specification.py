gs = Gensquare(N) # 
PRECONDITION: N must be a positive integer 

for x in gs: 
    print(x) 
# ON console 
0^2 
1^2 


(N-1)^2 

gs = Gensquare(0) # Error 
gs = Gensquare(-5) # Error 

gs = Gensquare(5) 
for x in gs: 
    print(x) 
0 
1 
4 
9 
16 