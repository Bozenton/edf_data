import os
import re

txt = "S101R01"

y = re.split('S|R',txt)
# print(y)
# s = y[2]
# print(int(s))


if __name__ == '__main__':
    names = os.listdir('.')
    for i, file_name in enumerate(names):
        name = file_name.split('.')[0]
        if file_name.split('.')[1] == 'edf':
            temp = re.split('S|R', name)
            sub = int(temp[1])
            run = int(temp[2])
            if run not in [4, 8, 12]:
                os.remove('./'+file_name)