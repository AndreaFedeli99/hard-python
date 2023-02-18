
def read_lists_from_file(fn):
    lines = [line.strip() for line in open(fn).readlines()]
    return [int(elem) for elem in lines[0].split(',')], [int(elem) for elem in lines[1].split(',')]

def build_matrix(l1, l2):
    matrix = []
    for i in range(len(l1)):
        row = []
        for j in range(len(l1)):
            if i == j:
               row.append(str(l1[i] + l2[j]))
            else:
                row.append('0')
        matrix.append(row)
    return matrix

def write_to_file(fn, matrix):
    with open(fn, mode='a+', encoding='utf-8') as f:
        for row in matrix:
            f.write(','.join(row) + "\n")

l1, l2 = read_lists_from_file("Hard-Python/Lesson4/data/file_02.txt")
matrix = build_matrix(l1, l2)
write_to_file("Hard-Python/Lesson4/data/file_03.txt", matrix)
