def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    return (f'{one}{delimiter}{two}')


new_string = get_summ('Learn', 'Python')
print(new_string.upper())
