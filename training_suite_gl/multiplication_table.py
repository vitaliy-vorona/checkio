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


def draw_table_lc():
    index = 1
    table = ''
    while index < 11:
        for i in range(1,11):
            i *= index
            if i < 10:
                table += ''.join(str(i)).rjust(4)
            elif i > 99:
                table += ''.join(str(i)).rjust(4)
            else:
                table += ''.join(str(i)).rjust(4)
        table += '\n'
        index += 1
    return table

print(draw_table_lc())
