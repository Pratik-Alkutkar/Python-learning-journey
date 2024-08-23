"""
@goal: To build sqlite3 data base from csv file. 
@author: Pratik Pramod Alkutkar 
@commandline: 
# python3 build_db_from_csv.py csv_file_path db_file_path 
@assumptions: 
1) The first line of the CSV file contains the column names
2) First column is a primary key. 
"""

import sys 
import sqlite3 

def main(argc:int, argv:list)->None: 
    if argc != 3: 
        print("UsageError:Correct Usage:%s csv_path db_path" % argv[0])
        sys.exit(-1)

    try: 
        csv_handle = open(argv[1], "r")
    except FileNotFoundError: 
        print("Bad path for csv file")
        sys.exit(-1)
    except PermissionError: 
        print("insufficient permission to access csv file")
        sys.exit(-1)
    except: 
        exc_name, exc_data, _ = sys.exc_info() 
        print(exc_name, exc_data, sep=':')
        sys.exit(-1)

    try: 
        conn = sqlite3.connect(argv[2])
    except: 
        exc_name, exc_data, _ = sys.exc_info() 
        print(exc_name, exc_data, sep=':')
        sys.exit(-1)

    header = next(csv_handle) 
    header = header.strip()
    H = header.split(",")
    column_list = [] 
    for h_entry in H: 
        tmp = h_entry.split(":")
        T = (tmp[0], tmp[1])
        column_list.append(T)
    table_name = argv[2]
    create_query = 'create table {} ('.format(table_name)
    create_query += ' ' + column_list[0][0] + ' ' + column_list[0][1] + ' ' + 'primary key'
    for i in range(1, len(column_list)): 
        col_name = column_list[i][0]
        col_type = column_list[i][1]
        create_query += ', ' + col_name + ' ' + col_type 
    create_query += ')'
    
    # obtain cursor object 
    # file create query 
    curs = conn.cursor() 
    try: 
        curs.execute(create_query)
    except: 
        exc_name, exc_data, _ = sys.exc_info() 
        print(exc_name, exc_data, sep=':')
        sys.exit(-1)

    query_data = [] 
    for line in csv_handle:
        line = line.strip() 
        line = line.split(",")
        for i in range(len(line)): 
            if column_list[i][1] == 'integer': 
                line[i] = int(line[i])
            elif column_list[i][1] == 'float': 
                line[i] = float(line[i])            
        query_data.append(tuple(line))
    
    insert_query = 'insert into {} values({}?)'.format(table_name, '?,'*(len(column_list)-1))
    try: 
        curs.executemany(insert_query, query_data)
    except: 
        exc_name, exc_data, _ = sys.exc_info() 
        print(exc_name, exc_data, sep=':')
        sys.exit(-1)

    print(curs.rowcount)
    conn.commit() 

    select_query = 'select * from {}'.format(table_name) 
    try: 
        curs.execute(select_query)
    except: 
        exc_name, exc_data, _ = sys.exc_info() 
        print(exc_name, exc_data, sep=':')
        sys.exit(-1)
    db_data = curs.fetchall() 
    for t in db_data: 
        print(t) 
        
    sys.exit(0)

main(len(sys.argv), sys.argv)
