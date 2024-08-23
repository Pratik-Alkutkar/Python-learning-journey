import sys 
import random 
import numpy as np 
import scipy 
import scipy.stats as stats 
import numpy.linalg as linalg

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

def boolean_indexing(): 
    print("boolean indexing:")
    strings = np.array(["abc", "pqr", "lmn", "abc", "pqr", "abc", "abc", "xyz"])
    print('strings == "abc":', strings == "abc")
    a_of_lists = np.array([[1,2], [2,3], [3,4], [4,5], [5,6], [7,8], [9,10], [11,12]])
    print("a_of_lists[strings == 'abc']:", a_of_lists[strings == 'abc'])
    bool_index_arr = (strings == "abc") | (strings == "xyz")
    print('bool_index_arr:', bool_index_arr)
    print('a_of_lists[bool_index_arr]:', 
          a_of_lists[bool_index_arr])
    print('a_of_lists[(strings == "abc") | (strings == "xyz")]', 
        a_of_lists[(strings == "abc") | (strings == "xyz")])

    print("Applying filter on elements of array and creating new array satisfying filter")
    a = np.array([10, 20, 30, 40, 50, 60, 70, 80])
    a1 = a[a <= 50]
    print("a1==a[a <= 50]:", a1)

def fancy_indexing(): 
    print("fancy_indexing():")
    
    a = np.array(
        [
            [0, 0, 0, 0], 
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
    )
    print("before:a:", a)
    for i in range(len(a)): 
        a[i] = (i + 1) * 10
    print("after:a:", a)
    
    print("fancy indexing starts from here:")
    a = np.zeros((8, 4))    # 8 rows, 4 cols 
    print("a:", a)

    for i in range(8): 
        a[i] = i 

    print("after a[i]=i:a:\n", a)
    print("a[[4, 3, 0, 6]]:", a[[4, 3, 0, 6]])
    print("a[[-1, -3, -5]]:", a[[-1, -3, -5]])

    a = np.zeros((8, 8))
    cnt = 0 
    for i in range(8): 
        for j in range(8): 
            a[i, j] = cnt 
            cnt += 1 
    print("a:", a)
    a1 = a[[2, 4, 1, 6], [0, 2, 4, 6]]
    print("a[2,0]:{}, a[4, 2]:{}, a[1, 4]:{}, a[6, 6]:{}".format(a[2, 0], a[4, 2], a[1, 4], a[6, 6]))
    # single dimensional array: a[2, 0], a[4, 2], a[1, 4], a[6, 6]
    print("a1==(a1 = a[[2, 4, 1, 6], [0, 2, 4, 6]]):", a1)
    a[[2, 4, 1, 6], [0, 2, 4, 6]] = 500 
    print("a[2,0]:{}, a[4, 2]:{}, a[1, 4]:{}, a[6, 6]:{}".format(a[2, 0], a[4, 2], a[1, 4], a[6, 6]))

def reshape_demo(): 
    print("In reshape_demo():")
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    print("a:", a)
    ndim_shape(a, "a:")
    dim_2d = (3, 4)
    a = a.reshape(dim_2d)
    ndim_shape(a, "a:")
    print("a:", a)

    # 64 = 8 x 8 | 2 x 4 x 8 | 2 x 4 x 4 x 2 | 2 x 2 x 2 x 2 x 2 x 2 
    a = np.array([i for i in range(64)])
    print("a:", a) 
    ndim_shape(a, "a:")

    a = a.reshape((8, 8))
    print("a:", a) 
    ndim_shape(a, "a:")

    a = a.reshape((2, 4, 8))
    print("a:", a) 
    ndim_shape(a, "a:")

    a = a.reshape(2, 4, 4, 2)
    print("a:", a) 
    ndim_shape(a, "a:")

    a = a.reshape((2, 2, 2, 2, 2, 2))
    print("a:", a) 
    ndim_shape(a, "a:")

def basic_statistic(): 
    print("In basic_statistic():")
    lst = [1.1, 3.4, 7.8, 6.5, 2.3, 9.9, 3.4, 1.1, 1.1, 7.8, 3.4, 3.4, 11.32, 3.4]
    a = np.array(lst)
    am = np.mean(a)
    print("Arithemetic mean:%.3f" % am)
    md = np.median(a)
    print("Median:%.3f" % md)
    v = np.var(a)
    print("variance:%.3f" % v)
    sd = np.std(a)
    print("standard deviation:%.3f" % sd)
    md = stats.mode(a)
    print("Mode:", md)

def linear_algebra(): 
    x = np.array(
            [
                [1.1, 2.2, 3.3], 
                [4.4, 5.5, 6.6]
            ]
        ) # 2x3 
    y = np.array(
        [
            [7.7, 8.8, 9.9, 10.10], 
            [11.11, 12.12, 13.13, 14.14], 
            [15.15, 16.16, 17.17, 18.18]
        ]
    )
    ndim_shape(x, "x:")
    ndim_shape(y, "y:")
    z = x.dot(y)
    print("z:", z)
    ndim_shape(z, "z:")
    # z = x @ y 

    m = np.array(
        [
            [43.32, 4.2, 1.3], 
            [-5.6, 1.2, 9.4], 
            [5.3, 6.7, 9.1]
        ]
    )

    if linalg.det(m) != 0: 
        m_inv = linalg.inv(m)
        In = m @ m_inv 
        print(In) 
        ndim_shape(In, "In:")
    
    """
        linalg.diag(sqaure_m) -> diagonal as 1D array 
        linalg.dot(M{mxn}, N{nxp}) -> 2D array mxp 
        linalg.det(square_m) -> float -> determinant of square_m 
        linalg.inv(square_m) -> inverse of given matrix 
         linalg.solve
        Ax = b 
        system of linear equation solve 
        If there are n variables, then there must be n linear equations 
        a11 * x1 +    ...     + a1n * xn = c1 
        .
        .

        .
        an1 * x1 +    ...       + ann * xn = cn 

        A = [
            a11                 1an 


            an1                 ann 
        ]

        b = [
            c1 
            c2 


            cn 
        ]

        x = [
            x1 
            x2 


            xn 
        ]

        Ax=b 
        x1=?, x2=?, ..., xn=?
        
        linalg.eig(square_m) -> eigenvalue and eigenvector of square_m 
        linalg.qr(m) -> QR decompisition 
        linalg.svd(m) -> Single value decomposition 
        linalg.pinv(square) -> Moore-Penrose pseudo inverse matrix 
    """

def main(): 
    ways_of_creation() 
    different_dtypes() 
    vector_scaler_ops() 
    vector_vector_ops() 
    index_range_slice() 
    boolean_indexing()
    fancy_indexing()
    reshape_demo() 
    basic_statistic()
    linear_algebra() 

main() 

