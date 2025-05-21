def reverse(s):
    reverse_str=""
    for char in s:
        reverse_str=char+reverse_str
    return reverse_str

text=input('Enter the string')
print(f'{reverse(text)}')