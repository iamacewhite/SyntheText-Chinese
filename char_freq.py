from collections import Counter
import cPickle as cp
cnt=0
filename ='./data/newsgroup/newsgroup.txt'
with open(filename, 'rb') as f:
    c = Counter()
    for x in f:
        x=x.decode('gbk')
        c += Counter(x.strip())
        cnt+=len(x.strip())
        #print c
print cnt

for key in c:
    c[key]=float(c[key])/cnt
    print key,c[key]

d = dict(c)
#print d
with open("./data/models/char_freq.cp",'wb') as f:
    cp.dump(d,f)
