Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
C = """String class methods continued..."""
# Index method
s = "Hello,World
SyntaxError: unterminated string literal (detected at line 1)
s = "Hello,World"
s[6]
'W'
# index operator -> Index is known, character is given
# index method -> character is known, index is given
s.index('W')
6
s = 'aaBBBaaBBBaaCCCaaDDD'
s.index('aa')
0
# second version of index method, to find out multiple occurrences
s.index('aa', 1)
5
s.index('aa', 6)
10
s.index('aa', 11)
15

= RESTART: C:/Users/yoges/OneDrive/Documents/CPA/PYTHON/BATCH_CODES/BATCH_46/SESSION_036/all_occurrences.py
Enter a string:aaBBBaaBBBaaCCCaaDDD
Enter a sub-string whose indices must be searched:aa
1 occurrence at index 0
2 occurrence at index 5
3 occurrence at index 10
4 occurrence at index 15
# count method
s = 'aaBBBaaBBBaaCCCaaDDD'
s.count('aa')
4
s.count('BBB')
2
s.count('a')
8
s.count('C')
3
s.count('x')
0
# find method
# find is a lenient version of index
s
'aaBBBaaBBBaaCCCaaDDD'
sub = 'XYZ'
s.index(sub)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s.index(sub)
ValueError: substring not found
if sub in s:
    print(s.index(sub))

    
# s.index(sub, search_index) --> sub in s[search_index : ] is TRUE -> No exception | is False -> ValueError
s.find(sub)
-1
C = """
/etc/passwd
pratik:x:1000:1000:Pratik Pramod Alkutkar,,,:/home/pratik:/bin/bash

user_name:x:user_id:group_id:Name,room_number,extension_number:home_dir:Shell_path
"""
s = "pratik:x:1000:1000:Pratik Pramod Alkutkar,,,:/home/pratik:/bin/bash"
L = s.split(":")
L
['pratik', 'x', '1000', '1000', 'Pratik Pramod Alkutkar,,,', '/home/pratik', '/bin/bash']
s = 'aa##BBBBB##cccccc##$$$$##657657575##dgfddsgdsg'
L = s.split('##')
L
['aa', 'BBBBB', 'cccccc', '$$$$', '657657575', 'dgfddsgdsg']
L = s.split('##', 3)
L
['aa', 'BBBBB', 'cccccc', '$$$$##657657575##dgfddsgdsg']
s.rsplit('##')
['aa', 'BBBBB', 'cccccc', '$$$$', '657657575', 'dgfddsgdsg']
s.rsplit('##', 3)
['aa##BBBBB##cccccc', '$$$$', '657657575', 'dgfddsgdsg']
L = [10, 20, 30, 40]
sep = '##'
sep.join(L)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    sep.join(L)
TypeError: sequence item 0: expected str instance, int found
s = 'aaBBBaaCCCaaDDDaa'
s.split('aa')
['', 'BBB', 'CCC', 'DDD', '']
s = ':abc:'
s.split(':')
['', 'abc', '']
L = ['Yogeshwar', 'Rohit', 'Radhika', 'Sneha']
sep
'##'
sep.join(L)
'Pratik##Roh##Radhika##Sneha'
s = sep.join(L)
print()

print(s)
#Pratik##Rohit##Radhika##Sneha
# so far: index(), count(), strip(), lstrip(), rstrip(), split(), lsplit(), join()
# so far: index(), count(), strip(), lstrip(), rstrip(), split(), rsplit(), join() (ignore lsplit() there is no such method)
# find()
s1='abc'
s2 = 'ABC'
s3 = s1.upper()
s3
'ABC'
s1
'abc'
id(s1)
1980935561072
id(s3)
1980970001200
s4 = s2.lower()
s2
'ABC'
s4
'abc'
id(s2)
1980935564336
id(s4)
1980940296304
L = [10, 20, 30, 40]
L1 = []
for x in L:
    L1.append(str(x))

    
