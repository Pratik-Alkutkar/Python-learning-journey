import sys 

def validate_tags(tags:list)->bool: 
    stack = []
    for tag in tags: 
        if tag.startswith("/"): 
            if len(stack) == 0: 
                return False 
            if stack[-1] != tag[1 : ]: 
                return False 
            else: 
                stack.pop()
        else: 
            stack.append(tag)
    if len(stack) == 0: 
        return True 
            
def get_all_tags(html_path:str)->tuple: 
    try: 
        html_handle = open(html_path, "r")
    except: 
        exc_name, exc_data, exc_tb = sys.exc_info() 
        print(exc_name, exc_data, sep=':')
        sys.exit(-1)

    opening_tags = []
    closing_tags = []
    all_tags = [] 

    IN_TAG, OUT_TAG = 1, 2 
    state = OUT_TAG
    start_index, end_index = 0, 0
    for line in html_handle: 
        line = line.strip() 
        for i in range(len(line)):
            if state == OUT_TAG and line[i] == '<':
                state = IN_TAG 
                start_index = i+1 
            elif state == IN_TAG and line[i] == ">":
                state = OUT_TAG 
                end_index = i 
                tag = line[start_index:end_index]
                tag_text = tag
                if tag.startswith("/"): 
                    tag_text = tag[1:]
                if not (tag_text.isalnum): 
                    print("HTML SYNTAX ERROR")
                all_tags.append(tag)
                if tag.startswith("/"): 
                    closing_tags.append(tag)
                else: 
                    opening_tags.append(tag)
    html_handle.close() 
    return (all_tags, opening_tags, closing_tags)

def main(argc:int, argv:list)->None: 

    if argc != 2: 
        print("UsageError : %s html_file_path".format(argv[0]))
        sys.exit(-1) 

    all_tags, opening_tags, closing_tags = get_all_tags(argv[1])
    print(all_tags, opening_tags, closing_tags)
    ret = validate_tags(all_tags)
    if ret == True: 
        print("HTML file tags are well-formed")
    else: 
        print("HTML file tags are malformed")

    sys.exit(0) 

main(len(sys.argv), sys.argv)