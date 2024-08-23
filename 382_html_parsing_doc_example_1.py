from html.parser import HTMLParser
from functools import reduce 

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()

with open("html_path", "r") as html_handle: 
    lines = html_handle.readlines() 
    # revise 
    #for i in range(len(lines)): 
    #    lines[i] = lines[i].strip() 
    html_str = reduce(lambda x, y : x + y, lines)

parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
"""
Exercise 1 : Parse an entire HTML file instead of hard coded 
HTML content 

Exercise 2: Explore html.parser package to know more methods 
like handle_starttag, handle_endtag, handle_data 
"""