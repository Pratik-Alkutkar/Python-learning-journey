import sys 
import random 
import numpy as np 

def ndim_shape(a, msg="Array:"): 
    assert type(a) == np.ndarray, "TypeError"
    print(msg)
    print("Dim:{}, Shape:{}".format(a.ndim, a.shape))

def ways_of_creation(): 
    print("ndarray creation ways:")
    a1 = np.arange(5)
    a2 = np.arange(1, 5) 
    a3 = np.arange(10, 20, 3)
    a4 = np.arange(1.1, 5.5)
    a5 = np.arange(1.1, 16.6, 1.2)
    
    L1 = [10, 20, 30, 40]
    L2 = [[1,2], [3,4], [5,6]]
    L3 = [[[1,2,4], [4,5,6]], [[7,8,9], [10,11,12]], [[13,14,15], [16,17,18]], 
          [[19,20,21], [22,23,24]]]
    a6 = np.array(L1)
    print(a6)
    print("Shape:{}, Dim:{}".format(a6.shape, a6.ndim))
    a7 = np.array(L2)
    print(a7)
    print("Shape:{}, Dim:{}".format(a7.shape, a7.ndim))
    a8 = np.array(L3)
    print(a8)
    print("Shape:{}, Dim:{}".format(a8.shape, a8.ndim))

    a9 = np.zeros(5)
    a10 = np.zeros((2, 3))
    a11 = np.zeros((3, 2, 2))
    ndim_shape(a9, msg='a9:')
    ndim_shape(a10, msg='a10:')
    ndim_shape(a11, msg='a11:')
    a12 = np.zeros_like(a9)
    a13 = np.zeros_like(a10)
    a14 = np.zeros_like(a11)
    ndim_shape(a12, msg='a12:')
    ndim_shape(a13, msg='a13:')
    ndim_shape(a14, msg='a14:')

    a15 = np.ones(5)
    ndim_shape(a15, msg='a15:')
    a16 = np.ones_like(a15) 
    ndim_shape(a16, msg='a16:')

    a17 = np.empty(5)
    ndim_shape(a17, msg='a17:')
    a18 = np.empty_like(a17)
    ndim_shape(a18, msg='a18:')
    print("a17:", a17)
    print("a18:", a18)

    a19 = np.full(5, fill_value=7)
    a20 = np.full_like(a19, fill_value=8)
    ndim_shape(a19, msg='a19:')
    ndim_shape(a20, msg='a20:')
    print("a19:", a19)
    print("a20:", a20)

    m = np.identity(3)
    print("m:", m)
    ndim_shape(m, "m:")

def different_dtypes(): 
    pass 

