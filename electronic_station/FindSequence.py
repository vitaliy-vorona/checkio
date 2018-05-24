# search for consecutive 4 elements in NxN matrix in vertical, horizontal and diagonal position


def checkio(matrix):
    index_i = 0
    index_j = 0
    itter_counter = 0
    end_index = len(matrix) - 1
    target_sequence = []

    # search from top to bottom
    while True:
        if len(target_sequence) == 4:
            return True

        if index_i == len(matrix):
            index_j += 1
            index_i = 0
            target_sequence.clear()

        if index_j == len(matrix):
            index_i = 0
            break

        current_value = matrix[index_i][index_j]

        if len(target_sequence) >= 1 and current_value == target_sequence[-1]:
            target_sequence.append(current_value)

        else:
            target_sequence.clear()
            target_sequence.append(current_value)

        index_i += 1

    # diagonal search from right to left and top to bottom
    while True:
        if len(target_sequence) == 4:
            return True
        if end_index == -1 or index_i == len(matrix):
            itter_counter += 1
            index_i = itter_counter
            end_index = len(matrix) - 1
            target_sequence.clear()

        if len(matrix) - itter_counter <= 3:
            index_i = 0
            itter_counter = 0
            break

        current_value = matrix[index_i][end_index]

        if len(target_sequence) >= 1 and current_value == target_sequence[-1]:
            target_sequence.append(current_value)

        else:
            target_sequence.clear()
            target_sequence.append(current_value)

        end_index -= 1
        index_i += 1

    # diagonal search from top to bottom and right to left
    while True:
        if len(target_sequence) == 4:
            return True
        if end_index == -1 or index_i == len(matrix):
            itter_counter += 1
            index_i = 0
            end_index = len(matrix) - itter_counter
            target_sequence.clear()

        if len(matrix) - itter_counter <= 3:
            index_i = 0
            index_j = 0
            itter_counter = 0
            break

        current_value = matrix[index_i][end_index]

        if len(target_sequence) >= 1 and current_value == target_sequence[-1]:
            target_sequence.append(current_value)

        else:
            target_sequence.clear()
            target_sequence.append(current_value)

        end_index -= 1
        index_i += 1

    # diagonal search from left to right and top to bottom
    while True:
        if len(target_sequence) == 4:
            return True
        if index_j == len(matrix):
            index_i = 0
            itter_counter += 1
            index_j = itter_counter
            target_sequence.clear()

        if len(matrix) - itter_counter <= 3:
            index_i = 0
            index_j = 0
            itter_counter = 0
            break

        current_value = matrix[index_i][index_j]

        if len(target_sequence) >= 1 and current_value == target_sequence[-1]:
            target_sequence.append(current_value)

        else:
            target_sequence.clear()
            target_sequence.append(current_value)

        index_i += 1
        index_j += 1

    # diagonal search from top to bottom and left to right
    while True:
        if len(target_sequence) == 4:
            return True
        if index_i == len(matrix):
            itter_counter += 1
            index_i = itter_counter
            index_j = 0
            target_sequence.clear()

        if len(matrix) - itter_counter <= 3:
            index_i = 0
            index_j = 0
            break

        current_value = matrix[index_i][index_j]

        if len(target_sequence) >= 1 and current_value == target_sequence[-1]:
            target_sequence.append(current_value)

        else:
            target_sequence.clear()
            target_sequence.append(current_value)

        index_i += 1
        index_j += 1

    # Horizontal search
    while True:
        if len(target_sequence) == 4:
            return True
        if index_j == len(matrix):
            index_i += 1
            index_j = 0
            target_sequence.clear()

        if index_i == len(matrix):
            return False

        current_value = matrix[index_i][index_j]

        if len(target_sequence) >= 1 and current_value == target_sequence[-1]:
            target_sequence.append(current_value)

        else:
            target_sequence.clear()
            target_sequence.append(current_value)

        index_j += 1


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [2, 1, 4, 1],
        [1, 1, 4, 1],
        [1, 3, 4, 6],
        [1, 1, 4, 5]
    ]) == True, "Vertical"
    assert checkio([
        [2, 1, 4, 1],
        [1, 3, 1, 1],
        [1, 1, 4, 6],
        [1, 1, 4, 5]
    ]) == True, "Vertical from right to left"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 2],
        [1, 3, 2, 2, 3],
        [4, 1, 2, 3, 1],
        [5, 2, 3, 5, 5],
        [1, 3, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [2, 1, 1, 6, 2],
        [1, 3, 6, 2, 7],
        [4, 6, 7, 7, 1],
        [6, 2, 7, 9, 5],
        [1, 7, 4, 1, 1]
    ]) == True, "Long Digi"
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    assert checkio([[2, 3, 6, 5, 6, 2, 8, 3, 7, 4],
                    [6, 9, 5, 9, 7, 6, 8, 5, 1, 6],
                    [6, 8, 2, 6, 1, 9, 3, 6, 6, 4],
                    [5, 8, 3, 2, 3, 8, 7, 4, 6, 4],
                    [2, 3, 1, 4, 5, 1, 2, 5, 6, 9],
                    [5, 4, 8, 7, 5, 5, 8, 4, 9, 5],
                    [9, 7, 9, 9, 5, 9, 9, 8, 1, 2],
                    [5, 1, 7, 4, 8, 3, 4, 1, 8, 8],
                    [5, 3, 3, 2, 6, 1, 4, 3, 8, 8],
                    [4, 8, 1, 4, 5, 8, 8, 7, 4, 7]]) == True, "last one"
