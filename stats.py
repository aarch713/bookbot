
def get_bookContent(path):
    with open(path) as f:
        book_content = f.read()
    return book_content

def get_book_char_count_list(path):
    
    final_dic = {}
    final_list= []
    for i in get_bookContent(path):
        i = i.lower()
        if i not in final_dic:
            final_dic[i] = 1
        else:
            final_dic[i] += 1
    #return len(book_content.split())
    for char in final_dic:
        if char == " ":
            continue
        
        final_list.append({"char": char, "num": final_dic[char]})
    
    final_list.sort(reverse=True, key=sort_on)
    return final_list

def get_book_text_len(path):
    
    book_content = get_bookContent(path)
    
    return len(book_content.split())

def sort_on(items):
    return items["num"]

