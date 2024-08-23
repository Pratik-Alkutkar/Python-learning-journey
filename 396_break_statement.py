# 1 
for variable in iterable:
    if cond:
        break

# 2
for variable in iterable:
    if cond:
        # do something
    else:
        # do something 
        break

# 3
for variable in iterable:
    if cond:
        # do something
    elif cond1:
        # do something
    elif cond2:
        break
    else:
        # do something

        
# 4
i = 0
while i < N:
    if cond:
        break
    i = i + 1

# 5
for variable in iterable:
    if cond:
        break