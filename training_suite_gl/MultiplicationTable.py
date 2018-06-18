def draw_table():
    index_row = 1
    index_col = 1
    result = ''
    while index_row < 11:
        while index_col < 11:
            x = index_col * index_row
            if x < 10:
                result += '   ' + (str(x))
            elif x < 100:
                result += '  ' + (str(x))
            else:
                result += ' ' + (str(x))
            index_col += 1
        result += '\n'
        index_row += 1
        index_col = 1
        result.strip()
    return result


print(draw_table())