def vector_scaler_ops(): 
    print("vector scaler ops:")
    a = np.arange(1, 6)
    print("a:", a)
    print("a+2:", a+2)
    print("a-2", a-2)
    print("a*2", a*2)
    print("a//2:", a//2)
    print("a/3", a/3)
    print("a % 2:", a % 2)
    print("a**4", a**4)
    print("1/a:", 1/a)
    print("a > 2:", a > 2)
    print("a >= 2:", a >= 2)
    print("a < 2:", a < 2)
    print("a <= 2", a <= 2)
    print("a == 2:", a== 2)
    print("a != 2:", a != 2)

def vector_vector_ops(): 
    print("vector-vector ops:")
    a1 = np.arange(1, 6)
    a2 = np.arange(2, 11, 2)
    print("a1:", a1, "a2:", a2)
    print("a1 + a2:", a1 + a2)
    print("a1 - a2:", a1 - a2)
    print("a1 * a2:", a1 * a2) 
    print("a2 // a1:", a2 // a1)
    print("a2 / a1:", a2 / a1)
    print("a2 %% a1:", a2 % a1)
    print("a1**a2:", a1**a2)
    print("a1 > a2:", a1 > a2)
    print("a1 >= a2:", a1 > a2)
    print("a1 < a2:", a1 < a2)
    print("a1 <= a2:", a1 <= a2)
    print("a1 == a2:", a1 == a2)
    print("a1 != a2:", a1 != a2)

def index_range_slice():
    print("Indexing:one dimensional ndarray")
    a = np.arange(10)
    print("a[0]:", a[0])
    print("a[3]:", a[3])
    print("a[-1]:", a[-1])
    print("a[-4]:", a[-4]) 
    try: 
        print("a[50]:", a[50])
    except: 
        exc_name, exc_data, _ = sys.exc_info() 
        print(exc_name, exc_data, sep=':')
    print("len(a):", len(a))
    print("traversing single dimensional array using indexing")
    for i in range(len(a)): 
        print("a[{}]:{}".format(i, a[i]))
    print("-" * 65)
    print("Range:one dimensional ndarray")
    a = np.arange(15)
    for i in range(len(a)): 
        a[i] = random.randint(1, 100)
    print("Randomly built array for testing range & slice:", a)
    print("range test:")
    print("a[2:8]:", a[2:8])
    print("a[-10:-4]:", a[-10:-4])
    print("a[:5]:", a[:5])
    print("a[10:]:", a[10:])
    print("a[:]:", a[:])
    print("slice test:")
    print("a[1:8:2]:", a[1:8:2])
    print("a[10:2:-3]:", a[10:2:-3])
    print("a[-13:-1:4]:", a[-13:-1:4])
    print("a[-2:-9:-3]:", a[-2:-9:-3])
    print("a[::2]:", a[::2])
    print("a[1::2]:", a[1::2])
    print("a[::-1]:", a[::-1])
    print("two dimensional array:")
    L = [[1,2,3], [4,5,6], [7,8,9]]
    a2d = np.array(L)
    ndim_shape(a2d, "array from index_range_slice():")
    print("a2d[0][2]:", a2d[0][2])
    print("a2d[0,2]:", a2d[0, 2])
    print("traversing a2d:")
    for i in range(len(a2d)):
        for j in range(len(a2d[i])): 
            print("a2d[{},{}]:{}".format(i, j, a2d[i, j])) 
    print("3d array:")
    L = [[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]]
    a3d = np.array(L)
    print("a3d:\n", a3d)
    ndim_shape(a3d, "a3d from index_range_slice()")

    print("Printing 2d arrays:")
    print("a3d[0]:", a3d[0])    # 2d array 
    print("a3d[1]:",a3d[1])     # 2d array 

    print("Printing 1d arrays:")
    print("a3d[0, 0]:", a3d[0,0]) # 1d array 
    print("a3d[0, 1]:", a3d[0, 1]) # 1d array 

    print("a3d[1, 0]:", a3d[1, 0]) # 1d array 
    print("a3d[1, 1]:", a3d[1, 1]) # 1d array 

    print("Traversing through 1d array:")
    for i in range(len(a3d[1, 0])):
        print("a3d[1, 0, {}]:{}".format(i, a3d[1, 0, i]))

    print("Trversing through 3d array:")
    for i in range(len(a3d)): 
        for j in range(len(a3d[i])): 
            for k in range(len(a3d[i, j])): 
                print("a3d[{},{},{}]:{}".format(i, j, k, a3d[i, j, k]))

    print("index, range, slice of 2d array:")
    L = [
            [1, 2, 3, 4, 5, 6], 
            [7, 8, 9, 10, 11, 12], 
            [12, 14, 15, 16, 17, 18],
            [19, 20, 21, 22, 23, 24], 
            [25, 26, 27, 28, 29, 30] 
    ]
    a2d = np.array(L)
    print("a2d[1:4, 2:5]:", a2d[1:4, 2:5])
    print("a2d[:3, 4:]:", a2d[:3, 4:])
    print("a2d[::2, 1::2]", a2d[::2, 1::2])
    print("a2d[::-1, 3:]", a2d[::-1, 3:])

def main(): 
    ways_of_creation() 
    different_dtypes() 
    vector_scaler_ops() 
    vector_vector_ops() 
    index_range_slice() 
main() 