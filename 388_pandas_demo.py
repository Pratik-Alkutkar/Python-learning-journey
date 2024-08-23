import sys 
import numpy as np 
import pandas as pd 
from pandas import Series, DataFrame 
from functools import reduce 

def series_demo(): 
    """
        Def: Series: One dimensional array like object containing 
        values of homogenious data type and associated array of labels 
        called the index. 
    """
    a = np.array([10, 20, 30, 40, 50])
    print("a:", a)
    srs_1 = pd.Series([10, 20, 30, 40, 50])
    print("srs_1:\n", srs_1)
    print("srs_1.array:", srs_1.array)
    print("type(srs_1.array):", type(srs_1.array))
    print("srs_1.index:", srs_1.index)
    print("type(srs_1.index):", type(srs_1.index))

    data = [10, 20, 30, 40, 50]
    labels = ["a", "b", "c", "d", "e"]
    srs2 = Series(data, index=labels)
    print("srs2:\n", srs2)
    print("srs2.array:\n", srs2.array)
    print("srs2.index:\n", srs2.index)

    print("srs2['a']:", srs2['a'])
    print("srs2[['a', 'b', 'c']]:\n", srs2[['a', 'b', 'c']])

    print("srs2[srs2 >= 30]:\n", srs2[srs2 >= 30])
    print("srs2 * 2:\n", srs2*2)

    D = {"x":1.1, "y":2.2, "z":3.3}
    srs3 = pd.Series(D)
    print("srs3:\n", srs3)
    print("srs3['x']:{}, srs3['y']:{}, srs3['z']:{}".format(srs3['x'], srs3['y'], srs3['z']))
    print("pd.isna(srs3):\n", pd.isna(srs3))

    s_data = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}
    srs4 = pd.Series(s_data, index=labels)
    print("srs4:\n", srs4)
    print("pd.isna(srs4)\n", pd.isna(srs4))

    srs5 = pd.Series(s_data, index=['A', 'B', 'C', 'E', 'F', 'G', 'H'])
    print("srs5:\n", srs5)
    print("pd.isna(srs5):\n", pd.isna(srs5))

    srs6 = pd.Series(s_data, ['a', 'B', 'c', 'D', 'e', 'F'])
    print("srs6:\n", srs6)
    print("pd.isna(srs6):\n", pd.isna(srs6))

    D = {'a':10, 'b':20, 'c':30}
    srs7 = pd.Series(D)
    print("srs7:\n", srs7)
    srs7.index = ['x', 'y', 'z']
    print("srs7:\n", srs7)
    srs7['x'] = 1.1 
    srs7['y'] = 2.2 
    srs7['z'] = 3.3 
    print("srs7:\n", srs7)
    srs7.array.name=""
    srs7.index.name="cname"
    print("srs7:\n",srs7)

def dataframe_demo(): 
    points = {
        'x':[1.1,2.2,3.3,4.4,5.5], 
        'y':[6.6,7.7,8.8,9.9,10.10], 
        'z':[11.11,12.12,13.13,14.14,15.15]
    }

    df = pd.DataFrame(points)
    print("df:\n", df)

    data = {
        'state': ['MH', 'MH', 'MH', 'MP', 'MP', 'MP'], 
        'year': [2015, 2016, 2017, 2018, 2019, 2020], 
        'population': [110.32, 112.45, 113.78, 99.34, 100.23, 101.55]
    }

    frame = pd.DataFrame(data)
    print("frame:\n", frame)
    print("Printing head of the frame")
    print(frame.head())

    print("Printing tail of the frame")
    print(frame.tail())

    print("Printing Columns:")
    print("frame.columns:", frame.columns)
    print("States:\n", frame['state'])
    print("Year:", frame['year'])
    print("population:", frame['population'])
    print("frame[['state', 'population']]:\n", 
          frame[['state', 'population']])
    print("Statem Column:")
    print(frame.state)
    print("Year Columns:")
    print(frame.year)
    print("Population Column:")
    print(frame.population)

    print("Frame:\n", frame)
    print("Rows")   
    print("Row with index 0:")
    print(frame.loc[0])
    print("Row with index 1:")
    print(frame.loc[1])
    print("Row wtih index 2:")
    print(frame.loc[2])

    print("Change Column:")
    frame['year'] = 2023 
    print("Frame:\n", frame)
    frame['year'] = np.arange(2010, 2016)
    print("Frame:\n", frame)

    frame['gdp'] = None
    print("Frame\n:", frame)

    frame['western'] = frame['state'] == 'MH'
    print("Frame\n:", frame)

    avg_pop = (reduce(lambda x, y : x + y, frame['population']))/len(frame["population"])
    print("avg_pop:", avg_pop)

def main(): 
    series_demo()
    dataframe_demo()

    sys.exit(0)

main()

"""
lst = [some data elements]
a = np.array(lst)

D = {key:value pairs}
s = pd.Series(D)
s.array -> D.values() 
s.index -> D.keys() 

    C1  C2  C3          Cn  -> D.keys() 
    v   v   v           v 
    v   v   v           v 


    v   v   v           v

D = {
        'C1_name':[v_R1, v_R2, ..., v_Rn], 
        'C2_name':[v_R1, v_R2, ..., v_Rn], 

        'Cm_name':[v_R1, v_R2, ..., v_Rn]
    }

df = pd.DataFrame(D)
#-------------------------------------------------------
CONDITIONAL CHANGE: 

frame['Ci'] = COND(frame[Cj]) 

Considering there are N rows in dataframe 

frame.loc(k)[Ci] = COND(frame.loc(k)[Cj])

for 0 <= k < N

lambda x : f(x) 
lambda x1, x2, ..., xn : rhs_exp(x1, ..., xn)

frame[C] = map(lambda x : f(x), frame[C])
filter(lambda x : cond(x),  frame[C]) 
reduce(lambda x, y : binary_op(x, y), frame[C])
"""