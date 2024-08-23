"""
python_book = {
    'title': 'Learning Python', 
    'author' : ['Mark Lutz'], 
    'pages' : 1569, 
    'price': 10.50, 
    'edition':5 
    'pub_year': {'day':24, 'month':5, 'year:2008}
}

{'day':31, 'month':1, 'year':2023}
"""

class Date: 
    def __init__(self, init_day, init_month, init_year): 
        self.day = init_day 
        self.month = init_month 
        self.year = init_year

class Book: 
    def __init__(self, bk_title, bk_author_list, bk_pages, 
                bk_price, bk_edition, bk_pub_year): 
        self.title = bk_title 
        self.author = bk_author_list 
        self.pages = bk_pages 
        self.price = bk_price 
        self.edition = bk_edition 
        self.pub_year = bk_pub_year 


def main(): 
    learning_python_book = Book("Learning Python", ['Mark Lutz'], 1569, 10.50, 5, Date(25, 5, 2008))
    print(learning_python_book.__dict__)

main()