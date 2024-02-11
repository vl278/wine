import sys
dic={}
for line in sys.stdin:
    ele = line.strip().split(' ')
   # print(ele)
    if dic.get(ele[0]) ==  None :
        res=[]
        res.append(float(ele[1]))
        res.append(1)
        dic[ele[0]]= res

    else:
        cnt = dic.get(ele[0])[1]
        old_suma = dic.get(ele[0])[0]
        new_suma = old_suma + float(ele[1])
        res = []
        res.append(new_suma)
        res.append((cnt+1))
        dic[ele[0]] = res
for value_key in dic.keys():
    print('quality = '+str(value_key)+
          ' average sugar='+str(dic.get(value_key)[0]/dic.get(value_key)[1]) +
          ' count='+str(dic.get(value_key)[1]))