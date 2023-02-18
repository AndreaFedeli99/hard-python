
fn1 = 'Hard-Python/Lesson4/data/file_03_1.txt'
fn2 = 'Hard-Python/Lesson4/data/file_03_2.txt'
out = 'Hard-Python/Lesson4/data/file_03_3.txt'

def merge_common_lines(fn1, fn2):
    f1 = open(fn1).readlines()
    f2 = open(fn2).readlines()

    f1_lines = {f1[i].strip(): i for i in range(len(f1))}
    f2_lines = {f2[i].strip(): i for i in range(len(f2))}

    common_lines = []
    for line,index in f1_lines.items():
        if line in f2_lines:
            common_lines.append((index, line))
    
    with open(out, mode='a+', encoding='utf-8') as f:
        for line in sorted(common_lines, key=lambda x: x[0], reverse=True):
            f.write("{}\n".format(line[1]))

merge_common_lines(fn1, fn2)