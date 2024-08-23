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

def main(): 
    ways_of_creation() 
    different_dtypes() 
    vector_scaler_ops() 
    vector_vector_ops() 

main() 