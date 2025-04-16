s = "dwajkl   7329HDAI4367^$73Q&(Y dwdwa   ^&*$(#))"
count_cap = 0
count_small = 0
count_spaces = 0
count_digits = 0
count_symbols = 0
for ch in s:
    ascii_code = ord(ch)
    if ascii_code >= 97 and ascii_code <= 122:
        count_small += 1
    elif ascii_code >= 65 and ascii_code <= 90:
        count_cap += 1
    elif ascii_code >= 48 and ascii_code <= 57:
        count_digits += 1
    elif ascii_code == 32:
        count_spaces += 1
    else:
        count_symbols += 1

print(
    f" cap = {count_cap}, small ={count_small}, digit = {count_digits}, space ={count_spaces}, symbol = {count_symbols}"
)
my_string = "hfejJH&(*$&#@hdkwajhdHdwadDJKWHdwadwaADkjWAB)"
# Swap case
result = ""
for ch in my_string:
    ascii_code = ord(ch)
    if ascii_code >= 65 and ascii_code <= 90:
        result += chr(ascii_code + 32)
    elif ascii_code >= 97 and ascii_code <= 122:
        result += chr(ascii_code - 32)
    else:
        result += ch

print(result)
