Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
[DEBUG ON]
[DEBUG OFF]
class Date:
    pass

D = Date()
type(D)
<class '__main__.Date'>
D.__dict__
{}
D.day = 26
D.__dict__
{'day': 26}
D.month = 1
D.__dict__
{'day': 26, 'month': 1}
D.year = 2023
D.__dict__
{'day': 26, 'month': 1, 'year': 2023}
D.day
26
D.month
1
D.year
2023
class Date:
    pass

republic_day_of_india = Date()
type(republic_day_of_india)
<class '__main__.Date'>
republic_day_of_india.day = 26
republic_day_of_india.month = 1
republic_day_of_india.year = 2023
republic_day_of_india.__dict__
{'day': 26, 'month': 1, 'year': 2023}
my_birth_date = Date()
my_birth_date.__dict__
{}
my_birth_date.day = 1
my_birth_date.month = 11
my_birth_date.year = 1986
my_birth_date.__dict__
{'day': 1, 'month': 11, 'year': 1986}
D = Date(26, 1, 2023)