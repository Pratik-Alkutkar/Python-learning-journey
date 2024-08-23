Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello,World")
Hello,World
n = 10
print(n)
10
print("The value of n is")
The value of n is
print("The value of n is", n)
The value of n is 10
print("The value of n is %d" % n)
The value of n is 10
n=10
f=3.1415
print("The value of n is %d and the value of f is %f" % (n, f))
The value of n is 10 and the value of f is 3.141500
print("ABCDEFGHIJKLMNOPQRTSUVWXYZabcedfghijklmnopqrstuvwxyz0123456789~`!@#$^&*()_+-={}|[]\:";'<>?,./")
      
SyntaxError: unterminated string literal (detected at line 1)
print("ABCDEFGHIJKLMNOPQRTSUVWXYZabcedfghijklmnopqrstuvwxyz0123456789~`!@#$^&*()_+-={}|[]\:;'<>?,./")
      
ABCDEFGHIJKLMNOPQRTSUVWXYZabcedfghijklmnopqrstuvwxyz0123456789~`!@#$^&*()_+-={}|[]\:;'<>?,./
print("The value of n is 10")
      
The value of n is 10
print("The value of n is", n, "The value of f is", f)
      
The value of n is 10 The value of f is 3.1415
10 % 3
      
1
f=3.1415161718
      
katrina=10
      
vicky=3.14
      
print("Katrina=%d, Vicky=%f" % (katrina, vicky))
      
Katrina=10, Vicky=3.140000
f=3.1415161718
      
f_num=3.1415161718
      
print("f_num=%f" % f_num)
      
f_num=3.141516
print("f_num=%.2f" % f_num)
      
f_num=3.14
print("f_num=%.3f" % f_num)
      
f_num=3.142
print("f_num=%.4f" % f_num)
      
f_num=3.1415
print("f_num=%.5f" % f_num)
      
f_num=3.14152
print("f_num=%.6f" % f_num)
      
f_num=3.141516
print("f_num=%.10f" % f_num)
      
f_num=3.1415161718
my_int = 10
      
my_float=3.1415
      
my_str = "Yogeshwar"
      
print("My Name is %s, My roll number is %d, My CGPA is %.1f" % (my_str, my_int, my_float))
      
My Name is Yogeshwar, My roll number is 10, My CGPA is 3.1
s = "My Name is {} My Roll is My CGPA is {}".format(my_str, my_int, my_float)
      
print(s)
      
My Name is Yogeshwar My Roll is My CGPA is 10
