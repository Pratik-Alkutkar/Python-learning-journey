import sys, os 

# Language 
def cpa_print(*args, sep=' ', end='\n', file=sys.stdout, flush=False): 
    

    # LOGIC 
    if len(args) == 0: 
        return None 
    
    s = ""
    for i in range(len(args)-1): 
        s = s + str(args[i]) + sep 
    s = s + str(args[len(args)-1]) + end 
    
    # DOMAIN
    sb = s.encode() # string to be printed as bytes 
    fd = file.fileno()
    os.write(fd, sb) # os.write(file.fileno(), s.encode())
    if flush == True: 
        os.fsync(fd)

filename = "abc.txt"
f_handle = open(filename, "w")
cpa_print("PRINTING WITHOUT print()")
cpa_print()
cpa_print(10, sep=':')
cpa_print(10, 20, sep='#')
cpa_print(10, 20, 30, sep='$$$', file=f_handle, flush=True)
cpa_print(10, 20, 30, 40, 50, sep='#$#', end='[END]\n', file=f_handle, flush=True)
f_handle.close()

# tuple length N 
# indices : 0, 1, 2, ...., N-2, N-1 
# 0         N-2