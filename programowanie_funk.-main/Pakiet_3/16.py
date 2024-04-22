def remove_whitespace(string_list):

    return [s.strip() for s in string_list]


words = ['  hello ', 'world!  ', '  python  ', '       awesome']
no_whitespace_list = remove_whitespace(words)
print("Lista bez białych znaków:", no_whitespace_list)