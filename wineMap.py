import sys
flag_header= True
for line in sys.stdin:
    if flag_header:
        flag_header=False
        continue
    ele = line.strip().split(',')
    print(ele[11]+' '+ele[3])
