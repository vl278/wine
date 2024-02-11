import sys
for line in sys.stdin:
    ele = line.strip().split(',')
    print(ele[3]+' '+ele[11])
