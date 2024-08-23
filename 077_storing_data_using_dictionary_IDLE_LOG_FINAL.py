Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
T = (4096, 2160)
T[0]
4096
T[1]
2160
D = {'resX':4096, 'resY':2160}
D['resX']
4096
D['resY']
2160
my_computer = ('Intel', 'GSkill Trident 32 GB', 'nvidia 10Ti', 'LG 4K')
my_computer
('Intel', 'GSkill Trident 32 GB', 'nvidia 10Ti', 'LG 4K')
my_computer = {'CPU':'Intel 6950x', 'GPU':'nVidia 1080Ti', 'RAM':'G. Skill Trident 32GB', 'Monitor':'LG 4K'}
my_computer['CPU']
'Intel 6950x'
my_computer['GPU
            
SyntaxError: unterminated string literal (detected at line 1)
my_computer['GPU']
            
'nVidia 1080Ti'
my_computer['RAM']
            
'G. Skill Trident 32GB'
my_computer['Monitor']
            
'LG 4K'
book = {'publisher':'Sams publishing', 'language':'English', 'ISBN-10':0672227509, 'ISBN-13':9780672227509, 'weight':1.290, 'dimensions':(3.28, 18.75, 23.11)}
            
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
book = {'publisher':'Sams publishing', 'language':'English', 'ISBN-10':'0672227509', 'ISBN-13':9780672227509, 'weight':1.290, 'dimensions':(3.28, 18.75, 23.11)}
            
book
            
{'publisher': 'Sams publishing', 'language': 'English', 'ISBN-10': '0672227509', 'ISBN-13': 9780672227509, 'weight': 1.29, 'dimensions': (3.28, 18.75, 23.11)}
book['publisher']
            
'Sams publishing'
book['weight']
            
1.29
book['language']
            
'English'
book = {'publisher':'Sams publishing', 'language':'English', 'ISBN-10':'0672227509', 'ISBN-13':9780672227509, 'weight':1.290, 'dimensions':{'depth':3.28, 'length':18.75, 'height':23.11} }
            
book['dimensions']
            
{'depth': 3.28, 'length': 18.75, 'height': 23.11}
book['dimensions']['depth']
            
3.28
book['dimensions']['length']
            
18.75
book['dimensions']['height']
            
23.11
book = {'publisher':'Sams publishing', 'language':'English', 'ISBN-10':'0672227509', 'ISBN-13':9780672227509, 'weight':1.290, 'dimensions':{'depth':3.28, 'length':18.75, 'height':23.11}, 'DOP':{'day':26, 'month':1, 'year':2023}}
            
book['DOP']['day']
            
26
