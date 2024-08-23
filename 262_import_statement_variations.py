"""
1: import package_name 
    [Entire package will be in memory, 
    will be accessible through package_name]

2: import package_name as package_name_alias 
    where package_name_alias is a shorter name of package 
    derived from original package_name
    [
        Entire package will be in memory, 
        will be accessible through package_name_alias
    ]

3: from package_name import attribte_name 
    where attribute_name is one of the 
    function, classes, data constant, nested package 
    implemented within package_name 
    [
        only object associated with attribute_name will be in memory 
        and will be accessible through attribute_name
    ]

4: from package_name import attribute_name as attribute_name_alias 

    where attribute_bame is one of the following: 
    function, class, data constant, nested package implemented 
    within package name 

    where attribute_name_alias is a shorter name attribute 
    based on attribute_name

     [
        only object associated with attribute_name will be in memory 
        and will be accessible through attribute_name_alias
    ]
"""

# Internals of variations: 
# import math as m 

import math 
m = math 
del math 

# from math import sin 
import math 
sin = math.sin 
del math 

# from math import sin as s 
import math 
s = math.sin 
del math 