L
[10, 20, 30, 40]
L1
['10', '20', '30', '40']
sep=':'
sep.join(L1)
'10:20:30:40'
':'.join(map(lambda x : str(x), [10, 20, 30, 40]))
'10:20:30:40'
s1 = "ABC"
id(s1)
1980935564336
id(s1.lower())
1980971155376
s = 'core programming academy'
s1 = s.title()
print(s)
core programming academy
print(s1)
Core Programming Academy
s1 = 'abc'
s2 = 'ABC'
s3 = 'Core Programming Academy'
s1.islower()
True
s2.isupper()
True
s3.istitle()
True
s2.islower()
False
s1.isupper()
False
s1.istitle()
False
s1 = 'acbABC'
s2 = '654634535'
s3 = 'abc123'
s1.isalpha()
True
s2.isalpha()
False
s2.isdigit()
True
s3.isalnum()
True
s4 = 'abc123$%^#$$'
s4.isprintable()
True
# methods covered so far: index(), count(), strip(), lstrip(), rstrip(), split(), rsplit(), join(), find(), upper(), lower()
# title(), isupper(), islower(), istitle(), isalpha(), isdigit(), isalnum()
for i in range(255):
    print(i, chr(i))

    
0 
1 
2 
3 
4 
5 
6 
7 
8 
9 	
10 

11 
12 
13 

14 
15 
16 
17 
18 
19 
20 
21 
22 
23 
24 
25 
26 
27 
28 
29 
30 
31 
32  
33 !
34 "
35 #
36 $
37 %
38 &
39 '
40 (
41 )
42 *
43 +
44 ,
45 -
46 .
47 /
48 0
49 1
50 2
51 3
52 4
53 5
54 6
55 7
56 8
57 9
58 :
59 ;
60 <
61 =
62 >
63 ?
64 @
65 A
66 B
67 C
68 D
69 E
70 F
71 G
72 H
73 I
74 J
75 K
76 L
77 M
78 N
79 O
80 P
81 Q
82 R
83 S
84 T
85 U
86 V
87 W
88 X
89 Y
90 Z
91 [
92 \
93 ]
94 ^
95 _
96 `
97 a
98 b
99 c
100 d
101 e
102 f
103 g
104 h
105 i
106 j
107 k
108 l
109 m
110 n
111 o
112 p
113 q
114 r
115 s
116 t
117 u
118 v
119 w
120 x
121 y
122 z
123 {
124 |
125 }
126 ~
127 
128 
129 
130 
131 
132 
133 
134 
135 
136 
137 
138 
139 
140 
141 
142 
143 
144 
145 
146 
147 
148 
149 
150 
151 
152 
153 
154 
155 
156 
157 
158 
159 
160  
161 ¡
162 ¢
163 £
164 ¤
165 ¥
166 ¦
167 §
168 ¨
169 ©
170 ª
171 «
172 ¬
173 ­
174 ®
175 ¯
176 °
177 ±
178 ²
179 ³
180 ´
181 µ
182 ¶
183 ·
184 ¸
185 ¹
186 º
187 »
188 ¼
189 ½
190 ¾
191 ¿
192 À
193 Á
194 Â
195 Ã
196 Ä
197 Å
198 Æ
199 Ç
200 È
201 É
202 Ê
203 Ë
204 Ì
205 Í
206 Î
207 Ï
208 Ð
209 Ñ
210 Ò
211 Ó
212 Ô
213 Õ
214 Ö
215 ×
216 Ø
217 Ù
218 Ú
219 Û
220 Ü
221 Ý
222 Þ
223 ß
224 à
225 á
226 â
227 ã
228 ä
229 å
230 æ
231 ç
232 è
233 é
234 ê
235 ë
236 ì
237 í
238 î
239 ï
240 ð
241 ñ
242 ò
243 ó
244 ô
245 õ
246 ö
247 ÷
248 ø
249 ù
250 ú
251 û
252 ü
253 ý
254 þ
