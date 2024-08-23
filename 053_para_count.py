'''
@commandline: # python paracount.py file1 file2 ... 

paracount_1     file1 
paracount_2     file2 


paracount_n     filen 
total_paras     total 
'''

'''
Hint: 
    Traverse through the file line by line. 
    While accessing each line maintain the state 
    whether you are starting with new para or 
    inside the old para. 

    Starting point of new para? 
    First charater must be tab. And there must be 
    at least one character other than tab char. 
'''