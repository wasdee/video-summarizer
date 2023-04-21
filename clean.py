
def remove_dup_line(lines):
    """
    remove the dup consecutive line while keep the order
    """
    prev_line = None
    for line in lines:
        if line != prev_line:
            yield line
        prev_line = line

# read file with *.txt 
from pathlib import Path

dir_ = Path('translate').glob('*.txt')
for fp in dir_:
    with fp.open('r', encoding='utf-8') as f:
        lines = f.readlines()
    lines = remove_dup_line(lines)

    f_clean = fp.parent / (fp.stem + '_clean.txt')
    with f_clean.open('w', encoding='utf-8') as fp:
        fp.writelines(lines)
