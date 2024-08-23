import sys

def main():
    s = input("Enter a string:")
    sub = input("Enter a sub-string whose indices must be searched:")
    indices = []
    search_index = 0

    while sub in s[search_index : ]:
        ind = s.index(sub, search_index)
        indices.append(ind)
        search_index = ind + 1

    for i in range(len(indices)):
        print("%d occurrence at index %d" % (i+1, indices[i]))

    sys.exit(0)
    
main() 
