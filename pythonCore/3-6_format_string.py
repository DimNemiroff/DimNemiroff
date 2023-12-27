string = 'sdfcv'
length = 28


def format_string(string, length):
    if len(string) < length:
        string = ((length - len(string)) // 2) * ' ' + string 
    return string


print(format_string(string, length))

