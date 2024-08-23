import os 
import sys 

def cpa_call(*cmdline): 
    ret = os.spawnv(cmdline)
    return ret 